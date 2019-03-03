%define libname %mklibname gemrb_core 0
%define devname	%mklibname -d gemrb_core

Name:		gemrb
Version:	0.8.5
Release:	2
Summary:	Port of the original Infinity (Game) Engine
Group:		Games/Adventure
License:	GPLv2+
URL:		http://gemrb.sourceforge.net/
Source0:	https://github.com/gemrb/gemrb/archive/v%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(python2)
BuildRequires:  pkgconfig(libvlc)
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
%setup -q

%build
%cmake -DLAYOUT=fhs -DLIB_DIR='%{_libdir}/gemrb' -DSDL_BACKEND=SDL2 -DOPENGL_BACKEND=OpenGL
%make_build

%install
%make_install -C build

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
%doc AUTHORS COPYING NEWS README INSTALL
%attr(755,root,root) %{_bindir}/gemrb
%attr(755,root,root) %{_libdir}/gemrb/plugins/NullSource.so
#attr(755,root,root) %{_libdir}/gemrb/plugins/TTFImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/2DAImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/ACMReader.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/AREImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/BAMImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/BIFImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/BIKPlayer.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/BMPImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/BMPWriter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/CHUImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/CREImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/DirectoryImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/DLGImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/EFFImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/FXOpcodes.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/GAMImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/GUIScript.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/IDSImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/INIImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/ITMImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/IWDOpcodes.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/KEYImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/MOSImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/MUSImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/MVEPlayer.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/NullSound.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/OGGReader.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/OpenALAudio.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/PLTImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/PNGImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/PROImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/PSTOpcodes.so
#attr(755,root,root) %{_libdir}/gemrb/plugins/SDLAudio.so
#attr(755,root,root) %{_libdir}/gemrb/plugins/SDLVideo.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/SPLImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/STOImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/TISImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/TLKImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WAVReader.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WEDImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WMPImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/ZLibManager.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/SAVImporter.so

%config(noreplace) %{_sysconfdir}/gemrb/GemRB.cfg
%{_mandir}/man6/gemrb.6.*
%{_datadir}/gemrb/*
%{_datadir}/applications/gemrb.desktop
%{_iconsdir}/hicolor/scalable/apps/gemrb.svg
%{_datadir}/pixmaps/gemrb.png
%{_bindir}/extend2da.py
