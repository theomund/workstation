# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

text --non-interactive
zerombr

%pre --erroronfail
: > /tmp/preferred-disk.ks

if [ -b /dev/nvme0n1 ]; then
  echo "ignoredisk --only-use=nvme0n1" > /tmp/preferred-disk.ks
fi
%end

%include /tmp/preferred-disk.ks

clearpart --all --initlabel --disklabel=gpt
autopart --nohome --type=lvm
network --device=link --activate
ostreecontainer --transport=containers-storage --url=ghcr.io/theomund/workstation/payload:@TAG@ --no-signature-verification

%post --erroronfail
bootc switch --mutate-in-place --transport registry ghcr.io/theomund/workstation/payload:@TAG@
%end

reboot --eject
