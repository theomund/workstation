# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

Name: workstation-payload
Version: %{_version}
Release: %{_release}%{?dist}
Summary: Payload component of workstation image
License: MPL-2.0
ExclusiveArch: x86_64
URL: https://github.com/theomund/workstation
Source0: file://%{name}-%{_version}-%{_release}-rootfs.tar.gz
Obsoletes: PackageKit-command-not-found <= 2.0.0
Requires: cockpit-machines
Requires: code
Requires: ffmpeg
Requires: ffmpeg-libs
Requires: firefox
Requires: nvidia-driver
Requires: nvidia-driver-cuda
Requires: nvidia-open-kmod
Requires: thunderbird

%description
%{summary}

%prep

%build

%check

%install
tar xzvf %{SOURCE0} -C %{buildroot}

%post
%systemd_post workstation-payload.service
sed -i 's/^#mount_program =.*/mount_program = ""/; s/^mountopt =/#&/' /usr/share/containers/storage.conf

%files
%{_datadir}/flatpak/preinstall.d/%{name}.preinstall
%{_datadir}/flatpak/remotes.d/%{name}.flatpakrepo
%{_libdir}/firefox/distribution/policies.json
%{_presetdir}/10-%{name}.preset
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_unitdir}/mcelog.service.d/10-%{name}.conf
%{_unitdir}/nvidia-persistenced.service.d/10-%{name}.conf
%attr(0755,-,-) %{_libexecdir}/%{name}

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
