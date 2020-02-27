Name:          hello
Version:       2.8
Release:       1%{?dist}
Summary:       The "Hello World" program from GNU
License:       GPLv3+
URL:           http://ftp.gnu.org/gnu/hello
Distribution:  Tizen
Vendor:        Private
Packager:      Geunsik Lim <leemgs@gmail.com>
Source0:       http://ftp.gnu.org/gnu/hello/hello-2.8.tar.gz

BuildRequires: gettext

Requires(post): info
Requires(preun): info

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*
%{_bindir}/hello

%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING

%changelog
* Tue Sep 22 2017 Geunsik Lim <leemgs@gmail.com>
- Hello version to help developers that have to generate Tizen package
