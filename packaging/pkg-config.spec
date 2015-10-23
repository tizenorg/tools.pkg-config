Summary: A tool for determining compilation options
Name: pkg-config
Version: 0.25
Release: %{?release_prefix:%{release_prefix}.}2.47.%{?dist}%{!?dist:tizen}
VCS:     external/pkg-config#Z910F_PROTEX_0625-2-g4d73d1879925f70f08441274250fa42f6c9ae71e
License: GPLv2+
URL: http://pkgconfig.freedesktop.org
Group: Development/Tools
Source:  http://www.freedesktop.org/software/pkgconfig/releases/pkg-config-%{version}.tar.gz
Patch1:  pkg-config-system_libdir-multilib.patch
#BuildRequires: glib2-devel
BuildRequires: popt-devel

Provides: pkgconfig
Provides: pkgconfig(pkg-config) = %{version}

%description
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.

%prep
%setup -n pkg-config-%{version} -q
%patch1 -p1

%build
%configure \
        --disable-shared \
%ifarch x86_64
        --with-pc-path=%{_prefix}/lib/pkgconfig:%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
%else
        --with-pc-path=%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
%ifarch x86_64
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig
%endif
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pkgconfig

# we include this below, already
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/pkg-config

%remove_docs

mkdir -p %{buildroot}/usr/share/license
cp -f COPYING %{buildroot}/usr/share/license/%{name}

%files
%defattr(-,root,root)
%{_bindir}/*
%ifarch x86_64
%dir %{_prefix}/lib/pkgconfig
%endif
%dir %{_libdir}/pkgconfig
%dir %{_datadir}/pkgconfig
%{_datadir}/aclocal/*
/usr/share/license/%{name}
%manifest pkg-config.manifest
%changelog
* Sat Jun 28 2014 SLP SCM <slpsystem.m@samsung.com> - None 
- PROJECT: external/pkg-config
- COMMIT_ID: 4d73d1879925f70f08441274250fa42f6c9ae71e
- BRANCH: master
- PATCHSET_REVISION: 4d73d1879925f70f08441274250fa42f6c9ae71e
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/534231
- PATCHSET_REVISION: 4d73d1879925f70f08441274250fa42f6c9ae71e
- TAGGER: SLP SCM <slpsystem.m@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code-Review : 2
- Newton Lee <newton.lee@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merged x86_64 support to master
- Merged x86_64 support to master
* Wed Dec 18 2013 .kim@samsung.com> - None 
- PROJECT: external/pkg-config
- COMMIT_ID: 256d8e8aacaf8ef9c8fa2df7e4a09334d6616c10
- PATCHSET_REVISION: 256d8e8aacaf8ef9c8fa2df7e4a09334d6616c10
- CHANGE_OWNER: \"Kim Kibum\" <kb0929.kim@samsung.com>
- PATCHSET_UPLOADER: \"Kim Kibum\" <kb0929.kim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/372718
- PATCHSET_REVISION: 256d8e8aacaf8ef9c8fa2df7e4a09334d6616c10
- TAGGER: Kim Kibum <kb0929.kim@samsung.com>
- Gerrit patchset approval info:
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- Kim Kibum <kb0929.kim@samsung.com> Verified : 1
- CHANGE_SUBJECT: install license file
- install license file
* Wed Nov 27 2013 .kim@samsung.com> - None 
- PROJECT: external/pkg-config
- COMMIT_ID: 2dee0f8d1d9f87ebcd6d7a9728e9fd9abea879d0
- PATCHSET_REVISION: 2dee0f8d1d9f87ebcd6d7a9728e9fd9abea879d0
- CHANGE_OWNER: \"Kidong Kim\" <kd0228.kim@samsung.com>
- PATCHSET_UPLOADER: \"Kidong Kim\" <kd0228.kim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/349082
- PATCHSET_REVISION: 2dee0f8d1d9f87ebcd6d7a9728e9fd9abea879d0
- TAGGER: Kidong Kim <kd0228.kim@samsung.com>
- Gerrit patchset approval info:
- Bumjin Im <bj.im@samsung.com> Code Review : 2
- Bumjin Im <bj.im@samsung.com> Verified : 1
- CHANGE_SUBJECT: [model] REDWOOD [binary_type] PDA [customer] OPEN [issue#] N/A [problem] N/A [cause] N/A [solution] remove execute label of executable [team] security [request] N/A [horizontal_expansion] N/A
- [model] REDWOOD [binary_type] PDA [customer] OPEN [issue#] N/A [problem] N/A [cause] N/A [solution] remove execute label of executable [team] security [request] N/A [horizontal_expansion] N/A
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121022.075003 
- PROJECT: external/pkg-config
- COMMIT_ID: c28b26ae7c7d4601e9ee670f3c1e999bd8862fad
- PATCHSET_REVISION: c28b26ae7c7d4601e9ee670f3c1e999bd8862fad
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103938
- PATCHSET_REVISION: c28b26ae7c7d4601e9ee670f3c1e999bd8862fad
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Git OBS Sync
- [Version] 0.25
- [Project] GT-I8800
- [Title] Git OBS Sync
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
