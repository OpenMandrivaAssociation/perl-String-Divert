%define real_name String-Divert

Summary:	String::Divert - String Object supporting Folding and Diversions
Name:		perl-%{real_name}
Version:	0.96
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
String::Divert is small Perl 5 module providing a scalar-like string
object with some overloaded operators, supporting the concept of Fold-
ing and Diversion. This allows nested generation of structured output.
The idea is to decouple the sequential generation of output from the
nested and non-sequential structure of the output.

%prep
%setup -q -n %{real_name}-%{version} 

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


