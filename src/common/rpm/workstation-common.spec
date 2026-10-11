# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

Name: workstation-common
Version: %{_version}
Release: %{_release}%{?dist}
Summary: Common component of workstation image
License: MPL-2.0
ExclusiveArch: x86_64
URL: https://github.com/theomund/workstation
Source0: file://%{name}-%{_version}-%{_release}-rootfs.tar.gz
Requires: almalinux-release-nvidia-driver, rpmfusion-nonfree-release, tmux

%description
%{summary}

%prep
%build
%check

%install
tar xzvf %{SOURCE0} -C %{buildroot}

%files
%{_sysconfdir}/localtime
%{_sysconfdir}/yum.repos.d/%{name}.repo

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
