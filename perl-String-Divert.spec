%define upstream_name    String-Divert
%define upstream_version 0.96

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	String::Divert - String Object supporting Folding and Diversions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
String::Divert is small Perl 5 module providing a scalar-like string
object with some overloaded operators, supporting the concept of Fold-
ing and Diversion. This allows nested generation of structured output.
The idea is to decouple the sequential generation of output from the
nested and non-sequential structure of the output.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/String/*
%{_mandir}/*/*
