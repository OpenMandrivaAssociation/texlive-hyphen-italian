%global tl_name hyphen-italian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.8g
Release:	%{tl_revision}.1
Summary:	Italian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/ithyph.tex
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-italian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Italian in ASCII encoding. Compliant with the
Recommendation UNI 6461 on hyphenation issued by the Italian Standards
Institution (Ente Nazionale di Unificazione UNI).

