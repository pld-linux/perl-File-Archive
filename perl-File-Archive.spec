#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Archive
Summary:	File::Archive - figure out what is in an archive file
Summary(pl):	File::Archive - przegl±danie, co jest w pliku archiwum
Name:		perl-File-Archive
Version:	0.53
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d61787275af3627af4eb92bae6f7527
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Archive-Tar >= 1.08-2
BuildRequires:	perl-Compress-Zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Archive Perl module for figuring out what is in an archive file.

%description -l pl
Modu³ Perla File::Archive umo¿liwia przegl±danie zawarto¶ci archiwów.

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
