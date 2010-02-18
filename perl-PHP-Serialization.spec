%define upstream_name    PHP-Serialization
%define upstream_version 0.33

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple flexible means of converting the output of PHP's serialize() into the equivalent Perl memory structure, and vice versa
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PHP/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


