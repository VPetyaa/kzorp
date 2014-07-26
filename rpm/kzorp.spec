Name:			kzorp
Version:		0.1.3
Release:		1
URL:			https://www.balabit.com/network-security/zorp-gpl
Source0:		%{name}_%{version}ubuntu5.tar.gz
#Patch0:			createdir.patch
Summary:		BalaBit Zorp proxy firewall kernel module
License:		GPL-2.0
Group:			System/Daemons
BuildRequires:		automake
BuildRequires:		autoconf
BuildRequires:		gcc-c++
BuildRequires:		python
BuildRequires:		libtool

%if 0%{?fedora} || 0%{?centos}
BuildRequires:		kernel-devel
BuildRequires:		kernel-headers
%else
BuildRequires:		linux-glibc-devel
BuildRequires:		dh-autoreconf
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BalaBit Zorp proxy firewall kernel module

Summary:		Headers for libzorpll
Group:			System/Daemons
Requires:		%{name} = %{version}

%prep
%setup -q -n kzorp
# %patch0 -p1

%build
autoreconf -i
#%{?suse_update_config:%{suse_update_config -f config}}
%configure --disable-werror --enable-debug

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%post
ldconfig

%postun
ldconfig

%files
%dir %attr(755,root,root)/usr/src/kzorp-0.1.3
%attr(755,root,root) /usr/lib/python2.7/site-packages/*
%attr(755,root,root) /usr/sbin/kzorp-client
%attr(755,root,root) /usr/src/kzorp-0.1.3/*

%changelog
