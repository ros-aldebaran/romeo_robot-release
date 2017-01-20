Name:           ros-indigo-romeo-description
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS romeo_description package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/romeo_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
The romeo_description package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jan 20 2017 Surya Ambrose <surya.ambrose@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Sun Feb 14 2016 mikael arguedas <mikael.arguedas@gmail.com> - 0.1.3-1
- Autogenerated by Bloom

* Sun Dec 20 2015 mikael arguedas <mikael.arguedas@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

* Wed Oct 21 2015 mikael arguedas <mikael.arguedas@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Oct 21 2015 mikael arguedas <mikael.arguedas@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Thu Oct 08 2015 mikael arguedas <mikael.arguedas@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

