# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       telepathy-resiprocate

# >> macros
# << macros

Summary:    A SIP connection manager
Version:    1.12.0
Release:    0
Group:      Qt/Qt
License:    ASL 2.0
URL:        https://www.resiprocate.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  telepathy-resiprocate.yaml
Source101:  telepathy-resiprocate-rpmlintrc
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(TelepathyQt5)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  cmake

%description


%if "%{?vendor}" == "chum"
Title: Telepathy Resiprocate
PackagedBy: nephros
Categories:
 - Library
Custom:
  Repo: https://github.com/resiprocate/resiprocate
PackageIcon: https://avatars.githubusercontent.com/u/2827263?s=48&v=4
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake . 
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%license LICENSE.txt
# >> files
# << files