Summary:	Dia2Code generate code from a Dia diagram
Summary(pl.UTF-8):	Dia2Code generuje kod źródłowy z diagramów Dia
Name:		dia2code
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/dia2code/%{name}-%{version}.tar.gz
# Source0-md5:	496a8b855c1db4143b40eb11f5adbc30
Patch0:		dia2code-1.0.0-fix-imports.patch
URL:		http://dia2code.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.4.1
Requires:	libxml2 >= 2.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dia2Code is a small utility used to generate code from a Dia diagram.
Generates code for: ActionScript3. Ada, C, C++, C#, Java, PHP(4,5),
Python, Ruby, shapefile and SQL.

%description -l pl.UTF-8
Dia2Code to małe narzędzie, które generuje kod źródłowy z diagramów
Dia. Generuje kod źródłowy dla języków: ActionScript3, Ada, C, C++,
C#, Java, PHP(4,5), Python, Ruby, shapefile oraz SQL.

%prep
%setup -q
%patch -P0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p docs/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
