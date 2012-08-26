%define		subver RC7
%define		rel 2
%define		status		beta
%define		pearname	HTTP_WebDAV_Server
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - WebDAV Server Baseclass
Summary(pl.UTF-8):	%{pearname} - podstawowa klasa serwera WebDAV
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	1.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	eb3e2e1649c91d415d5360d15edb8edf
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.4
Requires:	php-pear >= 4:1.0-9.2
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
W większości zgodna z RFC2518 klasa pomocnicza do implementacji
serwera WebDAV.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/HTTP_WebDAV_Server/* docs/%{pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/WebDAV/Server.php
%{php_pear_dir}/HTTP/WebDAV/Server
%{php_pear_dir}/HTTP/WebDAV/Tools/_parse_*.php
%{php_pear_dir}/HTTP/WebDAV/file.php
