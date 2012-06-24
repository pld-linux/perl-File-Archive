%include	/usr/lib/rpm/macros.perl
Summary:	File-Archive perl module
Summary(pl):	Modu� perla File-Archive
Name:		perl-File-Archive
Version:	0.52
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Archive-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Archive-Tar
BuildRequires:	perl-Compress-Zlib
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
File-Archive - Figure out what is in an archive file.

%description -l pl
File-Archive umo�liwia przegl�danie zawarto�ci archiw�w.

%prep
%setup -q -n File-Archive-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/Archive
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README.txt}.gz

%{perl_sitelib}/File/Archive.pm
%{perl_sitearch}/auto/File/Archive

%{_mandir}/man3/*
