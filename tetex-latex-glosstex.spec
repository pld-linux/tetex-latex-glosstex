Summary:	Prepare glossaries in LaTeX.
Name:		glosstex
Version:	0.4
Release:	0.1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org:/pub/tex/support/%{name}.tar.gz
Source1:	glosstex.md5
BuildRequires:	tetex-format-latex
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define glosstexdir %{_datadir}/texmf/tex/latex/glosstex

%description
GlossTeX is a tool for the automatic preparation of glossaries, lists of
acronyms and sorted lists in general for use with LaTeX and MakeIndex.
GlossTeX combines the functionality of acronym and nomencl and provides
some new features.

%prep
cd %{_sourcedir}
md5sum -c %{SOURCE1} > /dev/null
cd -
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -ansi -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{glosstexdir}}

install glosstex $RPM_BUILD_ROOT%{_bindir}/
install *.cfg *.sty $RPM_BUILD_ROOT%{glosstexdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO TAGS glosstex.dvi
%attr(755,root,root) %{_bindir}/*
%{glosstexdir}
