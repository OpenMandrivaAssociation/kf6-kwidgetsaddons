%define libname %mklibname KF6WidgetsAddons
%define devname %mklibname KF6WidgetsAddons -d
%define git 20230605

Name: kf6-kwidgetsaddons
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kwidgetsaddons/-/archive/master/kwidgetsaddons-master.tar.bz2#/kwidgetsaddons-%{git}.tar.bz2
Summary: Large set of desktop widgets
URL: https://invent.kde.org/frameworks/kwidgetsaddons
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
Large set of desktop widgets

%package -n %{libname}
Summary: Large set of desktop widgets
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Large set of desktop widgets

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Large set of desktop widgets

%prep
%autosetup -p1 -n kwidgetsaddons-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kwidgetsaddons.*
%{_datadir}/kf6/kcharselect

%files -n %{devname}
%{_includedir}/KF6/KWidgetsAddons
%{_libdir}/cmake/KF6WidgetsAddons
%{_qtdir}/mkspecs/modules/qt_KWidgetsAddons.pri
%{_qtdir}/doc/KF6WidgetsAddons.*

%files -n %{libname}
%{_libdir}/libKF6WidgetsAddons.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kwidgetsaddons6widgets.so
