Name:           ros-indigo-catkin-pip
Version:        0.1.12
Release:        0%{?dist}
Summary:        ROS catkin_pip package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/asmodehn/catkin_pip
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel >= 2.7.5
Requires:       python-pip >= 1.5.4
Requires:       ros-indigo-rospack
BuildRequires:  git >= 1.9.1
BuildRequires:  python-devel >= 2.7.5
BuildRequires:  python-pip >= 1.5.4
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospack

%description
Catkin macros to allow using pure python packages in usual catkin workspaces
with normal python workflow.

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
* Sat Aug 27 2016 AlexV <asmodehn@gmail.com> - 0.1.12-0
- Autogenerated by Bloom

* Thu Aug 11 2016 AlexV <asmodehn@gmail.com> - 0.1.11-0
- Autogenerated by Bloom

* Tue Aug 09 2016 AlexV <asmodehn@gmail.com> - 0.1.10-0
- Autogenerated by Bloom

* Fri Jun 24 2016 AlexV <asmodehn@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

* Mon Jun 06 2016 AlexV <asmodehn@gmail.com> - 0.1.8-0
- Autogenerated by Bloom

* Sun Jun 05 2016 AlexV <asmodehn@gmail.com> - 0.1.7-0
- Autogenerated by Bloom

* Sun Jun 05 2016 AlexV <asmodehn@gmail.com> - 0.1.6-0
- Autogenerated by Bloom

* Fri Jun 03 2016 AlexV <asmodehn@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Jun 02 2016 AlexV <asmodehn@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Wed Jun 01 2016 AlexV <asmodehn@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

