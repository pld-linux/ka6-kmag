#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmag
Summary:	kmag
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1e07b0d361b8e6b678f172b539b87dff
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMag is a small utility for Linux to magnify a part of the screen.
KMag is very useful for people with visual disabilities and for those
working in the fields of image analysis, web development etc.

%description -l pl.UTF-8
KMag jest małym programem użytkowym dla Linuksa powiekszającym część
ekranu. KMag jest bardzo przydatny dla osób niedowidzących jak i dla
pracujących na polu analizy obrazu, programowaniu webowym, itp.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/ko

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_desktopdir}/org.kde.kmag.desktop
%{_iconsdir}/hicolor/*x*/apps/kmag.png
%{_iconsdir}/hicolor/scalable/apps/kmag.svg
%{_datadir}/kmag
%lang(ca) %{_mandir}/ca/man1/kmag.1*
%lang(de) %{_mandir}/de/man1/kmag.1*
%lang(es) %{_mandir}/es/man1/kmag.1*
%lang(et) %{_mandir}/et/man1/kmag.1*
%lang(fr) %{_mandir}/fr/man1/kmag.1*
%lang(it) %{_mandir}/it/man1/kmag.1*
%lang(C) %{_mandir}/man1/kmag.1*
%lang(nl) %{_mandir}/nl/man1/kmag.1*
%lang(pt) %{_mandir}/pt/man1/kmag.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmag.1*
%lang(ru) %{_mandir}/ru/man1/kmag.1*
%lang(sl) %{_mandir}/sl/man1/kmag.1*
%lang(sv) %{_mandir}/sv/man1/kmag.1*
%lang(uk) %{_mandir}/uk/man1/kmag.1*
%{_datadir}/metainfo/org.kde.kmag.metainfo.xml
