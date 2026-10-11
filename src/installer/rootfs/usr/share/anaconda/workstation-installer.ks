# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

text --non-interactive
zerombr
ignoredisk --only-use=nvme0n1
clearpart --all --initlabel --disklabel=gpt
reqpart --add-boot
part pv.01 --fstype="lvmpv" --size=1 --grow
volgroup vg0 pv.01
logvol swap --fstype="swap" --vgname=vg0 --name=swap --size=4096
logvol / --fstype="xfs" --vgname=vg0 --name=root --size=10240 --grow
network --bootproto=dhcp --device=link --activate --onboot=on
xconfig --startxonboot
ostreecontainer --transport=containers-storage --url=ghcr.io/theomund/workstation/payload:0.3.0-1 --no-signature-verification

%post --erroronfail
set -eu
bootc switch --mutate-in-place --transport registry ghcr.io/theomund/workstation/payload:0.3.0-1
%end

reboot --eject
