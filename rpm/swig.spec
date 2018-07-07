Name:       swig
Summary:    Connects C/C++/Objective C to some high-level programming languages
Version:    3.0.12
Release:    1
Group:      Development/Tools
License:    GPLv3
URL:        http://swig.sourceforge.net
Source0:    http://download.sourceforge.net/swig/swig-%{version}.tar.gz
Source1:    swig-rpmlintrc
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  perl
BuildRequires:  python-devel
BuildRequires:  fdupes
BuildRequires:  byacc

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

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%autogen
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes  %{buildroot}/%{_datadir}/swig/

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/swig
