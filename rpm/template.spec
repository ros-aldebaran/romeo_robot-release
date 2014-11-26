Name:           ros-indigo-romeo-dcm-msgs
Version:        0.0.12
Release:        1%{?dist}
Summary:        ROS romeo_dcm_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Message, service and action declarations for Aldebaran's ROMEO

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 26 2014 Ha Dang <hris2003@gmail.com> - 0.0.12-1
- Autogenerated by Bloom

* Wed Nov 26 2014 Ha Dang <hris2003@gmail.com> - 0.0.11-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Ha Dang <hris2003@gmail.com> - 0.0.10-0
- Autogenerated by Bloom

* Thu Sep 25 2014 Ha Dang <hris2003@gmail.com> - 0.0.9-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Ha Dang <hris2003@gmail.com> - 0.0.8-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Ha Dang <hris2003@gmail.com> - 0.0.7-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Ha Dang <hris2003@gmail.com> - 0.0.6-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Ha Dang <hris2003@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Thu Sep 11 2014 Ha Dang <hris2003@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Ha Dang <hris2003@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Ha Dang <hris2003@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Ha Dang <hris2003@gmail.com> - 0.0.1-1
- Autogenerated by Bloom

* Tue Sep 09 2014 Ha Dang <hris2003@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

