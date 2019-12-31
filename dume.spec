%global commit0 55f6b74ce0eabc05f4478a99e077643e6a03865d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%global qmake_5 /usr/bin/qmake-qt5
%global debug_package %{nil}


Name:		dume
Summary:	Tools and UI for FFmpeg with Qt/C++
License:	GPLv3
URL:		https://github.com/Rainbox-dev/DuME
Version:	0.1.0
Release:	0.1%{dist}
Group:		Applications/Multimedia
Source0:	https://github.com/Rainbox-dev/DuME/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	qt5-devel 
BuildRequires:	OpenImageIO-devel
Requires:	ffmpeg

%description
The Duduf Media Encoder. Rendering and transcoding medias

%prep
%autosetup -n DuME-%{commit0} 

%build
pushd src
%{qmake_5} -makefile DuME.pro

make V=1 %{?_smp_mflags}


%install
pushd src

# App
install -D --mode=644 DuME %{buildroot}/%{_bindir}/DuME

# Icon and desktop file
install -D resources/icons/icon-03.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -D --mode=644 %{S:1} %{buildroot}/usr/share/applications/%{name}.desktop

%files
%{_bindir}/DuME
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog

* Mon Dec 30 2019 David Va <davidva AT tuta DOT io> 0.1.0-1
- Initial build
