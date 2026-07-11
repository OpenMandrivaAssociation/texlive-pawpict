%global tl_name pawpict
%global tl_revision 21629

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Using graphics from PAW
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pawpict
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for the easy inclusion of graphics made by PAW (Physics Analysis
Workstation). You need to have PAW installed on your system to benefit
from this package.

