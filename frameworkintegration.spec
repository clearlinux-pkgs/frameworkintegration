#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : frameworkintegration
Version  : 6.1.0
Release  : 78
URL      : https://download.kde.org/stable/frameworks/6.1/frameworkintegration-6.1.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.1/frameworkintegration-6.1.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.1/frameworkintegration-6.1.0.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
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
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n frameworkintegration-6.1.0
cd %{_builddir}/frameworkintegration-6.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713287566
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713287566
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/frameworkintegration
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/frameworkintegration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kpackagehandlers/knshandler
/usr/lib64/libexec/kf6/kpackagehandlers/knshandler

%files data
%defattr(-,root,root,-)
/usr/share/knotifications6/plasma_workspace.notifyrc

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/FrameworkIntegration/frameworkintegration_version.h
/usr/include/KF6/KStyle/KStyle
/usr/include/KF6/KStyle/kstyle.h
/usr/include/KF6/KStyle/kstyle_export.h
/usr/lib64/cmake/KF6FrameworkIntegration/KF6FrameworkIntegrationConfig.cmake
/usr/lib64/cmake/KF6FrameworkIntegration/KF6FrameworkIntegrationConfigVersion.cmake
/usr/lib64/cmake/KF6FrameworkIntegration/KF6FrameworkIntegrationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6FrameworkIntegration/KF6FrameworkIntegrationTargets.cmake
/usr/lib64/libKF6Style.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Style.so.6.1.0
/V3/usr/lib64/qt6/plugins/kf6/FrameworkIntegrationPlugin.so
/usr/lib64/libKF6Style.so.6
/usr/lib64/libKF6Style.so.6.1.0
/usr/lib64/qt6/plugins/kf6/FrameworkIntegrationPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/frameworkintegration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/frameworkintegration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/frameworkintegration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/frameworkintegration/e458941548e0864907e654fa2e192844ae90fc32
