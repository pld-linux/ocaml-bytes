#
# Conditional build:
%bcond_without	ocaml_opt	# build opt (native code)

Summary:	Transitional Bytes module for OCaml
Summary(pl.UTF-8):	Przejściowy moduł Bytes dla OCamla
Name:		ocaml-bytes
Version:	1.2
Release:	2
License:	unknown
Group:		Libraries
Source0:	https://github.com/chambart/ocaml-bytes/archive/%{name}.%{version}.tar.gz
# Source0-md5:	487d38796dae39e06b7cfffcc82ea0f3
URL:		https://github.com/chambart/ocaml-bytes/
BuildRequires:	ocaml >= 3.04-7
# already included in OCaml 4
BuildRequires:	ocaml < 1:4
BuildRequires:	ocaml-findlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Transitional Bytes module to simplify adoption of -safe-string in
OCaml 4.02.0.

%description -l pl.UTF-8
Bytes module for compatibility with OCaml >= 4.02 (runtime part).
Przejściowy moduł Bytes ułatwiający adopcję typu -safe-string w
OCamlu 4.02.0.

%package devel
Summary:	Transitional Bytes module for OCaml
Summary(pl.UTF-8):	Przejściowy moduł Bytes dla OCamla
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Transitional Bytes module to simplify adoption of -safe-string in
OCaml 4.02.0.

%description devel -l pl.UTF-8
Bytes module for compatibility with OCaml >= 4.02 (runtime part).
Przejściowy moduł Bytes ułatwiający adopcję typu -safe-string w
OCamlu 4.02.0.

%prep
%setup -q -n %{name}-%{name}.%{version}

%build
%configure \
	--libdir=%{_libdir}/ocaml

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# adjust to PLD-specific layout
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/bytes
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/bytes/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/bytes
cat <<EOF >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/bytes/META
directory="+bytes"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README.md bytes.mli
%dir %{_libdir}/ocaml/bytes
%{_libdir}/ocaml/bytes/bytes.cm[aiox]
%if %{with ocaml_opt}
%{_libdir}/ocaml/bytes/bytes.a
%{_libdir}/ocaml/bytes/bytes.cmxa
%{_libdir}/ocaml/bytes/bytes.cmxs
%endif
%{_libdir}/ocaml/site-lib/bytes
