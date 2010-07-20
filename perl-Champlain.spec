%define upstream_name    Champlain
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Map rendering canvas
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Clutter)
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: libchamplain-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Champlain consists of the Perl bindings for the C library libchamplain
which provides a canvas widget based on the Clutter manpage that displays
maps from various free map sources such as _OpenStreetMap_, _OpenAerialMap_
and _Maps for free_.

For more information about libchamplain see: the
http://projects.gnome.org/libchamplain/ manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
#gw this fails on a display without GL support
#%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


