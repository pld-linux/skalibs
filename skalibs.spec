#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	Essentially general-purpose libraries
Summary(pl.UTF-8):	Istotne biblioteki ogólnego przeznaczenia
Name:		skalibs
Version:	2.3.10.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://skarnet.org/software/skalibs/%{name}-%{version}.tar.gz
# Source0-md5:	51cb8484896c68eb8d167767cdfc702e
URL:		http://skarnet.org/software/skalibs/
BuildRequires:	make >= 3.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# FIXME. temporarily disable. fix this later
%define		skip_post_check_so	libbiguint.so.%{version} libdatastruct.so.%{version} librandom.so.%{version} libstdcrypto.so.%{version} libunixonacid.so.%{version}

%description
skalibs is a package centralizing the public-domain C development
files I use for building other software: it contains essentially
general-purpose libraries. You will need to install skalibs if you
plan to build skarnet.org software. The point is that you won't have
to download and compile big libraries everytime you need to build a
package: do it only once.

skalibs can also be used as a sound basic start for C development.
There are a lot of general-purpose libraries out there; but if your
main goal is to produce small and secure C code, you will like
skalibs.

skalibs contains exclusively public-domain code. So you can
redistribute it as you want, and it does not prevent you from
distributing any of your executables.

%description -l pl.UTF-8
skalibs to pakiet centralizujący pliki programistyczne C będące
własnością publiczną (public-domain) używane przez autora do tworzenia
innego oprogramowania - zawiera istotne biblioteki ogólnego
przeznaczenia. Trzeba zainstalować ten pakiet, aby móc budować
programy ze skarnet.org. Cel jest taki, że nie trzeba ściągać i
kompilować dużych bibliotek za każdym razem przy budowaniu pakietu -
robi się to tylko raz.

skalibs można używać także przy rozpoczynaniu programowania w C. Jest
tu wiele bibliotek ogólnego przeznaczenia; ale jeśli głównym celem
jest tworzenie małego i bezpiecznego kodu w C, skalibs jest dobrym
rozwiązaniem.

skalibs zawiera wyłącznie kod public-domain. Można go więc
rozpowszechniać w dowolny sposób i nie przeszkadza to w
rozpowszechnianiu własnych binarek.

%package devel
Summary:	Header files and development documentation for skalibs
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty do skalibs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for skalibs.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do skalibs.

%package static
Summary:	Static skalibs library
Summary(pl.UTF-8):	Statyczna biblioteka skalibs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static skalibs library.

%description static -l pl.UTF-8
Statyczna biblioteka skalibs.

%prep
%setup -q

sed -i -e "s~tryldflag LDFLAGS_AUTO -Wl,--hash-style=both~:~" configure

%build
%configure \
	--enable-ipv6 \
	%{__enable_disable static-libs static_libs} \
	--dynlibdir=%{_libdir} \
	--libdir=%{_libdir} \
	--datadir=%{_sysconfdir} \
	--sysdepdir=%{_libdir}/%{name} \
	--enable-force-devr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_includedir}/%{name}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# SONAME: libskarnet.so.2.3
# so this is junk
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libskarnet.so.2.3.10

%if 0
cp -p etc/leapsecs.dat $RPM_BUILD_ROOT%{_sysconfdir}
cp -a include/* $RPM_BUILD_ROOT%{_includedir}/%{name}

cp -a library.so/* $RPM_BUILD_ROOT%{_libdir}
%if %{with static_libs}
cp -a library/* $RPM_BUILD_ROOT%{_libdir}
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbiguint.so.1.4
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdatastruct.so.1.4
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librandom.so.1.4
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstdcrypto.so.1.4
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstddjb.so.1.4
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunixonacid.so.1.4
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING AUTHORS
%attr(755,root,root) %{_libdir}/libskarnet.so.2.3.10.0
%ghost %{_libdir}/libskarnet.so.2.3
%if 0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/leapsecs.dat
%attr(755,root,root) %{_libdir}/libbiguint.so.*.*.*
%ghost %{_libdir}/libbiguint.so.1
%attr(755,root,root) %{_libdir}/libdatastruct.so.*.*.*
%ghost %{_libdir}/libdatastruct.so.1
%attr(755,root,root) %{_libdir}/librandom.so.*.*.*
%ghost %{_libdir}/librandom.so.1
%attr(755,root,root) %{_libdir}/libstdcrypto.so.*.*.*
%ghost %{_libdir}/libstdcrypto.so.1
%attr(755,root,root) %{_libdir}/libstddjb.so.*.*.*
%ghost %{_libdir}/libstddjb.so.1
%attr(755,root,root) %{_libdir}/libunixonacid.so.*.*.*
%ghost %{_libdir}/libunixonacid.so.1
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/libskarnet.so
%if 0
%{_libdir}/libbiguint.so
%{_libdir}/libdatastruct.so
%{_libdir}/librandom.so
%{_libdir}/libstdcrypto.so
%{_libdir}/libstddjb.so
%{_libdir}/libunixonacid.so
%endif
%{_includedir}/skalibs
%dir %{_libdir}/skalibs
%{_libdir}/skalibs/rt.lib
%{_libdir}/skalibs/socket.lib
%{_libdir}/skalibs/sysclock.lib
%{_libdir}/skalibs/sysdeps
%{_libdir}/skalibs/sysdeps.h
%{_libdir}/skalibs/tainnow.lib
%{_libdir}/skalibs/target
%{_libdir}/skalibs/util.lib

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libskarnet.a
%endif
