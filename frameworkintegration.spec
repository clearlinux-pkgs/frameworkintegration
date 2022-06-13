#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : frameworkintegration
Version  : 5.95.0
Release  : 49
URL      : https://download.kde.org/stable/frameworks/5.95/frameworkintegration-5.95.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.95/frameworkintegration-5.95.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.95/frameworkintegration-5.95.0.tar.xz.sig
Summary  : Framework providing components to allow applications to integrate with a KDE Workspace
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-3.0
Requires: frameworkintegration-data = %{version}-%{release}
Requires: frameworkintegration-lib = %{version}-%{release}
Requires: frameworkintegration-license = %{version}-%{release}
BuildRequires : appstream-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifications-dev
BuildRequires : kpackage-dev
BuildRequires : kwidgetsaddons-dev

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
Requires: frameworkintegration = %{version}-%{release}

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
%setup -q -n frameworkintegration-5.95.0
cd %{_builddir}/frameworkintegration-5.95.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655153718
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1655153718
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/frameworkintegration
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/frameworkintegration-5.95.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32
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
/usr/include/KF5/FrameworkIntegration/frameworkintegration_version.h
/usr/include/KF5/KStyle/KStyle
/usr/include/KF5/KStyle/kstyle.h
/usr/include/KF5/KStyle/kstyle_export.h
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationConfig.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationConfigVersion.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5FrameworkIntegration/KF5FrameworkIntegrationTargets.cmake
/usr/lib64/libKF5Style.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Style.so.5
/usr/lib64/libKF5Style.so.5.95.0
/usr/lib64/qt5/plugins/kf5/FrameworkIntegrationPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/frameworkintegration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/frameworkintegration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32
