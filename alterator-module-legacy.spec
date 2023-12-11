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
Alterator manager backends generator for support the old alterator modules.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_rpmlibdir/
mkdir -p %buildroot%_alterator_datadir/applications
install -v -p -m 755 -D %name.filetrigger %buildroot%_rpmlibdir/
install -v -p -m 755 -D alterator-generate-legacy-backends %buildroot%_libexecdir/%name
install -v -p -m 755 -D alterator-object-run %buildroot%_libexecdir/%name
install -v -p -m 644 -D alterator-object-run.application %buildroot%_alterator_datadir/applications

%files
%_rpmlibdir/%name.filetrigger
%_libexecdir/%name
%_alterator_datadir/applications/*.application

%changelog
* Wed Nov 22 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
