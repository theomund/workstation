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
Source0: file://%{name}-%{version}-%{_release}-rootfs.tar.gz
Obsoletes: PackageKit-command-not-found <= 2.0.0
Requires: bcvk
Requires: cockpit-machines
Requires: code
Requires: ffmpeg
Requires: nvidia-driver
Requires: nvidia-driver-cuda
Requires: thunderbird
Requires: tmux

%description
%{summary}

%package repo
Summary: Repository configuration for %{name}
Requires: almalinux-release-nvidia-driver
Requires: rpmfusion-nonfree-release

%description repo
%{summary}

%prep
%autosetup -c

%build

%install
cp -a . %{buildroot}

%check

%post
%systemd_post %{name}.service bootc-fetch-apply-updates.timer rpm-ostree-countme.timer

%files
%{_datadir}/flatpak/preinstall.d/%{name}.preinstall
%{_datadir}/flatpak/remotes.d/%{name}.flatpakrepo
%{_libdir}/firefox/distribution/policies.json
%{_presetdir}/10-%{name}.preset
%{_sysconfdir}/containers/storage.conf
%{_sysconfdir}/localtime
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_unitdir}/mcelog.service.d/10-%{name}.conf
%{_unitdir}/nvidia-persistenced.service.d/10-%{name}.conf

%files repo
%{_sysconfdir}/yum.repos.d/%{name}.repo

%changelog
* Sun Sep 27 2026 Theomund <34360334+theomund@users.noreply.github.com> - 0.1.0-1
- Initial package
