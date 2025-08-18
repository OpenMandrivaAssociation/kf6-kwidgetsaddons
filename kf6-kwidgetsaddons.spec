%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6WidgetsAddons
%define devname %mklibname KF6WidgetsAddons -d
#define git 20240217

Name: kf6-kwidgetsaddons
Version: 6.17.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kwidgetsaddons/-/archive/master/kwidgetsaddons-master.tar.bz2#/kwidgetsaddons-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kwidgetsaddons-%{version}.tar.xz
%endif
Summary: Large set of desktop widgets
URL: https://invent.kde.org/frameworks/kwidgetsaddons
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: python%{pyver}dist(build)
BuildRequires: pkgconfig(python3)
BuildRequires: cmake(Shiboken6)
BuildRequires: cmake(PySide6)
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
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBUILD_QCH:BOOL=ON

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

%package -n python-kwidgetsaddons
Summary: Python bindings to KWidgetsAddons
Group: Development/Python
Requires: %{libname} = %{EVRD}

%description -n python-kwidgetsaddons
Python bindings to KWidgetsAddons

%install -a
%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kwidgetsaddons.*

%files -n %{devname}
%{_includedir}/KF6/KWidgetsAddons
%{_libdir}/cmake/KF6WidgetsAddons

%files -n %{libname}
%{_libdir}/libKF6WidgetsAddons.so*

%files -n python-kwidgetsaddons
%{_libdir}/python*/site-packages/KWidgetsAddons.cpython-*.so

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kwidgetsaddons6widgets.so
