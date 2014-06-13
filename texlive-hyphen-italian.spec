# revision 25990
# category TLCore
# catalog-ctan /language/hyphenation/ithyph.tex
# catalog-date 2009-09-29 00:01:21 +0200
# catalog-license lgpl
# catalog-version 4.8g
Name:		texlive-hyphen-italian
Version:	4.8g
Release:	9
Summary:	Italian hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/ithyph.tex
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-italian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Italian in ASCII encoding. Compliant
with the Recommendation UNI 6461 on hyphenation issued by the
Italian Standards Institution (Ente Nazionale di Unificazione
UNI).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-italian
%_texmf_language_def_d/hyphen-italian
%_texmf_language_lua_d/hyphen-italian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-italian <<EOF
\%% from hyphen-italian:
italian loadhyph-it.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-italian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-italian <<EOF
\%% from hyphen-italian:
\addlanguage{italian}{loadhyph-it.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-italian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-italian <<EOF
-- from hyphen-italian:
	['italian'] = {
		loader = 'loadhyph-it.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-it.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.8g-4
+ Revision: 804792
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.8g-3
+ Revision: 767563
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.8g-2
+ Revision: 759923
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.8g-1
+ Revision: 718665
- texlive-hyphen-italian
- texlive-hyphen-italian
- texlive-hyphen-italian
- texlive-hyphen-italian

