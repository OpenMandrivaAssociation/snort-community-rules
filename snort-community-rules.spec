Summary:	The Community Rulesets for Snort
Name:		snort-community-rules
Version:	2.4
Release:	7
License:	GPL
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	http://www.snort.org/pub-bin/downloads.cgi/Download/comm_rules/Community-Rules-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.4-6mdv2010.0
+ Revision: 433982
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4-5mdv2009.0
+ Revision: 260873
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4-4mdv2009.0
+ Revision: 252690
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.4-2mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Oct 22 2006 David Walluck <walluck@mandriva.org> 2.4-2mdv2007.0
+ Revision: 71647
+ Status: not released
- rebuild
- Import snort-community-rules

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-1mdk
- initial Mandriva package

