%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          imgtools
Summary:       A Tk extension to scale and rotate photo images
Version:       0.3
Release:       0
License:       BSD 2-Clause license
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://sourceforge.net/projects/tkimgtools/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.6
BuildRequires: tk-devel >= 8.6
Requires:      tcl >= 8.6
Requires:      tk >= 8.6
BuildRoot:     %{buildroot}

%description
Imgtools is a C extension to Tk that provides functionality to
transform and manipulate photo images.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="%optflags" ./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{directory}/%{_lib}/tcl
%{directory}/share/man/mann
