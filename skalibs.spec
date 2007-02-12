Summary:	Essentially general-purpose libraries
Summary(pl.UTF-8):	Istotne biblioteki ogólnego przeznaczenia
Name:		skalibs
Version:	0.44
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.skarnet.org/software/skalibs/%{name}-%{version}.tar.gz
# Source0-md5:	0e5e06a51af541a4ea15cba64d71f4d5
URL:		http://www.skarnet.org/software/skalibs/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -c

%build
cd prog/%{name}-%{version}
# see http://www.skarnet.org/software/skalibs/install.html

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
