# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

Name: workstation-payload
Version: %{_version}
Release: %{_release}%{?dist}
Summary: Payload component of workstation image.
License: MPL-2.0
BuildArch: noarch
Source0: %{name}-%{_version}-%{_release}-rootfs.tar.gz
Requires: code
Requires: firefox
Requires: nvidia-driver
Requires: nvidia-driver-cuda
Requires: nvidia-open-kmod
Requires: thunderbird

%description
%{summary}

%install
tar xzvf %{SOURCE0} -C %{buildroot}

%files
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
