Summary:	GTK+2 based notepad clone
Summary(pl):	Klon notepada oparty na GTK+
Name:		leafpad
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://tarot.freeshell.org/leafpad/%{name}-%{version}.tar.gz
# Source0-md5:	3aa3495d6071b1b2c049f0d52f35afe5
Source1:	%{name}.desktop
URL:		http://tarot.freeshell.org/leafpad/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leafpad is a simple GTK+ based text editor. The user interface is
similar to "notepad", and it aims to be lighter than GEdit and KWrite
and to be as useful as them.

%description -l pl
Leafpad to prosty edytor tekstu oparty na GTK+. Program w za�o�eniach
ma by� l�ejszy od GEdita i KWrite'a, ale tak samo u�yteczny jak one.
Interfejs u�ytkownika jest podobny do programu "notepad".

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
