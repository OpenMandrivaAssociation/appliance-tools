Name:          appliance-tools
Summary:       Tools for building Appliances
Version:       009.0
Release:       1
License:       GPLv2
Group:         System/Base
URL:           https://pagure.io/appliance-tools

Source0:       https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2

# Patches backported from upstream
Patch0001:     0001-fstype-is-optional-for-swap-check-mountpoint-also.patch

BuildArch:     noarch

BuildRequires: python-devel
BuildRequires: %{_bindir}/pod2man
BuildRequires: /bin/sed

# Ensure system deps are installed (rhbz#1409536)
Requires:      python-imgcreate >= 25.0-2
Requires:      python-progress
Requires:      python-future
Requires:      curl rsync kpartx
Requires:      zlib
Requires:      qemu-img
Requires:      xz
Requires:      xfsprogs
Requires:      sssd-client


%description
Tools for generating appliance images on Fedora based systems, including
derived distributions such as RHEL, CentOS, and others.

This package also supports building appliance images on OpenMandriva systems.


%prep
%autosetup -p1

%build
# Nothing to do

%install
%make_install PYTHON=python3 SED_PROGRAM=/bin/sed

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Delete ec2-*, as it needs a lot of work to fix
rm -rf %{buildroot}%{_bindir}/ec2*
rm -rf %{buildroot}%{_mandir}/man*/ec2*
rm -rf %{buildroot}%{python3_sitelib}/ec2convert

%files
%doc README
%doc config/fedora-aos.ks
%license COPYING
%{_mandir}/man*/*
%{_bindir}/appliance-creator
%{python3_sitelib}/appcreate/
