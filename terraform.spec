Summary:	An interactive fractal landscape generator
Summary(pl):	Interaktywny generator krajobrazów fraktalnych
Name:		terraform
Version:	0.9.0
Release:	5
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/terraform/%{name}-%{version}.tar.gz
# Source0-md5:	a1af0cbb6719b49b30d326df9d06434a
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-acfix2.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-po.patch
URL:		http://terraform.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel
BuildRequires:	gtk+-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and
transform it.

%description -l pl
Terraform to interaktywny program do generowania i obrabiania terenów.
Pozwala wygenerowaæ losowy teren i przetransformowaæ go.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-sgmltools
	# don't work with our sgml-tools

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install desktop-links/Terraform.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install desktop-links/terraform.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog docs/*.sgml
%attr(755,root,root) %{_bindir}/terraform
%{_datadir}/terraform
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
