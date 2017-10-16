%global owner wolfwoolford
%global srcname did
Name: %{srcname}		
Version: %{version_base}
Release: %{version_release}%{org_tag}%{dist}
Summary: Localised bash history logging and searching	

License:	
URL: https://github.com/%{owner}/did		
Source0: https://github.com/%{owner}/%{srcname}/archive/v%{version_base}.tar.gz
BuildArch: noarch

%description
Directory specific command line history.

Did is a directory specific command line history logger for Linux style 
terminals. Did prints every command ever run in the current directory
using a simple command : 'did'

%prep
%setup -q

%build
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{srcname}/

%install
install -m 0644 -t %{buildroot}%{_sysconfdir}/xdg/%{srcname}/ didrc

%files
%doc README
%{_sysconfdir}/xdg/%{srcname}


%changelog

