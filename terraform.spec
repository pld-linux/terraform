Summary:	An interactive fractal landscape generator
Summary(pl):	Interaktywny generator krajobrazów fraktalnych
Name:		terraform
Version:	0.8.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/terraform/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://terraform.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	gnome-print-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and
transform it.

%description -l pl
Terraform to interaktywny program do generowania i obrabiania terenów.
Pozwala wygenerowaæ losowy teren i przetransformowaæ go.

%prep
%setup -q
%patch -p1

%build
rm -f missing
gettextize -c -f
aclocal -I macros
autoconf
automake -a -c -f
%configure \
	--disable-sgmltools
	# don't work with our sgml-tools

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install desktop-links/Terraform.desktop $RPM_BUILD_ROOT%{_applnkdir}/%{name}.desktop
install desktop-links/terraform.png $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS ChangeLog docs/{FAQ,README,UsersGuide}.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz
%attr(755,root,root) %{_bindir}/terraform
%{_datadir}/terraform
%{_applnkdir}/*
%{_pixmapsdir}/*
