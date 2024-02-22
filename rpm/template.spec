%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ntrip-client
Version:        1.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ntrip_client package

License:        MIT
URL:            https://github.com/LORD-MicroStrain/ntrip_client
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-nmea-msgs
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rtcm-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-nmea-msgs
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-rtcm-msgs
BuildRequires:  ros-rolling-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
NTRIP client that will publish RTCM corrections to a ROS topic, and optionally
subscribe to NMEA messages to send to an NTRIP server

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Feb 22 2024 Rob Fisher <rob.fisher@parker.com> - 1.3.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Rob Fisher <rob.fisher@parker.com> - 1.2.0-2
- Autogenerated by Bloom

