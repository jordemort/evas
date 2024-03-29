# Conditional build stuff; from rpm 4.4 /usr/lib/rpm/macros.
# bcond_without defaults to WITH, and vice versa.  Yes, it's
# ass-backward.  Blame PLD.
%if %{!?with:1}0
%define with() %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%endif
%if %{!?without:1}0
%define without() %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%endif
%if %{!?bcond_with:1}0
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%endif
%if %{!?bcond_without:1}0
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%endif

## disabled features
%bcond_with    module_loader_edb
%bcond_with    module_saver_edb
%bcond_with    module_engine_directfb
%bcond_with    module_engine_gl_x11
%bcond_with    module_engine_software_16_x11
%bcond_with    module_engine_software_sdl
%bcond_with    module_engine_software_xcb
%bcond_with    module_loader_gif
%bcond_with    module_loader_svg

## enabled features
%bcond_without module_engine_software_x11
%bcond_without module_engine_buffer
%bcond_without module_engine_fb
%bcond_without module_loader_pmaps
%bcond_without module_loader_png
%bcond_without module_saver_png
%bcond_without module_loader_jpeg
%bcond_without module_saver_jpeg
%bcond_without module_loader_tiff
%bcond_without module_saver_tiff
%bcond_without module_loader_eet
%bcond_without module_saver_eet
%bcond_without module_loader_xpm
%bcond_without module_loader_bmp
%bcond_without module_loader_wbmp
%bcond_without module_loader_tga
%bcond_without module_loader_ico
%bcond_without module_loader_psd
%bcond_without module_loader_generic

# This just keeps a missing doxygen from killing the build.
%define _missing_doc_files_terminate_build 0

# Macros for ./configure use
%define ac_with_module_loader_eet --%{?with_module_loader_eet:en}%{!?with_module_loader_eet:dis}able-image-loader-eet
%define ac_with_module_loader_jpeg --%{?with_module_loader_jpeg:en}%{!?with_module_loader_jpeg:dis}able-image-loader-jpeg
%define ac_with_module_loader_pmaps --%{?with_module_loader_pmaps:en}%{!?with_module_loader_pmaps:dis}able-image-loader-pmaps
%define ac_with_module_loader_png --%{?with_module_loader_png:en}%{!?with_module_loader_png:dis}able-image-loader-png
%define ac_with_module_loader_tiff --%{?with_module_loader_tiff:en}%{!?with_module_loader_tiff:dis}able-image-loader-tiff
%define ac_with_module_loader_gif --%{?with_module_loader_gif:en}%{!?with_module_loader_gif:dis}able-image-loader-gif
%define ac_with_module_loader_edb --%{?with_module_loader_edb:en}%{!?with_module_loader_edb:dis}able-image-loader-edb
%define ac_with_module_loader_xpm --%{?with_module_loader_xpm:en}%{!?with_module_loader_xpm:dis}able-image-loader-xpm
%define ac_with_module_loader_svg --%{?with_module_loader_svg:en}%{!?with_module_loader_svg:dis}able-image-loader-svg
%define ac_with_module_loader_bmp --%{?with_module_loader_bmp:en}%{!?with_module_loader_bmp:dis}able-image-loader-bmp
%define ac_with_module_loader_wbmp --%{?with_module_loader_wbmp:en}%{!?with_module_loader_wbmp:dis}able-image-loader-wbmp
%define ac_with_module_loader_tga --%{?with_module_loader_tga:en}%{!?with_module_loader_tga:dis}able-image-loader-tga
%define ac_with_module_loader_ico --%{?with_module_loader_ico:en}%{!?with_module_loader_ico:dis}able-image-loader-ico
%define ac_with_module_loader_psd --%{?with_module_loader_psd:en}%{!?with_module_loader_psd:dis}able-image-loader-psd
%define ac_with_module_loader_generic --%{?with_module_loader_generic:en}%{!?with_module_loader_generic:dis}able-image-loader-generic
%define ac_with_module_saver_eet --%{?with_module_saver_eet:en}%{!?with_module_saver_eet:dis}able-image-saver-eet
%define ac_with_module_saver_jpeg --%{?with_module_saver_jpeg:en}%{!?with_module_saver_jpeg:dis}able-image-saver-jpeg
%define ac_with_module_saver_png --%{?with_module_saver_png:en}%{!?with_module_saver_png:dis}able-image-saver-png
%define ac_with_module_saver_tiff --%{?with_module_saver_tiff:en}%{!?with_module_saver_tiff:dis}able-image-saver-tiff
%define ac_with_module_saver_gif --%{?with_module_saver_gif:en}%{!?with_module_saver_gif:dis}able-image-saver-gif
%define ac_with_module_saver_edb --%{?with_module_saver_edb:en}%{!?with_module_saver_edb:dis}able-image-saver-edb
%define ac_with_module_saver_xpm --%{?with_module_saver_xpm:en}%{!?with_module_saver_xpm:dis}able-image-saver-xpm
%define ac_with_module_engine_software-x11 --%{?with_module_engine_software_x11:en}%{!?with_module_engine_software_x11:dis}able-software-x11
%define ac_with_module_engine_buffer --%{?with_module_engine_buffer:en}%{!?with_module_engine_buffer:dis}able-buffer
%define ac_with_module_engine_fb --%{?with_module_engine_fb:en}%{!?with_module_engine_fb:dis}able-fb
%define ac_with_module_engine_gl_x11 --%{?with_module_engine_gl_x11:en}%{!?with_module_engine_gl_x11:dis}able-gl-x11
%define ac_with_module_engine_directfb --%{?with_module_engine_directfb:en}%{!?with_module_engine_directfb:dis}able-directfb
%define ac_with_module_engine_software_16_x11 --%{?with_module_engine_software_16_x11:en}%{!?with_module_engine_software_16_x11:dis}able-software-16-x11
%define ac_with_module_engine_software_sdl --%{?with_module_engine_software_sdl:en}%{!?with_module_engine_software_sdl:dis}able-sdl
%define ac_with_module_engine_software_xcb --%{?with_module_engine_software_xcb:en}%{!?with_module_engine_software_xcb:dis}able-software-xcb

%{!?_rel:%{expand:%%global _rel 0.enl%{?dist}}}

Summary: Multi-platform Canvas Library
Name: evas
Version: 1.7.7
Release: %{_rel}
License: BSD
Group: System Environment/Libraries
URL: http://www.enlightenment.org/
Source: http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
Packager: %{?_packager:%{_packager}}%{!?_packager:Michael Jennings <mej@eterm.org>}
Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:The Enlightenment Project (http://www.enlightenment.org/)}
Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
BuildRequires: /usr/bin/freetype-config
Provides: evas
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%package devel
Summary: Evas headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for Evas.

%if %{with module_loader_eet}
%package module_loader_eet
Summary: EET Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: eet-devel
%description module_loader_eet
EET Image loader module for Evas
%endif

%if %{with module_saver_eet}
%package module_saver_eet
Summary: EET Image saver module for Evas
Group: System Environment/Libraries
BuildRequires: eet-devel
%description module_saver_eet
EET Image saver module for Evas
%endif

%if %{with module_loader_jpeg}
%package module_loader_jpeg
Summary: JPEG Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_jpeg
JPEG Image loader module for Evas
%endif

%if %{with module_saver_jpeg}
%package module_saver_jpeg
Summary: JPEG Image saver module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_saver_jpeg
JPEG Image saver module for Evas
%endif

%if %{with module_loader_pmaps}
%package module_loader_pmaps
Summary: Pixmap Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libXpm-devel
%description module_loader_pmaps
Pixmap Image loader module for Evas
%endif

%if %{with module_loader_png}
%package module_loader_png
Summary: PNG Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libpng-devel
%description module_loader_png
PNG Image loader module for Evas
%endif

%if %{with module_saver_png}
%package module_saver_png
Summary: PNG Image saver module for Evas
Group: System Environment/Libraries
BuildRequires: libpng-devel
%description module_saver_png
PNG Image saver module for Evas
%endif

%if %{with module_loader_tiff}
%package module_loader_tiff
Summary: TIFF Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libtiff-devel
%description module_loader_tiff
TIFF Image loader module for Evas
%endif

%if %{with module_saver_tiff}
%package module_saver_tiff
Summary: TIFF Image saver module for Evas
Group: System Environment/Libraries
BuildRequires: libtiff-devel
%description module_saver_tiff
TIFF Image saver module for Evas
%endif

%if %{with module_loader_gif}
%package module_loader_gif
Summary: GIF Image loader module for Evas
Group: System Environment/Libraries
#BuildSuggests: libungif-devel, giflib-devel
BuildRequires: /usr/include/gif_lib.h
%description module_loader_gif
GIF Image loader module for Evas
%endif

%if %{with module_loader_edb}
%package module_loader_edb
Summary: EDB Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: edb-devel
%description module_loader_edb
EDB Image loader module for Evas
%endif

%if %{with module_saver_edb}
%package module_saver_edb
Summary: EDB Image saver module for Evas
Group: System Environment/Libraries
BuildRequires: edb-devel
%description module_saver_edb
EDB Image saver module for Evas
%endif

%if %{with module_loader_xpm}
%package module_loader_xpm
Summary: XPM Image loader module for Evas
Group: System Environment/Libraries
##BuildRequires: (none, X?)
%description module_loader_xpm
XPM Image loader module for Evas
%endif

%if %{with module_loader_svg}
%package module_loader_svg
Summary: SVG Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: esvg-devel >= 0.16
%description module_loader_svg
svg Image loader module for Evas
%endif

%if %{with module_loader_bmp}
%package module_loader_bmp
Summary: BMP Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_bmp
BMP Image loader module for Evas
%endif

%if %{with module_loader_wbmp}
%package module_loader_wbmp
Summary: WBMP Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_wbmp
WBMP Image loader module for Evas
%endif

%if %{with module_loader_tga}
%package module_loader_tga
Summary: TGA Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_tga
TGA Image loader module for Evas
%endif

%if %{with module_loader_ico}
%package module_loader_ico
Summary: ICO Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_ico
ICO Image loader module for Evas
%endif

%if %{with module_loader_psd}
%package module_loader_psd
Summary: PSD Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_psd
PSD Image loader module for Evas
%endif

%if %{with module_loader_generic}
%package module_loader_generic
Summary: Generic Image loader module for Evas
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description module_loader_generic
Generic Image loader module for Evas
%endif

%package module_engine_software_generic
Summary: Software X11 rendering engine module for Evas
Group: System Environment/Libraries
Requires: evas
%description module_engine_software_generic
Software X11 rendering engine module for Evas

%if %{with module_engine_software_x11}
%package module_engine_software_x11
Summary: Software X11 rendering engine module for Evas
Group: System Environment/Libraries
BuildRequires: libX11-devel, libICE-devel, libXext-devel
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_software_x11
Software X11 rendering engine module for Evas
%endif

%if %{with module_engine_buffer}
%package module_engine_buffer
Summary: Buffer rendering engine module for Evas
Group: System Environment/Libraries
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_buffer
Memory Buffer rendering engine module for Evas
%endif

%if %{with module_engine_fb}
%package module_engine_fb
Summary: Framebuffer rendering engine module for Evas
Group: System Environment/Libraries
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_fb
Framebuffer rendering engine module for Evas
%endif

%if %{with module_engine_gl_x11}
%package module_engine_gl_x11
Summary: OpenGL under X11 rendering engine module for Evas
Group: System Environment/Libraries
#BuildSuggests: xorg-x11-devel, xorg-x11-Mesa-libGL, XFree86-devel
Requires: evas
%description module_engine_gl_x11
OpenGL under X11 rendering engine module for Evas
%endif

%if %{with module_engine_directfb}
%package module_engine_directfb
Summary: Directfb rendering engine module for Evas
Group: System Environment/Libraries
#BuildSuggests: DirectFB, libdirectfb-devel, directfb-devel
BuildRequires: /usr/include/directfb/dfb_types.h
Requires: evas
%description module_engine_directfb
Directfb rendering engine module for Evas
%endif

%if %{with module_engine_software_16_x11}
%package module_engine_software_16_x11
Summary: Software 16-bit X11 rendering engine module for Evas
Group: System Environment/Libraries
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_software_16_x11
Software 16-bit X11 rendering engine module for Evas
%endif

%if %{with module_engine_software_sdl}
%package module_engine_software_sdl
Summary: Software SDL X11 rendering engine module for Evas
Group: System Environment/Libraries
BuildRequires: SDL-devel
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_software_sdl
Software SDL X11 rendering engine module for Evas
%endif

%if %{with module_engine_software_xcb}
%package module_engine_software_xcb
Summary: Software XCB X11 rendering engine module for Evas
Group: System Environment/Libraries
BuildRequires: libxcb-devel
Requires: evas-module_engine_software_generic
Requires: evas
%description module_engine_software_xcb
Software XCB X11 rendering engine module for Evas
%endif

%prep
%setup -q

%build
%{configure} --prefix=%{_prefix} --x-libraries=%{_prefix}/X11R6/%{_lib} \
    --disable-install-examples \
    %{?ac_with_module_loader_eet} \
    %{?ac_with_module_saver_eet} \
    %{?ac_with_module_loader_jpeg} \
    %{?ac_with_module_saver_jpeg} \
    %{?ac_with_module_loader_pmaps} \
    %{?ac_with_module_loader_png} \
    %{?ac_with_module_saver_png} \
    %{?ac_with_module_loader_tiff} \
    %{?ac_with_module_saver_tiff} \
    %{?ac_with_module_loader_gif} \
    %{?ac_with_module_loader_edb} \
    %{?ac_with_module_saver_edb} \
    %{?ac_with_module_loader_xpm} \
    %{?ac_with_module_loader_svg} \
    %{?ac_with_module_loader_bmp} \
    %{?ac_with_module_loader_wbmp} \
    %{?ac_with_module_loader_tga} \
    %{?ac_with_module_loader_ico} \
    %{?ac_with_module_loader_psd} \
    %{?ac_with_module_loader_generic} \
    %{?ac_with_module_engine_software_x11} \
    %{?ac_with_module_engine_buffer} \
    %{?ac_with_module_engine_fb} \
    %{?ac_with_module_engine_gl_x11} \
    %{?ac_with_module_engine_directfb} \
    %{?ac_with_module_engine_software_16_x11} \
    %{?ac_with_module_engine_software_sdl} \
    %{?ac_with_module_engine_software_xcb} \
    $RPM_CONFIGURE_OPTS
%{__make} %{?_smp_mflags} %{?mflags}
test -x `which doxygen` && /bin/sh gendoc || :

%install
%{__make} %{?mflags_install} DESTDIR=$RPM_BUILD_ROOT install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*/*/*/*a

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_bindir}/%{name}*
%{_libdir}/*.so.*
%{_libdir}/evas/modules/engines/wayland_shm/*/module.so
%{_libdir}/evas/cserve2/loaders/*/*/module.*
%{_prefix}/libexec/*
%{_datadir}/evas/checkme

%files devel
%defattr(-, root, root)
%doc src/examples/*.edc src/examples/*.png src/examples/*.c
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/evas-1/*.h
%files module_engine_software_generic
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/software_generic/*/module.so

%if %{with module_loader_eet}
%files module_loader_eet
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/eet/*/module.so
%endif

%if %{with module_saver_eet}
%files module_saver_eet
%defattr(-, root, root)
%{_libdir}/evas/modules/savers/eet/*/module.so
%endif

%if %{with module_loader_pmaps}
%files module_loader_pmaps
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/pmaps/*/module.so
%endif

%if %{with module_loader_png}
%files module_loader_png
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/png/*/module.so
%endif

%if %{with module_saver_png}
%files module_saver_png
%defattr(-, root, root)
%{_libdir}/evas/modules/savers/png/*/module.so
%endif

%if %{with module_loader_jpeg}
%files module_loader_jpeg
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/jpeg/*/module.so
%endif

%if %{with module_saver_jpeg}
%files module_saver_jpeg
%defattr(-, root, root)
%{_libdir}/evas/modules/savers/jpeg/*/module.so
%endif

%if %{with module_loader_tiff}
%files module_loader_tiff
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/tiff/*/module.so
%endif

%if %{with module_saver_tiff}
%files module_saver_tiff
%defattr(-, root, root)
%{_libdir}/evas/modules/savers/tiff/*/module.so
%endif

%if %{with module_loader_gif}
%files module_loader_gif
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/gif/*/module.so
%endif

%if %{with module_loader_edb}
%files module_loader_edb
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/edb/*/module.so
%endif

%if %{with module_saver_edb}
%files module_saver_edb
%defattr(-, root, root)
%{_libdir}/evas/modules/savers/edb/*/module.so
%endif

%if %{with module_loader_xpm}
%files module_loader_xpm
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/xpm/*/module.so
%endif

%if %{with module_loader_svg}
%files module_loader_svg
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/svg/*/module.so
%endif

%if %{with module_loader_bmp}
%files module_loader_bmp
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/bmp/*/module.so
%endif

%if %{with module_loader_wbmp}
%files module_loader_wbmp
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/wbmp/*/module.so
%endif

%if %{with module_loader_tga}
%files module_loader_tga
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/tga/*/module.so
%endif

%if %{with module_loader_ico}
%files module_loader_ico
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/ico/*/module.so
%endif

%if %{with module_loader_psd}
%files module_loader_psd
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/psd/*/module.so
%endif

%if %{with module_loader_generic}
%files module_loader_generic
%defattr(-, root, root)
%{_libdir}/evas/modules/loaders/generic/*/module.so
%endif

%if %{with module_engine_software_x11}
%files module_engine_software_x11
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/software_x11/*/module.so
%endif

%if %{with module_engine_buffer}
%files module_engine_buffer
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/buffer/*/module.so
%endif

%if %{with module_engine_fb}
%files module_engine_fb
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/fb/*/module.so
%endif

%if %{with module_engine_gl_x11}
%files module_engine_gl_x11
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/gl_x11/*/module.so
%endif

%if %{with module_engine_directfb}
%files module_engine_directfb
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/directfb/*/module.so
%endif

%if %{with module_engine_software_16_x11}
%files module_engine_software_16_x11
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/software_16/*/module.so
%{_libdir}/evas/modules/engines/software_16_x11/*/module.so
%endif

%if %{with module_engine_software_sdl}
%files module_engine_software_sdl
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/software_sdl/*/module.so
%endif

%if %{with module_engine_software_xcb}
%files module_engine_software_xcb
%defattr(-, root, root)
%{_libdir}/evas/modules/engines/software_xcb/*/module.so
%endif

%changelog
