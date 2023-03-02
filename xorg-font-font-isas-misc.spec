Summary:	ISAS bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe ISAS
Name:		xorg-font-font-isas-misc
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-isas-misc-%{version}.tar.xz
# Source0-md5:	fe2c44307639062d07c6e9f75f4d6a13
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISAS Fang song ti and Song ti Chinese bitmap fonts in hanzi guobiao
(GB2312) encoding.

%description -l pl.UTF-8
Chińskie fonty bitmapowe ISAS Fang song ti i Song ti w kodowaniu hanzi
guobiao (GB2312).

%prep
%setup -q -n font-isas-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/misc/gb*.pcf.gz
