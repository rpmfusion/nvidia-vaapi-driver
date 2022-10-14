Name:           nvidia-vaapi-driver
Version:        0.0.7
Release:        1%{?dist}
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

# We will use Recommends instead
#Requires: (xorg-x11-drv-nvidia-cuda-libs%%{_isa} or xorg-x11-drv-nvidia-470xx-cuda-libs%%{_isa})

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
* Fri Oct 14 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Jun 22 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.6-11
- Switch to Recommends

* Mon May 30 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.6-10
- Update to 0.0.6

* Sat Feb 12 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.0.5-1
- Initial spec file
