Name:		texlive-pawpict
Version:	21629
Release:	1
Summary:	Using graphics from PAW
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pawpict
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Support for the easy inclusion of graphics made by PAW (Physics
Analysis Workstation). You need to have PAW installed on your
system to benefit from this package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
