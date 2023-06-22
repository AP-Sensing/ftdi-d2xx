BuildArch:     noarch
Name:          ftdi-d2xx
Version:       1.4.27
Release:       1
License:       GPLv3
Summary:       RPM for the FTDI D2XX Linux driver.
Distribution:  PhotonPonyOS

URL:           https://github.com/AP-Sensing/ftdi-d2xx/tree/ppos38
Vendor:        AP Sensing
Packager:      AP Sensing
Provides:      ftdi-d2xx = %{version}-%{release}

BuildRequires:  tar
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

ExclusiveArch: x86_64

Source1: libftd2xx-x86_64-%{version}.tgz

%description
This package provides the the FTDI D2XX Linux driver. Based on the driver found here: https://ftdichip.com/drivers/d2xx-drivers/

%prep
cp %{_sourcedir}/libftd2xx-x86_64-%{version}.tgz .
tar zxvf libftd2xx-x86_64-%{version}.tgz

%build

%install
# Binary
install -d -m 755 $RPM_BUILD_ROOT/usr/local/lib/
install -m 644 release/build/libftd2xx.so.%{version} $RPM_BUILD_ROOT/usr/local/lib/

pushd $RPM_BUILD_ROOT/usr/local/lib/
ln -s libftd2xx.so.%{version} libftd2xx.so
popd

# Header
install -d -m 755 $RPM_BUILD_ROOT/usr/local/include
install -m 644 release/ftd2xx.h $RPM_BUILD_ROOT/usr/local/include
install -m 644 release/WinTypes.h $RPM_BUILD_ROOT/usr/local/include

# Call ldconfig (https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_snippets)
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr(0644, root, root) /usr/local/lib/libftd2xx.so.%{version}
%attr(0644, root, root) /usr/local/include/ftd2xx.h
%attr(0644, root, root) /usr/local/include/WinTypes.h
/usr/local/lib/libftd2xx.so

%changelog
* Thu Jun 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.4.27-1
- Initial release