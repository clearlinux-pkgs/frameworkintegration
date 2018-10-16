#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : frameworkintegration
Version  : 5.51.0
Release  : 4
URL      : https://download.kde.org/stable/frameworks/5.51/frameworkintegration-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/frameworkintegration-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/frameworkintegration-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: frameworkintegration-data = %{version}-%{release}
Requires: frameworkintegration-lib = %{version}-%{release}
Requires: frameworkintegration-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : qtbase-dev mesa-dev

%description
# Framework Integration
Integration of Qt application with KDE workspaces
## Introduction

%package data
Summary: data components for the frameworkintegration package.
Group: Data

%description data
data components for the frameworkintegration package.


%package dev
Summary: dev components for the frameworkintegration package.
Group: Development
Requires: frameworkintegration-lib = %{version}-%{release}
Requires: frameworkintegration-data = %{version}-%{release}
Provides: frameworkintegration-devel = %{version}-%{release}

%description dev
dev components for the frameworkintegration package.


%package lib
Summary: lib components for the frameworkintegration package.
Group: Libraries
Requires: frameworkintegration-data = %{version}-%{release}
Requires: frameworkintegration-license = %{version}-%{release}

%description lib
lib components for the frameworkintegration package.


%package license
Summary: license components for the frameworkintegration package.
Group: Default

%description license
license components for the frameworkintegration package.


%prep
%setup -q -n frameworkintegration-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539648392
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539648392
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/frameworkintegration
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/frameworkintegration/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/frameworkintegration/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kpackagehandlers/knshandler

%files data
%defattr(-,root,root,-)
/usr/share/kf5/infopage/bar-bottom-left.png
/usr/share/kf5/infopage/bar-bottom-middle.png
/usr/share/kf5/infopage/bar-bottom-right.png
/usr/share/kf5/infopage/bar-middle-left.png
/usr/share/kf5/infopage/bar-middle-right.png
/usr/share/kf5/infopage/bar-top-left.png
/usr/share/kf5/infopage/bar-top-middle.png
/usr/share/kf5/infopage/bar-top-right.png
/usr/share/kf5/infopage/body-background.png
/usr/share/kf5/infopage/box-bottom-left.png
/usr/share/kf5/infopage/box-bottom-middle.png
/usr/share/kf5/infopage/box-bottom-right.png
/usr/share/kf5/infopage/box-center.png
/usr/share/kf5/infopage/box-middle-left.png
/usr/share/kf5/infopage/box-middle-right.png
/usr/share/kf5/infopage/box-top-left.png
/usr/share/kf5/infopage/box-top-middle.png
/usr/share/kf5/infopage/box-top-right.png
/usr/share/kf5/infopage/kde_infopage.css
/usr/share/kf5/infopage/kde_infopage_rtl.css
/usr/share/kf5/infopage/top-middle.png
/usr/share/knotifications5/plasma_workspace.notifyrc

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KStyle/KStyle
/usr/include/KF5/KStyle/kstyle.h
/usr/include/KF5/KStyle/kstyle_export.h
/usr/include/KF5/frameworkintegration_version.h
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationConfig.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationConfigVersion.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationTargets.cmake
/usr/lib64/libKF5Style.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Style.so.5
/usr/lib64/libKF5Style.so.5.51.0
/usr/lib64/qt5/plugins/kf5/FrameworkIntegrationPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/frameworkintegration/COPYING.LGPL-2
/usr/share/package-licenses/frameworkintegration/COPYING.LIB
