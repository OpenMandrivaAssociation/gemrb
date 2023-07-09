%global dont_remove_rpath 1

%define libname %mklibname gemrb_core 0
%define devname	%mklibname -d gemrb_core

%global optflags %{optflags} -pthread

Name:		gemrb
Version:	0.9.2
Release:	1
Summary:	Port of the original Infinity (Game) Engine
Group:		Games/Adventure
License:	GPLv2+
URL:		http://gemrb.sourceforge.net/
Source0:	https://github.com/gemrb/gemrb/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		gemrb-0.9.1-SDL-linkage.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(freetype2)

Requires:	openal

%description
GemRB (Game Engine Made with pre-Rendered Background) is a portable
open-source implementation of Bioware's Infinity Engine.

It was written to support pseudo-3D role playing games based on the
Dungeons & Dragons ruleset (Baldur's Gate and Icewind Dale series,
Planescape: Torment).

This is not a game, but the engine. You need data installed somewhere, and
point gemrb the the relevant directory. More details and a list of
supported games can be found at
http://gemrb.sourceforge.net/wiki/doku.php?id=getting_started

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n	%{libname}
%{summary}

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%autosetup -p1

%build
%cmake -DLAYOUT=fhs -DLIB_DIR='%{_libdir}/gemrb' -DSDL_BACKEND=SDL2 -DOPENGL_BACKEND=OpenGL \
	-DCMAKE_SKIP_RPATH:BOOL=OFF -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF -G Ninja
%ninja_build

%install
%ninja_install -C build

rm -f %{buildroot}/etc/gemrb/GemRB.cfg.noinstall.sample

# remove zero-length files
find %{buildroot} -type f -empty -delete
mv %{buildroot}/etc/gemrb/GemRB.cfg.sample %{buildroot}/etc/gemrb/GemRB.cfg
chmod +x %{buildroot}%{_bindir}/extend2da.py
rm -rf %{buildroot}%{_datadir}/doc/gemrb/en/

%files -n %{libname}
%{_libdir}/gemrb/libgemrb_core.so.*

%files -n %{devname}
%{_libdir}/gemrb/libgemrb_core.so

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md INSTALL
%attr(755,root,root) %{_bindir}/gemrb
%{_libdir}/%{name}/plugins/

%config(noreplace) %{_sysconfdir}/gemrb/GemRB.cfg
%{_mandir}/man6/gemrb.6.*
%{_datadir}/gemrb/*
%{_datadir}/applications/gemrb.desktop
%{_iconsdir}/hicolor/scalable/apps/gemrb.svg
%{_datadir}/pixmaps/gemrb.png
%{_bindir}/extend2da.py
%{_datadir}/metainfo/org.gemrb.gemrb.metainfo.xml
