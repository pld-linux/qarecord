Summary:	Simple stereo recording tool
Summary(pl):	Proste narzêdzie do nagrywania w stereo
Name:		qarecord
Version:	0.0.9
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	ftp://ftp.suse.com/pub/people/mana/%{name}-%{version}.tar.bz2
# Source0-md5:	30412e77424d79870a886fbde429e5b3
Source1:	%{name}.desktop
Patch0:		%{name}-paths_and_optflags.patch
URL:		http://www.suse.de/~mana/kalsatools.html
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QARecord is a simple stereo recording tool. It can record both 16 bit
and 32 bit WAVs. Can also be used as JACK client.

%description -l pl
QARecord jest prostym narzêdziem do nagrywania stereo. Mo¿e nagrywaæ
pliki WAV w rozdzielczo¶ci 16 bit i 32 bit. Mo¿e byæ tak¿e u¿yty jako
klient JACKa.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	-f make_qarecord \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -c qarecord $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
