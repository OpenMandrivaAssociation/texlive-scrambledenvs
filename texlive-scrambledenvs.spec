Name:		texlive-scrambledenvs
Version:	60615
Release:	1
Summary:	Create and print scrambled environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scrambledenvs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrambledenvs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrambledenvs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrambledenvs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to create and print scrambled
environments for purposes such as randomized hint environments.
You can mark a location with a series of hints, and then print
the hints at the end in a pseudo-random order. The general
structure follows: there is an outer environment which creates
the label, an inner environment that creates the references,
and a print command that prints out all of the hints. This
generalizes beyond hints; one can create scrambled solutions as
well, etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/scrambledenvs
%{_texmfdistdir}/tex/latex/scrambledenvs
%doc %{_texmfdistdir}/doc/latex/scrambledenvs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
