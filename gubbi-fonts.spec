%global fontname gubbi
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.1
Release:        2%{?dist}
Summary:        Free Kannada Opentype serif font

Group:          User Interface/X
License:        OFL
URL:            https://github.com/aravindavk/Gubbi
Source0:        http://cloud.github.com/downloads/aravindavk/Gubbi/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Source1: 65-0-gubbi.conf


%description
This package provides a free Kannada opentype serif font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYING README


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Pravin Satpute <psatpute@redhat.com> - 1.1-1
- Resolves bug 842962

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Pravin Satpute <psatpute@redhat.com> - 1.0-1
- Initial build

