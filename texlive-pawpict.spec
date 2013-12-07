# revision 21629
# category Package
# catalog-ctan /macros/latex/contrib/pawpict
# catalog-date 2007-01-12 20:52:49 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-pawpict
Version:	1.0
Release:	5
Summary:	Using graphics from PAW
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pawpict
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pawpict.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754723
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719208
- texlive-pawpict
- texlive-pawpict
- texlive-pawpict
- texlive-pawpict

