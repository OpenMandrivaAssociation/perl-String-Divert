%define upstream_name    String-Divert
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	String::Divert - String Object supporting Folding and Diversions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
String::Divert is small Perl 5 module providing a scalar-like string
object with some overloaded operators, supporting the concept of Fold-
ing and Diversion. This allows nested generation of structured output.
The idea is to decouple the sequential generation of output from the
nested and non-sequential structure of the output.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/String/*
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.0
+ Revision: 404415
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.96-6mdv2009.0
+ Revision: 258390
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.96-5mdv2009.0
+ Revision: 246474
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-3mdv2008.1
+ Revision: 138069
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.96-2mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 0.96-2mdv2007.0
+ Revision: 89743
- use the mkrel macro
- Import perl-String-Divert

* Mon Nov 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.96-1mdk
- 0.96

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.94-1mdk
- initial Mandriva package

