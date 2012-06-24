Summary:	Essentially general-purpose libraries
Summary(pl):	Istotne biblioteki og�lnego przeznaczenia
Name:		skalibs
Version:	0.43
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.skarnet.org/software/skalibs/%{name}-%{version}.tar.gz
# Source0-md5:	b7510392a4485bb5209e97ba3115d755
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

%description -l pl
skalibs to pakiet centralizuj�cy pliki programistyczne C b�d�ce
w�asno�ci� publiczn� (public-domain) u�ywane przez autora do tworzenia
innego oprogramowania - zawiera istotne biblioteki og�lnego
przeznaczenia. Trzeba zainstalowa� ten pakiet, aby m�c budowa�
programy ze skarnet.org. Cel jest taki, �e nie trzeba �ci�ga� i
kompilowa� du�ych bibliotek za ka�dym razem przy budowaniu pakietu -
robi si� to tylko raz.

skalibs mo�na u�ywa� tak�e przy rozpoczynaniu programowania w C. Jest
tu wiele bibliotek og�lnego przeznaczenia; ale je�li g��wnym celem
jest tworzenie ma�ego i bezpiecznego kodu w C, skalibs jest dobrym
rozwi�zaniem.

skalibs zawiera wy��cznie kod public-domain. Mo�na go wi�c
rozpowszechnia� w dowolny spos�b i nie przeszkadza to w
rozpowszechnianiu w�asnych binarek.

%package devel
Summary:	Header files and development documentation for skalibs
Summary(pl):	Pliki nag��wkowe i dokumentacja programisty do skalibs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for skalibs.

%description devel -l pl
Pliki nag��wkowe i dokumentacja programisty do skalibs.

%package static
Summary:	Static skalibs library
Summary(pl):	Statyczna biblioteka skalibs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static skalibs library.

%description static -l pl
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
