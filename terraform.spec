Summary:	An interactive fractal landscape generator
Summary(pl):	Interaktywny generator krajobrazów fraktalnych
Name:		terraform
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	%{name}-%{version}.tar.gz
URL:		http://212.187.12.197/RNG/terraform/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and
transform it.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" ./configure --prefix=%prefix
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/terraform
%{_datadir}/terraform/terraform-logo.jpg
%{_datadir}/terraform/tf_land.pov
%{_datadir}/terraform/arrow_right.xpm
%doc AUTHORS COPYING ChangeLog README FAQ
