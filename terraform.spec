# Note that this is NOT a relocatable package
%define ver		0.4.4
%define RELEASE		1
%define rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix		/usr

Summary: An interactive fractal landscape generator
Name: terraform
Version: %ver
Release: %rel
Copyright: GPL
Group: Graphics
Source: terraform-%{ver}.tar.gz
BuildRoot: /var/tmp/terraform-%{PACKAGE_VERSION}-root
URL: http://212.187.12.197/RNG/terraform/
Docdir: %{prefix}/doc

%description
Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and transform it.

%changelog
* Mon Oct 18 1999 Robert Gasch <Robert_Gasch@peoplesoft.com>
- first spec file 

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/terraform
%{prefix}/share/terraform/terraform-logo.jpg
%{prefix}/share/terraform/tf_land.pov
%{prefix}/share/terraform/arrow_right.xpm
%doc AUTHORS COPYING ChangeLog README FAQ
