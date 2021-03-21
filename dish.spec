%global owner wolfwoolford
Name: dish
Version: 1.0
Release: 1%{dist}
Summary: Localised bash history logging and searching	
Source: %{name}-%{version}.tgz

License: MIT	
URL: https://github.com/%{owner}/%{name}
BuildArch: noarch

%description
DIrectory Specific command line History.

Dish is a directory specific command line history logger for bash
terminals. Dish prints every command ever run in the current directory
using a simple command : 'dish'

%prep
%setup -q -n %{name}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/ dishrc

%files
%doc README
%{_datadir}/%{name}


%changelog

