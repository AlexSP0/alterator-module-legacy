%define _unpackaged_files_terminate_build 1

Name: alterator-module-legacy
Version: 0.1.0
Release: alt1

Summary: Alterator manager backends generator for support the old alterator modules.
License: GPLv2+
Group: Other
URL: https://gitlab.basealt.space/alt/alterator-module-legacy

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: python3-devel

%description
Alterator manager backends generator for support the old alterator modules. Alterator browser legacy objects interface.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_rpmlibdir/
mkdir -p %buildroot%_alterator_datadir/applications
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
#mkdir -p %buildroot%_sysconfdir/polkit-1/rules.d

install -v -p -m 755 -D %name.filetrigger %buildroot%_rpmlibdir/
install -v -p -m 755 -D alterator-generate-legacy-backends %buildroot%_libexecdir/%name
install -v -p -m 755 -D alterator-object-run %buildroot%_libexecdir/%name
install -v -p -m 644 -D alterator-object-run.application %buildroot%_alterator_datadir/applications
install -v -p -m 644 -D ru.basealt.alterator.legacy.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.legacy.policy %buildroot%_datadir/polkit-1/actions
#install -v -p -m 644 -D 49-alterator-interface-legacy.rules %buildroot%_sysconfdir/polkit-1/rules.d

%files
%dir %_libexecdir/%name
%dir %_sysconfdir/alterator/backends
%_rpmlibdir/%name.filetrigger
%_libexecdir/%name/alterator-generate-legacy-backends
%_libexecdir/%name/alterator-object-run
%_alterator_datadir/applications/*.application
%_datadir/dbus-1/interfaces/ru.basealt.alterator.legacy.xml
%_datadir/polkit-1/actions/ru.basealt.alterator.legacy.policy
#%_sysconfdir/polkit-1/rules.d/49-alterator-interface-legacy.rules

%changelog
* Mon Dec 11 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
