%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Archive
Summary:	File::Archive perl module
Summary(pl):	Modu� perla File::Archive
Name:		perl-File-Archive
Version:	0.53
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Archive-Tar
BuildRequires:	perl-Compress-Zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Archive - Figure out what is in an archive file.

%description -l pl
File::Archive umo�liwia przegl�danie zawarto�ci archiw�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *txt
%{perl_vendorlib}/File/Archive.pm
%{_mandir}/man3/*
