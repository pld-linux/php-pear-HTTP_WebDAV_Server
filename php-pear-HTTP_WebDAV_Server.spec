%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Server

Summary:	%{_pearname} - WebDAV Server Baseclass
Summary(pl):	%{_pearname} - podstawowa klasa serwera WebDAV
Name:		php-pear-%{_pearname}
Version:	0.99.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	54c5211c696b7e7a02a8ad6efa807091
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

In PEAR status of this package is: %{_status}.

%description -l pl
W wiêkszo¶ci zgodna z RFC2518 klasa pomocnicza do implementacji
servera WebDAV.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{db,Server,Tools}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Server/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Server
install %{_pearname}-%{version}/db/*.sql $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/db
install %{_pearname}-%{version}/Tools/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Tools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
