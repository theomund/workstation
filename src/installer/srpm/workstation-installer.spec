# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

Name: workstation-installer
Version: %{_version}
Release: %{_release}%{?dist}
Summary: Installer component of workstation image.
License: MPL-2.0
ExclusiveArch: x86_64
Source0: %{name}-%{_version}-%{_release}-rootfs.tar.gz
Requires: anaconda
Requires: anaconda-dracut
Requires: anaconda-install-env-deps
Requires: biosdevname
Requires: dracut-config-generic
Requires: dracut-network
Requires: grub2-efi-x64-cdboot
Requires: lorax-templates-almalinux
Requires: net-tools
Requires: prefixdevname
Requires: python3-mako
Requires: squashfs-tools

%description
%{summary}

%install
tar xzvf %{SOURCE0} -C %{buildroot}

%files
%{_localstatedir}/mnt

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
