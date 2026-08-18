%global pkgver 0.15.5.1
%global _build_id_links none

Name:           helium-browser-bin
Version:        %{pkgver}
Release:        1%{?dist}
Summary:        Private, fast, and honest web browser (prebuilt binary)
License:        GPL-3.0 AND BSD-3-Clause
URL:            https://github.com/imputnet/helium-linux
Source0:        https://github.com/imputnet/helium-linux/releases/download/0.15.5.1/helium-0.15.5.1-x86_64_linux.tar.xz
Source1:        helium-browser.desktop
Source2:        helium-browser-wrapper

BuildArch:      x86_64
Provides:       helium-browser = %{version}-%{release}
Conflicts:      helium-browser

Requires:       glib2, gtk3, nss, cups-libs, libdrm, mesa-libgbm, at-spi2-core, libxkbcommon-x11

%description
Helium is a fast, private Chromium-based browser. This package repackages
imputnet's official prebuilt Linux tarball rather than building Chromium
from source. See https://github.com/imputnet/helium-linux for upstream
release notes and licensing details.

%global _installdir /opt/helium-browser-bin

%prep
%setup -q -c -n helium

%build
# nothing to build, this is a prebuilt binary tarball

%install
mkdir -p %{buildroot}%{_installdir}
cp -a * %{buildroot}%{_installdir}/

mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/helium-browser

mkdir -p %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/helium-browser.desktop

mkdir -p %{buildroot}%{_datadir}/pixmaps
if [ -f %{buildroot}%{_installdir}/product_logo_256.png ]; then
    install -Dm644 %{buildroot}%{_installdir}/product_logo_256.png \
        %{buildroot}%{_datadir}/pixmaps/helium-browser.png
fi

%files
%{_installdir}
%{_bindir}/helium-browser
%{_datadir}/applications/helium-browser.desktop
%{_datadir}/pixmaps/helium-browser.png

%changelog
* Tue Aug 18 2026 Pancakse <me@pancakse.dev> - 0.15.5.1-1
- Track upstream release
