# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

Name: workstation-installer
Version: %{_version}
Release: %{_release}%{?dist}
Summary: Installer component of workstation image
License: MPL-2.0
ExclusiveArch: x86_64
URL: https://github.com/theomund/workstation
Source0: file://%{name}-%{version}-%{_release}-rootfs.tar.gz
Requires: anaconda-dracut
Requires: anaconda-install-img-deps
Requires: anaconda-tui
Requires: dracut-config-generic
Requires: fuse-overlayfs
Requires: grub2-efi-x64-cdboot
Requires: net-tools
Requires: squashfs-tools
Requires: xorriso

%description
%{summary}

%prep
%autosetup -c
sed -i "s/@TAG@/%{version}-%{_release}/g" .%{_datadir}/anaconda/%{name}.ks

%build

%install
cp -a . %{buildroot}

%check

%post
cp -ra /usr/lib/bootupd/updates/EFI /boot/efi/
kver=$(basename /usr/lib/modules/*)
DRACUT_NO_XATTR=1 dracut -f -v "/usr/lib/modules/${kver}/initramfs.img" "${kver}"

%files
%{_bindir}/list-harddrives
%{_datadir}/anaconda/%{name}.ks
%{_prefix}/lib/dracut/dracut.conf.d/%{name}.conf
%{_prefix}/lib/image-builder/bootc/iso.yaml
%{_prefix}/lib/systemd/logind.conf.d/%{name}.conf
%{_sysconfdir}/anaconda.repos.d
%{_sysconfdir}/anaconda/conf.d/90-%{name}.conf
%{_unitdir}/autovt@.service

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
