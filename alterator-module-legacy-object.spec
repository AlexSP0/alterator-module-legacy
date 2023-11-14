Name: alterator-module-legacy-object
Version: 0.1.0
Release: alt1

Summary: Scripts to support the old alterator modules.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-module-legacy-object

BuildArch: noarch

Source0: %name-%version.tar

%description
Scripts to support the old alterator modules.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/rpm
install -v -p -m 755 -D alterator-browser.filetrigger %buildroot%_libexecdir/rpm
install -v -p -m 755 -D gen-backends.sh %buildroot%_libexecdir/rpm

%post
bash -c "%_libexecdir/rpm/gen-backends.sh /usr/share/alterator/applications/"

%files
%_libexecdir/rpm/alterator-browser.filetrigger
%_libexecdir/rpm/gen-backends.sh

%changelog
* Mon Nov 13 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
