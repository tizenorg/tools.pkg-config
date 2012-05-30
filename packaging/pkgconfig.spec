Summary: A tool for determining compilation options
Name: pkgconfig
Version: 0.25
Release: 2.2
License: GPLv2+
URL: http://pkgconfig.freedesktop.org
Group: Development/Tools
Source:  http://www.freedesktop.org/software/pkgconfig/releases/pkg-config-%{version}.tar.gz
Source1001: packaging/pkgconfig.manifest 
#BuildRequires: glib2-devel
BuildRequires: popt-devel

Provides: pkgconfig(pkg-config) = %{version}

%description
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.

%prep
%setup -n %{name}-%{version} -q

%build
cp %{SOURCE1001} .
%configure \
        --disable-shared \
        --with-pc-path=%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pkgconfig

# we include this below, already
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/pkg-config

%remove_docs


%files
%manifest pkgconfig.manifest
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%{_datadir}/aclocal/*
