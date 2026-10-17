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
autopart --nohome --type=lvm
ostreecontainer --transport=containers-storage --url=@TAG@ --no-signature-verification

%post --erroronfail
bootc switch --mutate-in-place --transport registry @TAG@
%end

reboot --eject
