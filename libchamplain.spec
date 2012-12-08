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
Version:	0.12.3
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
%{_libdir}/pkgconfig/champlain-memphis-%{api}.pc
%dir %{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/gtk-doc/html/%{name}-gtk
%doc %{_datadir}/gtk-doc/html/%{name}/*
%doc %{_datadir}/gtk-doc/html/%{name}-gtk/*
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/champlain
%{_includedir}/%{name}-%{api}/champlain/*.h
%dir %{_includedir}/%{name}-gtk-%{api}
%dir %{_includedir}/%{name}-gtk-%{api}/champlain-gtk/
%{_includedir}/%{name}-gtk-%{api}/champlain-gtk/*.h
%{_datadir}/gir-1.0/Champlain-%{gir_major}.gir
%{_datadir}/gir-1.0/GtkChamplain-%{gir_major}.gir
%{_datadir}/vala/vapi/champlain*



%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru 0.12.3-2
- rebuilt against new cogl

* Sun Jul 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12.3-1
+ Revision: 809443
- update to new version 0.12.3

* Wed May 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.12.2-3
+ Revision: 795051
- rebuild for new empathy

* Tue May 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12.2-2
+ Revision: 794861
- rebuild for clutter and typelib

* Mon Mar 12 2012 Götz Waschk <waschk@mandriva.org> 0.12.2-1
+ Revision: 784392
- fix linking
- new version
- drop patch

* Fri Dec 09 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.12.0-1
+ Revision: 739609
- fixed requires
- added p0 for g_thread_init build errors
- new version 0.12.0
- cleaned up spec
- split out gir pkgs
- removed mkrel, BuildRoot, clean section, defattr
- removed .la files
- added a few things from mga spec
- converted BRs to pkgconfig provides
- removed py pkg vestigages

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-3
+ Revision: 662352
- mass rebuild

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.8.3-2
+ Revision: 650920
- rebuild for updated libsoup libtool archive

* Thu Mar 31 2011 Götz Waschk <waschk@mandriva.org> 0.8.3-1
+ Revision: 649397
- update to new version 0.8.3

* Sun Mar 20 2011 Götz Waschk <waschk@mandriva.org> 0.8.2-1
+ Revision: 647186
- update to new version 0.8.2

* Tue Jan 18 2011 Götz Waschk <waschk@mandriva.org> 0.8.1-1
+ Revision: 631435
- new version

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 581428
- update to new version 0.8.0

* Sat Sep 18 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 579346
- update to new version 0.7.2

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-2mdv2011.0
+ Revision: 578926
- rebuild for new gobject-introspection

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 574534
- new version
- new api and major
- depend on memphis
- add vala binding
- disable python for now

* Sat Aug 21 2010 Götz Waschk <waschk@mandriva.org> 0.4.7-1mdv2011.0
+ Revision: 571686
- update to new version 0.4.7

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.6-4mdv2011.0
+ Revision: 568276
- enable vala support

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.6-3mdv2011.0
+ Revision: 568188
- rebuild for new libproxy

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0.4.6-2mdv2011.0
+ Revision: 563848
- rebuild for new gobject-introspection

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.4.6-1mdv2011.0
+ Revision: 550752
- new version
- drop patch

* Tue Mar 23 2010 Götz Waschk <waschk@mandriva.org> 0.4.5-1mdv2010.1
+ Revision: 526923
- update to new version 0.4.5

* Fri Feb 12 2010 Götz Waschk <waschk@mandriva.org> 0.4.4-3mdv2010.1
+ Revision: 504651
- rebuild for new clutter
- drop perl binding here

* Wed Feb 03 2010 Götz Waschk <waschk@mandriva.org> 0.4.4-2mdv2010.1
+ Revision: 500454
- add python and perl bindings

* Fri Jan 29 2010 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 497899
- update to new version 0.4.4

* Sat Jan 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 488189
- update to new version 0.4.3

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 460929
- new version
- drop patch

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 0.4.1-1mdv2010.0
+ Revision: 458924
- Release 0.4.1
- replace Patch0 with Fedora version

  + Götz Waschk <waschk@mandriva.org>
    - obsolete old devel package

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 440843
- new version
- new soname

* Fri Sep 04 2009 Götz Waschk <waschk@mandriva.org> 0.3.92-1mdv2010.0
+ Revision: 429873
- update to new version 0.3.92

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 0.3.91-1mdv2010.0
+ Revision: 420323
- update to new version 0.3.91

* Tue Aug 18 2009 Götz Waschk <waschk@mandriva.org> 0.3.90-4mdv2010.0
+ Revision: 417723
- fix build with new gobject-introspection
- fix devel provides

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 0.3.90-2mdv2010.0
+ Revision: 415270
- move typelib to the library packages

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 0.3.90-1mdv2010.0
+ Revision: 414452
- update build deps
- new version
- new source URL
- enable introspection

* Thu Aug 06 2009 Götz Waschk <waschk@mandriva.org> 0.3.6-2mdv2010.0
+ Revision: 410558
- fix devel provides

* Tue Aug 04 2009 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdv2010.0
+ Revision: 408646
- new version
- update deps
- new major
- readd libtool archives

* Sun Jul 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.3-1mdv2010.0
+ Revision: 392400
- Fix BuildRequires
- import libchamplain


