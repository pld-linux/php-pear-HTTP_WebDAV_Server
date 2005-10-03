%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Server

Summary:	%{_pearname} - WebDAV Server Baseclass
Summary(pl):	%{_pearname} - podstawowa klasa serwera WebDAV
Name:		php-pear-%{_pearname}
Version:	0.99.1
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	54c5211c696b7e7a02a8ad6efa807091
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3
Requires:	php-pear
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
%{php_pear_dir}/%{_class}/%{_subclass}
