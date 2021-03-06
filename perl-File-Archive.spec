#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	File
%define		pnam	Archive
Summary:	File::Archive - figure out what is in an archive file
Summary(pl.UTF-8):	File::Archive - przeglądanie, co jest w pliku archiwum
Name:		perl-File-Archive
Version:	0.53
Release:	10
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d61787275af3627af4eb92bae6f7527
URL:		http://search.cpan.org/dist/File-Archive/
BuildRequires:	perl-Archive-Tar >= 1.08-2
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Archive Perl module for figuring out what is in an archive file.

%description -l pl.UTF-8
Moduł Perla File::Archive umożliwia przeglądanie zawartości archiwów.

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
%doc Changes *txt
%{perl_vendorlib}/File/Archive.pm
%{_mandir}/man3/*
