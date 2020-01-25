#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	String
%define		pnam	RexxParse
Summary:	String::RexxParse - Perl implementation of REXX parse command
Summary(pl.UTF-8):	String::RexxParse - implementacja perlowa polecenia analizującego REXX
Name:		perl-String-RexxParse
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e46a78a8f805086884e23965ef754c2b
URL:		http://search.cpan.org/dist/String-RexxParse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some long-time REXX programmers switching to Perl find it difficult to
give up REXX's template-based parsing abilities. This module is my
attempt to provide such parsing in Perl. Consider it BETA level code.
The documentation assumes a familiarity with REXX parse statements.

%description -l pl.UTF-8
Niektórzy doświadczeni programiści REXX-a przerzucający się na Perla
uznali za trudne porzucenie REXX-owych możliwości analizy opartej na
wzorcach. Ten moduł jest próbą udostępnienia takiej analizy w Perlu.
Kod jest na etapie BETA. Dokumentacja zakłada znajomość wyrażeń
analizujących REXX-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
