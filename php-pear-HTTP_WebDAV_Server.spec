%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Server

Summary:	%{_pearname} - WebDAV Server Baseclass
Summary(pl):	%{_pearname} - podstawowa klasa serwera WebDAV
Name:		php-pear-%{_pearname}
Version:	0.99
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	565eb8a14cc5cb547891be9e29d591ea
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

This class has in PEAR status: %{_status}.

%description -l pl
W wiêkszo¶ci zgodna z RFC2518 klasa pomocnicza do implementacji
servera WebDAV.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Server

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Server/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Server
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Server/*.php
