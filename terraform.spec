Summary:	An interactive fractal landscape generator
Summary(pl):	Interaktywny generator krajobrazów fraktalnych
Name:		terraform
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/terraform/%{name}-%{version}.tar.gz
URL:		http://terraform.sourceforge.net/
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

%build
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS ChangeLog README FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,FAQ}.gz
%attr(755,root,root) %{_bindir}/terraform
%dir %{_datadir}/terraform
%{_datadir}/terraform/terraform-logo.jpg
%{_datadir}/terraform/tf_land.pov
%{_datadir}/terraform/arrow_right.xpm
