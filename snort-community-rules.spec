Summary:	The Community Rulesets for Snort
Name:		snort-community-rules
Version:	2.4
Release:	%mkrel 2
License:	GPL
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	http://www.snort.org/pub-bin/downloads.cgi/Download/comm_rules/Community-Rules-%{version}.tar.bz2
BuildArch:	noarch

%description
The Community Rulesets contain rules submitted by members of the
open source community. While these rules are available as is, the
VRT performs basic tests to ensure that new rules will not break
Snort. These rules are distributed under the GPL and are freely
available to all open source Snort users.

%prep

%setup -q -c -n Community-Rules-%{version}
%{__mv} docs signatures

%build

%install
%{__rm} -rf %{buildroot} 

%{__mkdir_p} %{buildroot}%{_sysconfdir}/snort/rules
%{__cp} -a rules/*.rules %{buildroot}%{_sysconfdir}/snort/rules/

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(0644,root,root,0755)
%doc signatures
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/*.rules


