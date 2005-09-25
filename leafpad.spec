Summary:	GTK+2 based notepad clone
Summary(pl):	Klon notepada oparty na GTK+
Name:		leafpad
Version:	0.8.4
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
# Source0-md5:	bf7ceee550932d8550b515ef9d59c739
Patch0:		%{name}-desktop.patch
URL:		http://tarot.freeshell.org/leafpad/
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leafpad is a simple GTK+ based text editor. The user interface is
similar to "notepad", and it aims to be lighter than GEdit and KWrite
and to be as useful as them.

%description -l pl
Leafpad to prosty edytor tekstu oparty na GTK+. Program w za³o¿eniach
ma byæ l¿ejszy od GEdita i KWrite'a, ale tak samo u¿yteczny jak one.
Interfejs u¿ytkownika jest podobny do programu "notepad".

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
%{_desktopdir}/*
