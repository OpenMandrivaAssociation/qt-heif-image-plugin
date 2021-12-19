%define date 20210206

Name: qt-heif-image-plugin
Version: 0.3.4
Release: %{?date:0.%{date}.}2
Source0: https://github.com/jakar/qt-heif-image-plugin/archive/%{?date:master}%{!?date:%{version}}/%{name}-%{version}.tar.gz
Summary: Qt plugin for working with HEIF image files
URL: https://github.com/jakar/qt-heif-image-plugin
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: pkgconfig(libheif) >= 1.1
BuildRequires: qt5-macros
BuildRequires: qmake5

%description
Qt plugin for working with HEIF image files

%prep
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build

%files
%{_libdir}/qt5/plugins/imageformats/libqheif.so
