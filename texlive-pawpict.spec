Name:		texlive-pawpict
Version:	1.0
Release:	1
Summary:	Using graphics from PAW
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pawpict
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Support for the easy inclusion of graphics made by PAW (Physics
Analysis Workstation). You need to have PAW installed on your
system to benefit from this package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pawpict/pawpict.sty
%doc %{_texmfdistdir}/doc/latex/pawpict/README
#- source
%doc %{_texmfdistdir}/source/latex/pawpict/pawpict.dtx
%doc %{_texmfdistdir}/source/latex/pawpict/pawpict.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
