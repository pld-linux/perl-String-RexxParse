#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	RexxParse
Summary:	String::RexxParse - Perl implementation of REXX parse command
Summary(pl):	String::RexxParse - perlowa implementacja polecenia analizuj�cego REXX
Name:		perl-String-RexxParse
Version:	1.08
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some long-time REXX programmers switching to Perl find it difficult
to give up REXX's template-based parsing abilities.  This module is my
attempt to provide such parsing in Perl.  Consider it BETA level code.
The documentation assumes a familiarity with REXX parse statements.

%description -l pl
Niekt�rzy do�wiadczeni programi�ci REXX-a przerzucaj�cy si� na Perla
uznali za trudne porzucenie REXX-owych mo�liwo�ci analizy opartej na
wzorcach. Ten modu� jest pr�b� udost�pnienia takiej analizy w Perlu.
Kod jest na etapie BETA. Dokumentacja zak�ada znajomo�� wyra�e�
analizuj�cych REXX-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
