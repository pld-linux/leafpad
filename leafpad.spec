Summary:	GTK+2 based notepad clone
Summary(pl.UTF-8):	Klon notepada oparty na GTK+
Name:		leafpad
Version:	0.8.18.1
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
# Source0-md5:	254a72fc67505e3aa52884c729cd7b97
Patch0:		%{name}-werror.patch
URL:		http://tarot.freeshell.org/leafpad/
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leafpad is a simple GTK+ based text editor. The user interface is
similar to "notepad", and it aims to be lighter than GEdit and KWrite
and to be as useful as them.

%description -l pl.UTF-8
Leafpad to prosty edytor tekstu oparty na GTK+. Program w założeniach
ma być lżejszy od GEdita i KWrite'a, ale tak samo użyteczny jak one.
Interfejs użytkownika jest podobny do programu "notepad".

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-chooser
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_desktopdir}/%{name}.desktop
