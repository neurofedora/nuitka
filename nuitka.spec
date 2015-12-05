%global __python %{__python3}

Name:           nuitka
Version:        0.5.16.1
Release:        1%{?dist}
Summary:        Python compiler with full language support and CPython compatibility

License:        ASL 2.0
URL:            http://nuitka.net
Source0:        http://nuitka.net/releases/Nuitka-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
# Test deps
BuildRequires:  scons
BuildRequires:  python2-devel
BuildRequires:  chrpath
BuildRequires:  strace
# TODO: Once 3.5 will be supported, include python3 versions also
# ignatenkobrain: do not test qt4, qt5 and pyside, something broken
BuildRequires:  python-lxml
BuildRequires:  tkinter
Requires:       gcc-c++
Requires:       python3-devel scons
Recommends:     strace

%description
Python compiler with full language support and CPython compatibility

This Python compiler achieves full language compatibility and compiles Python
code into compiled objects that are not second class at all. Instead they can be
used in the same way as pure Python objects.

%prep
%autosetup -n Nuitka-%{version}

%build
%py3_build

%install
CFLAGS="%{optflags}" %{__python3} setup.py  install -O1 --skip-build --root %{buildroot} --install-lib=%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m0644 doc/{nuitka,nuitka-run}.1 %{buildroot}%{_mandir}/man1/

%check
%{__python3} tests/run-tests

%files
%license LICENSE.txt
%doc README.rst
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.1*
%{_datadir}/%{name}/

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.16.1
- Initial package
