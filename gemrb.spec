Name:		gemrb
Version:	0.7.2
Release:	1
Summary:	Port of the original Infinity (Game) Engine
Group:		Games/Adventure
License:	GPLv2+
URL:		http://gemrb.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/gemrb/GemRB%20Sources/GemRB%200.7.0%20Sources/%{name}-%{version}.tar.gz
Patch0:		gemrb-0.7.0-linkage.patch
BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	python-devel
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

%prep
%setup -q
#% patch0 -p0

%build
%cmake -DLAYOUT=fhs -DLIB_DIR='%{_libdir}/gemrb'
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}/etc/gemrb/GemRB.cfg.noinstall.sample

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README INSTALL
%attr(755,root,root) %{_bindir}/gemrb
%attr(755,root,root) %{_libdir}/gemrb/libgemrb_core.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/NullSource.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/TTFImporter.so
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
%attr(755,root,root) %{_libdir}/gemrb/plugins/SDLAudio.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/SDLVideo.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/SPLImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/STOImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/TISImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/TLKImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WAVReader.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WEDImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/WMPImporter.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/ZLibManager.so
%attr(755,root,root) %{_libdir}/gemrb/plugins/SAVImporter.so

%{_sysconfdir}/gemrb/GemRB.cfg.sample
%{_mandir}/man6/gemrb.6.*
%{_datadir}/gemrb/*
%{_datadir}/applications/gemrb.desktop
%{_iconsdir}/hicolor/scalable/apps/gemrb.svg
%{_datadir}/pixmaps/gemrb.png
%{_bindir}/extend2da.py
