%define libver 0.3
%define libgtkver %{libver}
%define major 3
%define gtkmajor %{major}

%define libname		%mklibname champlain %{libver} %{major}
%define libgtkname	%mklibname champlain-gtk %{libgtkver} %{gtkmajor}
%define develname	%mklibname champlain %{libver} -d


Summary:	Map view for Clutter
Name:		libchamplain
Version:	0.3.6
Release:	%mkrel 1
License:	LGPLv2+
Group:		Graphical desktop/GNOME 
URL:		http://blog.pierlux.com/projects/libchamplain/en/
Source0:	http://libchamplain.pierlux.com/release/latest/%{name}-%{version}.tar.bz2
BuildRequires:	clutter-gtk-devel >= 0.10
BuildRequires: 	libsoup-devel
#gw introspection support broken in 0.3.6
#BuildRequires:  gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package -n %{libname}
Summary:	Map view for Clutter
Group:		System/Libraries

%description -n %{libname}
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package -n %{libgtkname}
Summary:	Map view for Clutter
Group:		System/Libraries

%description -n %{libgtkname}
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

This package contains the GTK+ view for %{name}

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+
Requires:	%libname = %{version}
Requires:	%libgtkname = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-gtk-doc
%make

%install
rm -rf ${buildroot}
%makeinstall_std 

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/%{name}-%{libver}.so.%{major}*

%files -n %{libgtkname}
%defattr(-,root,root,-)
%{_libdir}/%{name}-gtk-%{libgtkver}.so.%{gtkmajor}*


%files -n %{develname}
%defattr(-,root,root,-)
%doc NEWS
%doc demos/launcher.c
%{_libdir}/*.la
%{_libdir}/%{name}-%{libver}.so
%{_libdir}/%{name}-gtk-%{libgtkver}.so
%{_libdir}/pkgconfig/champlain-%{libver}.pc
%{_libdir}/pkgconfig/champlain-gtk-%{libgtkver}.pc
%dir %{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/gtk-doc/html/%{name}-gtk
%doc %{_datadir}/gtk-doc/html/%{name}/*
%doc %{_datadir}/gtk-doc/html/%{name}-gtk/*
%dir %{_includedir}/%{name}-%{libver}
%dir %{_includedir}/%{name}-%{libver}/champlain
%{_includedir}/%{name}-%{libver}/champlain/*.h
%dir %{_includedir}/%{name}-gtk-%{libgtkver}
%dir %{_includedir}/%{name}-gtk-%{libgtkver}/champlain-gtk/
%{_includedir}/%{name}-gtk-%{libgtkver}/champlain-gtk/*.h

