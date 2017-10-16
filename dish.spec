%global owner wolfwoolford
%global srcname dish
Name: %{srcname}		
Version: %{version_base}
Release: %{version_release}%{dist}
Summary: Localised bash history logging and searching	
Source: %{name}-%{version}.tgz

License: MIT	
URL: https://github.com/%{owner}/dish		
BuildArch: noarch

%description
DIrectory Specific command line History.

Dish is a directory specific command line history logger for bash
terminals. Dish prints every command ever run in the current directory
using a simple command : 'dish'

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{srcname}/
install -m 0644 -t %{buildroot}%{_sysconfdir}/xdg/%{srcname}/ dishrc

%files
%doc README
%{_sysconfdir}/xdg/%{srcname}


%changelog

