Name:           nvidia-vaapi-driver
Version:        0.0.6
Release:        10%{?dist}
Summary:        VA-API implementation that uses NVDEC as a backend

License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Nvidia driver is only available on theses arches
ExclusiveArch:  x86_64 i686 aarch64 ppc64le

BuildRequires:  libva-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)

Requires: mesa-filesystem%{?_isa}

# The nvidia_drv_video.so symlink is also provided by theses packages
Conflicts: libva-vdpau-driver%{?_isa}
Conflicts: libva-vdpau-driver-vp9%{?_isa}
# Alternative name that better describes the API involved
Provides: nvdec-vaapi-driver = %{version}-%{release}


Requires: (xorg-x11-drv-nvidia-cuda-libs%{_isa} or xorg-x11-drv-nvidia-470xx-cuda-libs%{_isa})

%description
This is a VA-API implementation that uses NVDEC as a backend.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_libdir}/dri/nvidia_drv_video.so


%changelog
* Mon May 30 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.6-10
- Update to 0.0.6

* Sat Feb 12 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.5-1
- Initial spec file
