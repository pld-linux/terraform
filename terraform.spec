Summary:	An interactive fractal landscape generator
Name:		terraform
Version:	0.4.4
Release:	1
License:	GPL
Group:		Graphics
Source:		terraform-%{ver}.tar.gz
URL:		http://212.187.12.197/RNG/terraform/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and transform it.

%prep
%setup -q

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
