%global owner wolfwoolford
%global srcname dish
Name: %{srcname}		
Version: %{version_base}
Release: %{version_release}%{org_tag}%{dist}
Summary: Localised bash history logging and searching	

License:	
URL: https://github.com/%{owner}/dish		
Source0: https://github.com/%{owner}/%{srcname}/archive/v%{version_base}.tar.gz
BuildArch: noarch

%description
DIrectory Specific command line History.

Dish is a directory specific command line history logger for bash
terminals. Dish prints every command ever run in the current directory
using a simple command : 'dish'

%prep
%setup -q

%build
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{srcname}/

%install
install -m 0644 -t %{buildroot}%{_sysconfdir}/xdg/%{srcname}/ dishrc

%files
%doc README
%{_sysconfdir}/xdg/%{srcname}


%changelog

