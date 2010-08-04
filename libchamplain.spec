%define libver 0.4
%define libgtkver %{libver}
%define major 0
%define gtkmajor %{major}

%define libname		%mklibname champlain %{libver} %{major}
%define libgtkname	%mklibname champlain-gtk %{libgtkver} %{gtkmajor}
%define develname	%mklibname champlain %{libver} -d

Summary:	Map view for Clutter
Name:		libchamplain
Version:	0.4.6
Release:	%mkrel 2
License:	LGPLv2+
Group:		Graphical desktop/GNOME 
URL:		http://blog.pierlux.com/projects/libchamplain/en/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	clutter-gtk-devel >= 0.10
BuildRequires: 	libsoup-devel
BuildRequires:  gobject-introspection-devel
#gw python binding:
BuildRequires:  python-clutter-gtk-devel
BuildRequires:  python-clutter-devel
BuildRequires:  libGConf2-devel 
BuildRequires:  pygtk2.0-devel
#gw Csharp binding
#BuildRequires: clutter-gtk-sharp
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
Provides:	%name-devel = %version-%release
Obsoletes:	%mklibname champlain 0.3 -d

%description -n %{develname}
This package contains development files for %{name}.


%package -n python-champlain
Summary: Python bindings for %name
Group: Development/Python
Requires: %libname = %{version}
Requires: python-clutter-gtk

%description -n python-champlain
This package contains Python bindings for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-gtk-doc --enable-python
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
cp -r bindings/python/demos .
rm -f demos/Makefile*

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/%{name}-%{libver}.so.%{major}*
%_libdir/girepository-1.0/Champlain-%libver.typelib

%files -n %{libgtkname}
%defattr(-,root,root,-)
%{_libdir}/%{name}-gtk-%{libgtkver}.so.%{gtkmajor}*
%_libdir/girepository-1.0/GtkChamplain-%libver.typelib

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
%_datadir/gir-1.0/Champlain-%libver.gir
%_datadir/gir-1.0/GtkChamplain-%libver.gir

%files -n python-champlain
%defattr(-,root,root,-)
%doc README
%doc demos/
%{py_platsitedir}/champlain.*
%{py_platsitedir}/champlaingtk.*
