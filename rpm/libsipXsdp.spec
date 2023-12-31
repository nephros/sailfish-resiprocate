# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       libsipXsdp

# >> macros
# << macros
%define keepstatic 1
%define extraver 20231108
%define sover 2

Summary:    SDP container library
Version:    3.3.0
Release:    0
Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/sipXtapi/sipXtapi
Source0:    sipXtapi-%{version}_%{extraver}.tar.xz
Source100:  libsipXsdp.yaml
Source101:  libsipXsdp-rpmlintrc
Patch0:     0003-pcre-patch.patch
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  libsipXport-devel

%description
%{summary}

%if "%{?vendor}" == "chum"
PackagedBy: nephros
Categories:
 - Library
Custom:
  Repo: %{url}
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
%endif


%package devel
Summary:    Header files and library symbolic links for %{name}
Group:      Development
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n sipXtapi-%{version}_%{extraver}

# 0003-pcre-patch.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
export CFLAGS="${CFLAGS} %{optflags} -fPIC"
export CXXFLAGS="${CXXFLAGS} %{optflags} -fPIC"
export LD_AS_NEEDED=1

pushd sipXsdpLib
autoupdate
%reconfigure \
--prefix=%{_prefix} \
--includedir=%{_includedir}/%{name} \
--disable-shared \
--enable-static \
--without-openssl \
--without-cppunit \
--disable-doxygen

# --with-sipxportinc=
# --with-sipxportlib=
#--with-sipxportinc=%%{_includedir}/libsipXport \
#--with-sipxportlib=%%{_libdir} \


# << build pre



# >> build post

%make_build
popd
find . -name "*.so*"
#ls -l */src/.libs

# << build post

%install
rm -rf %{buildroot}
# >> install pre
pushd sipXsdpLib
make DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot} install
popd
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.la
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}.a
%{_includedir}/%{name}
# >> files devel
# << files devel
