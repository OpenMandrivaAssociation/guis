%define name	guis
%define version 1.6
%define release %mkrel 8

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	GUI widget server
Group:		Publishing
URL:		http://starynkevitch.net/Basile/guisdoc.html
Source:		http://starynkevitch.net/Basile/%{name}-%{version}.tar.bz2
Patch:		%{name}-1.5.configure.patch
BuildRequires:	ruby-gnome2-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	hevea
BuildRequires:  ruby-devel
BuildRequires:  tetex-latex
BuildRequires:  tetex-dvips
BuildRequires:  ghostscript-dvipdf
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
Guis widget server is a Gtk2 widget server. It listens on pipes for widget
requests (in the Python or Ruby scripting languages), and emit replies or
events in textual lines (e.g. Lispy, XML or plain token syntax). It is useful
for programs (in particular setuid programs) and scripts that don't or can't
link the Gtk2 libraries and need to delegate the user interface to another
process.

%prep
%setup -q
%patch

%build
./Configure
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
%make PREFIX=%{buildroot}%{_prefix} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README guisdoc.html guisdoc.ps guisdoc.pdf
%{_bindir}/*
%{_mandir}/man1/*


