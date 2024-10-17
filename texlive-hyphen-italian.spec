Name:		texlive-hyphen-italian
Version:	58652
Release:	2
Summary:	Italian hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/ithyph.tex
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-italian.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-italian
%_texmf_language_def_d/hyphen-italian
%_texmf_language_lua_d/hyphen-italian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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
