Summary:	Tetris game
Summary(hu.UTF-8):	Egy Tetris-klón
Summary(pl.UTF-8):	Gra typu tetris
Name:		bastet
Version:	0.43
Release:	4
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tgz
# Source0-md5:	b47090daa7b6d89b98b5b477cf155733
URL:		http://fph.altervista.org/prog/bastet.html
BuildRequires:	boost-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bastet stands for "bastard tetris", and is a simple ncurses-based
Tetris(R) clone for Linux. Unlike normal Tetris(R), however, Bastet
does not choose your next brick at random. Instead, it uses a special
algorithm designed to choose the worst brick possible. As you can
imagine, playing Bastet can be a very frustrating experience!

%description -l hu.UTF-8
Bastet a "bastard tetris" rövidítése, és egy egyszerű ncurses-alapú
Tetris(R)-klón Linux-ra. A hagyományos Tetris(R)-szel ellentétben a
Bastet a következő elemet nem véletlenszerűen választja, hanem egy
speciális algoritmust használ, amellyel a lehető legrosszabb elemet
választja ki. Gondolhatod, hogy a Bastet-tel való játék nagyon mennyire
frusztráló lehet!

%description -l pl.UTF-8
Bastet oznacza "bastard tetris". Jest to prosty klon gry tetris z tekstowym
interfejsem użytkownika opartym o bibliotekę ncurses. W odróżnieniu od innych
implementacji gry tetris Bastet używa wyrafinowanego algorytmu, który dobiera
zawsze najgorszy klocek do aktualnej sytuacji. Można się zatem domyślić, że
granie w Bastet jest bardzo frustrującym przeżyciem.

%prep
%setup -q
%{__sed} -i 's@curses.h@ncurses/curses.h@' *.?pp

%build
NCURSES_LIBS=$(ncurses5-config --libs)
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags} $NCURSES_LIBS"

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
