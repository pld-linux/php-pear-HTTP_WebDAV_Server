%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Server

%define	_rc RC3
%define	_rel 1
Summary:	%{_pearname} - WebDAV Server Baseclass
Summary(pl):	%{_pearname} - podstawowa klasa serwera WebDAV
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1.%{_rc}.%{_rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	d970aa31ae9005c50c4ee17e8b65a94d
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3
Requires:	php-pear >= 4:1.0-9.2
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

In PEAR status of this package is: %{_status}.

%description -l pl
W większości zgodna z RFC2518 klasa pomocnicza do implementacji
servera WebDAV.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Server
%{php_pear_dir}/%{_class}/%{_subclass}/Tools/*
