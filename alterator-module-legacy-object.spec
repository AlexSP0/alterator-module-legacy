Name: alterator-module-legacy-object
Version: 0.1.0
Release: alt1

Summary: Scripts to support the old alterator modules.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-module-legacy-object

BuildArch: noarch

Source0: %name-%version.tar


BuildRequires(pre): rpm-build-python3 
Requires: python3-module-pydbus

%description
Scripts to support the old alterator modules.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/alterator/scripts
mkdir -p %buildroot%_libexecdir/rpm
mkdir -p %buildroot%_datadir/alterator/applications
install -v -p -m 755 -D alterator-browser.filetrigger %buildroot%_libexecdir/rpm
install -v -p -m 755 -D gen-backends.sh %buildroot%_libexecdir/alterator/scripts
install -v -p -m 666 -D legacy-runner.py %buildroot%_libexecdir/alterator/scripts
install -v -p -m 755 -D legacy-run.sh %buildroot%_libexecdir/alterator/scripts
install -v -p -m 666 -D legacy-runner.alterator %buildroot%_datadir/alterator/applications

%files
%_libexecdir/rpm/alterator-browser.filetrigger
%_libexecdir/alterator/scripts/*.sh
%_libexecdir/alterator/scripts/*.py
%_datadir/alterator/applications/legacy-runner.alterator

%changelog
* Wed Nov 22 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
