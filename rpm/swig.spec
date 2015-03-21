Name:       swig
Summary:    Connects C/C++/Objective C to some high-level programming languages
Version:    2.0.12
Release:    1
Group:      Development/Tools
License:    GPLv3
URL:        http://swig.sourceforge.net
Source0:    http://download.sourceforge.net/swig/swig-%{version}.tar.gz
Source1:    swig-rpmlintrc
Source100:  swig.yaml
Patch0:     swig-1.3.23-pylib.patch
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  perl
BuildRequires:  python-devel
BuildRequires:  fdupes

%description
SWIG is a software development tool that connects programs written in C
and C++ with a variety of high-level programming languages. SWIG is 
primarily used with common scripting languages such as Perl, PHP, Python,
Tcl/Tk, and Ruby, however the list of supported languages also includes
non-scripting languages such as C#, Common Lisp (CLISP, Allegro CL, UFFI),
Java, Modula-3, OCAML, Octave, and R. Also several interpreted and compiled
Scheme implementations (Guile, MzScheme, Chicken) are supported. SWIG is 
most commonly used to create high-level interpreted or compiled programming 
environments, user interfaces, and as a tool for testing and prototyping C/C++
software. SWIG can also export its parse tree in the form of XML and Lisp
s-expressions.

%package doc
Summary:    Documentation files for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q
cd swig
%patch0 -p1

%build
cd swig
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd swig
%make_install
%fdupes  %{buildroot}/%{_datadir}/swig/

%files
%defattr(-,root,root,-)
%doc LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%{_bindir}/*
%{_datadir}/swig
%{_mandir}/man1/ccache-swig.1.gz

%files doc
%defattr(-,root,root,-)
%doc ANNOUNCE CHANGES INSTALL README TODO
%doc Doc/*
