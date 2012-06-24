%define		pname	glosstex
Summary:	Prepare glossaries in LaTeX
Summary(pl):	Przygotowywanie s�ownik�w z obja�nieniami w LaTeXu
Name:		tetex-latex-glosstex
Version:	0.4
Release:	0.1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org:/pub/tex/support/%{pname}.tar.gz
# Source0-md5:	b6926a1b13eb73eff9df14d6f8340e1c
Source1:	glosstex.md5
BuildRequires:	tetex-format-latex
Requires:	tetex-latex
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	glosstexdir %{_datadir}/texmf/tex/latex/glosstex
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
GlossTeX is a tool for the automatic preparation of glossaries, lists
of acronyms and sorted lists in general for use with LaTeX and
MakeIndex. GlossTeX combines the functionality of acronym and nomencl
and provides some new features.

%description -l pl
GlossTeX to narz�dzie do automatycznego przygotowywania s�ownik�w z
obja�nieniami, wykaz�w skr�t�w i og�lnie posortowanych list do
u�ywania z LaTeXem i programem MakeIndex. GlossTeX ��czy
funkcjonalno�� pakiet�w acronym i nomencl, ma tak�e troch� nowych
mo�liwo�ci.

%prep
cd %{_sourcedir}
md5sum -c %{SOURCE1} > /dev/null
cd -
%setup -q -n %{pname}

%build
%{__make} CFLAGS="%{rpmcflags} -ansi -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{glosstexdir}}

install glosstex $RPM_BUILD_ROOT%{_bindir}/
install *.cfg *.sty *.std $RPM_BUILD_ROOT%{glosstexdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc Changes README TODO TAGS glosstex.dvi
%attr(755,root,root) %{_bindir}/*
%{glosstexdir}
