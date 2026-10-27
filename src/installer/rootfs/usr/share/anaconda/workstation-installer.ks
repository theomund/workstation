# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

text --non-interactive
zerombr

%pre --erroronfail
if [ -b /dev/nvme0n1 ]; then echo "ignoredisk --only-use=nvme0n1"; fi > /tmp/preferred-disk.ks
%end

%include /tmp/preferred-disk.ks

clearpart --all --initlabel --disklabel=gpt
reqpart --add-boot
part pv.01 --fstype="lvmpv" --size=1 --grow
volgroup vg0 pv.01
logvol swap --fstype="swap" --vgname=vg0 --name=swap --size=4096
logvol / --fstype="xfs" --vgname=vg0 --name=root --size=10240 --grow
network --device=link --activate
xconfig --startxonboot
ostreecontainer --transport=containers-storage --url=@TAG@ --no-signature-verification

%post --erroronfail
bootc switch --mutate-in-place --transport registry @TAG@
%end

reboot --eject
