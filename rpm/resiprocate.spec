# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       resiprocate

# >> macros
# << macros

Summary:    A SIP connection manager
Version:    1.12.0
Release:    0
Group:      Applications
License:    ASL 2.0
URL:        https://www.resiprocate.org/
Source0:    %{name}-%{version}.tar.gz
Source100:  resiprocate.yaml
Source101:  resiprocate-rpmlintrc
Patch0:     01-srtp2.patch
Patch1:     11-resip-stack-bring-OpenSigComp-specific-code-up-to-date.patch
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(TelepathyQt5)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig
BuildRequires:  python3-pycxx-devel
BuildRequires:  boost-devel
BuildRequires:  asio-devel
BuildRequires:  opensigcomp-devel
BuildRequires:  radcli-devel
BuildRequires:  libsipXport-devel
BuildRequires:  libsipXmedia-devel
BuildRequires:  libsipXmediaAdapter-devel
BuildRequires:  libsipXsdp-devel
BuildRequires:  libsipXtack-devel
BuildRequires:  vim-common

%description
%{summary}.

%if "%{?vendor}" == "chum"
Title: Resiprocate
PackagedBy: nephros
Categories:
 - Library
Custom:
  Repo: https://github.com/resiprocate/resiprocate
PackageIcon: https://avatars.githubusercontent.com/u/2827263?s=48&v=4
%endif


%package -n %{name}-libs
Summary:    Libraries for %{name}
Group:      Libraries

%description -n %{name}-libs
%{summary}.

%package -n telepathy-%{name}
Summary:    a connection manager for the Telepathy framework
Group:      Applications
Requires(pre): systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd

%description -n telepathy-%{name}
%{summary}

It uses the TelepathyQt API to interact with DBus.

It uses the high level reCon API from reSIProcate to co-ordinate
SIP and media streams.  reCon also supports conferencing.
The media stack from the sipXtapi project is used.


%prep
%setup -q -n %{name}-%{name}-%{version}

# 01-srtp2.patch
%patch0 -p1
# 11-resip-stack-bring-OpenSigComp-specific-code-up-to-date.patch
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
sed -i "s/PKG_CHECK_MODULES(\[DEPS_PYTHON\], \[python >= 3.6\])/PKG_CHECK_MODULES(\[DEPS_PYTHON\], \[python3 >= 3.6\])/" configure.ac
sed -i "s/QT_SELECT=qt5/QT_SELECT=5/" apps/telepathy/Makefile.*
CFLAGS="${CFLAGS} %{optflags}"
CXXFLAGS="${CXXFLAGS} %{optflags}"
#CFLAGS="$CFLAGS -fPIC"
#LDFLAGS="$LDFLAGS -pie -shared"
CFLAGS="${CFLAGS} -I%{_includedir}/libsipXport"
CXXFLAGS="${CXXFLAGS} -I%{_includedir}/libsipXport"
CFLAGS="${CFLAGS} -I%{_includedir}/libsipXmedia"
CXXFLAGS="${CXXFLAGS} -I%{_includedir}/libsipXmedia"
CFLAGS="${CFLAGS} -I%{_includedir}/libsipXmediaAdapter"
CXXFLAGS="${CXXFLAGS} -I%{_includedir}/libsipXmediaAdapter"
CFLAGS="${CFLAGS} -I%{_includedir}/libsipXsdp"
CXXFLAGS="${CXXFLAGS} -I%{_includedir}/libsipXsdp"
CFLAGS="${CFLAGS} -I%{_includedir}/libsipXtack"
CXXFLAGS="${CXXFLAGS} -I%{_includedir}/libsipXtack"
#CFLAGS="${CFLAGS} -I/usr/include/boost"
#CXXFLAGS="${CXXFLAGS} -I/usr/include/boost"
CFLAGS="${CFLAGS} -I/usr/include/radcli"
CXXFLAGS="${CXXFLAGS} -I/usr/include/radcli"
CFLAGS="${CFLAGS} -I/usr/include/opensigcomp"
CXXFLAGS="${CXXFLAGS} -I/usr/include/opensigcomp"

# avoid using the working sipXmedia API, gives compile error otherwise
CPPFLAGS="$CPPFLAGS -DSIPX_TONES_INBAND"


CXXFLAGS="${CXXFLAGS} -Wno-strict-aliasing"

# from debian:
export QT_SELECT=5
CXXFLAGS="${CXXFLAGS} -fpermissive"
CPPFLAGS="$CPPFLAGS -D__pingtel_on_posix__ -D_linux_ -D_REENTRANT -D_FILE_OFFS"
CPPFLAGS="$CPPFLAGS -DDEFAULT_BRIDGE_MAX_IN_OUTPUTS=20"
CPPFLAGS="$CPPFLAGS -D__STDC_LIMIT_MACROS -D__STDC_CONSTANT_MACROS -D__STDC_FORMAT_MACROS"
CPPFLAGS="$CPPFLAGS -DRECON_SDP_ENCODING_NAMES_CASE_HACK"
CPPFLAGS="$CPPFLAGS -L%{_libdir}/qt5"
CPPFLAGS="$CPPFLAGS -I/usr/include/telepathy-qt5"
export CPPFLAGS
autoupdate
# << build pre

%reconfigure --disable-static \
    PKG_CONFIG_PATH="%{_libdir}/pkgconfig:${_prefix}/lib/pkgconfig:%{_datadir}/pkgconfig" \
    PYCXX_SRCDIR="%{_datadir}/python%{python3_version}/CXX" \
    --enable-static \
    --disable-pedantic-stack \
    --disable-assert-syslog \
    --disable-repro-plugins \
    --enable-ipv6 \
    --with-popt \
    --with-ssl \
    --with-telepathy \
    --without-c-ares \
    --without-apps \
    --without-geoip \
    --without-ichat-gw \
    --without-mysql \
    --without-netsnmp \
    --without-p2p \
    --without-postgresql \
    --without-python \
    --with-radcli \
    --without-radius \
    --without-recon \
    --without-rend \
    --without-repro \
    --with-sigcomp \
    --without-tfm


# >> build post
make -C rutil librutil.la
make -C resip/stack libresip.la
make -C resip/dum libdum.la
make -C reTurn libreTurnCommon.la
make -C reTurn/client libreTurnClient.la
make -C reflow libreflow.la
make -C resip/recon librecon.la
#make -C reflow %%{?_smp_mflags}
make -C apps/telepathy
# << build post

%install
rm -rf %{buildroot}
# >> install pre
make DESTDIR=%{buildroot} -C apps/telepathy install

install -d %{buildroot}%{_datadir}/telepathy/managers
install -m644 apps/telepathy/resiprocate.manager %{buildroot}%{_datadir}/telepathy/managers

# work around the fact that libtool doesn't install sometimes
#install -m 755 reTurn/client/libreTurnClient.la %%{buildroot}%%{_libdir}/
#install -m 755 reTurn/libreTurnCommon.la %%{buildroot}%%{_libdir}/
#install -m 755 reflow/libreflow.la %%{buildroot}%%{_libdir}/
#install -m 755 resip/dum/libdum.la %%{buildroot}%%{_libdir}/
#install -m 755 resip/recon/librecon.la %%{buildroot}%%{_libdir}/
#install -m 755 resip/stack/libresip.la %%{buildroot}%%{_libdir}/
#install -m 755 rutil/librutil.la %%{buildroot}%%{_libdir}/
# << install pre

# >> install post
sed -i "/^Exec/d" %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.resiprocate.service
echo "Exec=%{_bindir}/telepathy-resiprocate" >> %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.resiprocate.service
# << install post


%files -n %{name}-libs
%defattr(-,root,root,-)
# >> files %{name}-libs
# << files %{name}-libs

%files -n telepathy-%{name}
%defattr(-,root,root,-)
%license apps/telepathy/LICENSE.txt
%{_bindir}/telepathy-resiprocate
%{_datadir}/dbus-1/services/*
%{_datadir}/telepathy/managers/resiprocate.manager
# >> files telepathy-%{name}
# << files telepathy-%{name}
