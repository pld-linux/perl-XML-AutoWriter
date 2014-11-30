#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	XML
%define		pnam	AutoWriter
%include	/usr/lib/rpm/macros.perl
Summary:	XML::AutoWriter - DOCTYPE based XML output
Summary(pl.UTF-8):	XML::AutoWriter - oparte o DOCTYPE wyjście XML
Name:		perl-XML-AutoWriter
Version:	0.4
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b18624c8168e0a38daf39c7c6919ff24
URL:		http://search.cpan.org/dist/XML-AutoWriter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOCTYPE based XML output.

%description -l pl.UTF-8
Oparte o DOCTYPE wyjście XML.

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
%doc CHANGES
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Doctype
%{_mandir}/man3/*
