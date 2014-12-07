%define oname		champlain

%define api			0.12
%define major		0
%define gir_major	0.12
%define libname		%mklibname champlain %{api} %{major}
%define libgtk		%mklibname champlain-gtk %{api} %{major}
%define girname		%mklibname %{oname}-gir %{gir_major}
%define girgtk		%mklibname %{oname}-gtk-gir %{gir_major}
%define develname	%mklibname champlain %{api} -d

Summary:	Map view for Clutter
Name:		libchamplain
Version:	0.12.9
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/GNOME 
URL:		http://blog.pierlux.com/projects/libchamplain/en/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/0.12/%{name}-%{version}.tar.xz
Patch0:		libchamplain-0.12.2-fix-linking.patch
BuildRequires:	chrpath
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(memphis-0.2)
BuildRequires:	vala-tools

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package -n %{libname}
Summary:	Map view for Clutter
Group:		System/Libraries

%description -n %{libname}
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package -n %{libgtk}
Summary:	Map view for Clutter
Group:		System/Libraries

%description -n %{libgtk}
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

This package contains the GTK+ view for %{name}

%package -n %{girname}
Summary:	GObject Introspection interface description for GData
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for GData.

%package -n %{girgtk}
Summary:	GObject Introspection interface description for GData
Group:		System/Libraries
Requires:	%{libgtk} = %{version}-%{release}

%description -n %{girgtk}
GObject Introspection interface description for GData.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgtk} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girgtk} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname champlain 0.3 -d

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q
%apply_patches

autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc \
	--enable-python \
	--enable-introspection 

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%make

%install
%makeinstall_std 
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Remove rpaths.
chrpath --delete %{buildroot}%{_libdir}/%{name}-gtk-*.so.*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Champlain-%{gir_major}.typelib

%files -n %{libgtk}
%{_libdir}/%{name}-gtk-%{api}.so.%{major}*

%files -n %{girgtk}
%{_libdir}/girepository-1.0/GtkChamplain-%{gir_major}.typelib

%files -n %{develname}
%doc NEWS
%doc demos/launcher.c
%{_libdir}/%{name}-%{api}.so
%{_libdir}/%{name}-gtk-%{api}.so
%{_libdir}/pkgconfig/champlain-%{api}.pc
%{_libdir}/pkgconfig/champlain-gtk-%{api}.pc
# %{_libdir}/pkgconfig/champlain-memphis-%{api}.pc
%dir %{_datadir}/gtk-doc/html/%{name}-%{api}
%dir %{_datadir}/gtk-doc/html/%{name}-gtk-%{api}
%doc %{_datadir}/gtk-doc/html/%{name}-%{api}/*
%doc %{_datadir}/gtk-doc/html/%{name}-gtk-%{api}/*
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/champlain
%{_includedir}/%{name}-%{api}/champlain/*.h
%dir %{_includedir}/%{name}-gtk-%{api}
%dir %{_includedir}/%{name}-gtk-%{api}/champlain-gtk/
%{_includedir}/%{name}-gtk-%{api}/champlain-gtk/*.h
%{_datadir}/gir-1.0/Champlain-%{gir_major}.gir
%{_datadir}/gir-1.0/GtkChamplain-%{gir_major}.gir
%{_datadir}/vala/vapi/champlain*

