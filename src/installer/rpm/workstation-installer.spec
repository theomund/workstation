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
Source0: file://%{name}-%{_version}-%{_release}-rootfs.tar.gz
Requires: anaconda, anaconda-install-img-deps, anaconda-dracut
Requires: dracut-config-generic, dracut-network, net-tools
Requires: grub2-efi-x64-cdboot, plymouth, default-fonts-core-sans
Requires: default-fonts-other-sans, google-noto-sans-cjk-fonts
Requires: xorriso, squashfs-tools

%description
%{summary}

%prep
%build
%check

%install
tar xzvf %{SOURCE0} -C %{buildroot}

%post
cp -a /usr/lib/efi/*/*/EFI /boot/efi/

echo "install:x:0:0:root:/root:/usr/libexec/anaconda/run-anaconda" >> /etc/passwd
echo "install::14438:0:99999:7:::" >> /etc/shadow
passwd -d root

rm -v /usr/lib/systemd/system-generators/systemd-gpt-auto-generator

kernel=$(kernel-install list --json pretty | jq -r '.[] | select(.has_kernel == true) | .version')
DRACUT_NO_XATTR=1 dracut --force -v --zstd --reproducible --no-hostonly \
  --add "anaconda" \
  --install /usr/share/anaconda/workstation-installer.ks \
  "/usr/lib/modules/${kernel}/initramfs.img" "${kernel}"

%files
%{_bindir}/list-harddrives
%{_datadir}/anaconda/%{name}.ks
%{_localstatedir}/mnt
%{_localstatedir}/roothome
%{_prefix}/lib/image-builder/bootc/iso.yaml
%{_prefix}/lib/systemd/logind.conf.d/%{name}.conf
%{_sysconfdir}/anaconda.repos.d
%{_sysconfdir}/anaconda/conf.d/90-%{name}.conf
%{_sysconfdir}/systemd/system/autovt@.service
%{_sysconfdir}/systemd/system/default.target
%{_sysconfdir}/systemd/user/pipewire.service.d/%{name}.conf
%{_sysconfdir}/systemd/user/pipewire.socket.d/%{name}.conf
%{_tmpfilesdir}/%{name}.conf

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
