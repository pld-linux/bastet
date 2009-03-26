Summary:	Tetris game
Summary(pl.UTF-8):	Gra typu tetris
Name:		bastet
Version:	0.43
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tgz
# Source0-md5:	b47090daa7b6d89b98b5b477cf155733
URL:		http://fph.altervista.org/prog/bastet.html
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetris game clone.

%description -l pl.UTF-8
Klon gry tetris.

%prep
%setup -q
%{__sed} -i 's@curses.h@ncurses/curses.h@' `grep -r -l 'curses.h' .`

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags} `ncurses5-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bastet $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
