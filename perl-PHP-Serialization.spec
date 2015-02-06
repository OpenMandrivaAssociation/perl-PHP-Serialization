%define upstream_name    PHP-Serialization
%define upstream_version 0.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Simple flexible means of converting the output of PHP's serialize()
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PHP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Provides a simple, quick means of serializing perl memory structures
(including object data!) into a format that PHP can deserialize() and
access, and vice versa.

NOTE: Converts PHP arrays into Perl Arrays when the PHP array used
exclusively numeric indexes, and into Perl Hashes then the PHP array did
not.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 655152
- rebuild for updated spec-helper

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 526452
- update to 0.34

* Thu Feb 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.330.0-1mdv2010.1
+ Revision: 507356
- import perl-PHP-Serialization


* Thu Feb 18 2010 cpan2dist 0.33-1mdv
- initial mdv release, generated with cpan2dist
