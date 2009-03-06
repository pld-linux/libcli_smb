# TODO:
# - reduce headers set
# - shared talloc (>= 1.1.0), tdb (>= 1.1.0), ldb (>= 0.9.1)
Summary:	libcli_smb - samba client library
Summary(pl.UTF-8):	libcli_smb - biblioteka klienta samby
Name:		libcli_smb
Version:	4.0.0
%define	subver	alpha7
Release:	0.%{subver}.1
Epoch:		1
License:	GPL v3+
Group:		Libraries
Source0:	http://us1.samba.org/samba/ftp/samba4/samba-%{version}%{subver}.tar.gz
# Source0-md5:	0c25dced4dc64a6581a09917ec05dab2
URL:		http://www.samba.org/
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gnutls-devel
BuildRequires:	libaio-devel
BuildRequires:	pam-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcli_smb - library that allows to use samba clients functions.

%description -l pl.UTF-8
libcli_smb - biblioteka pozwalająca korzystać z funcji klienta samby.

%package devel
Summary:	Header files for libcli_smb samba client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienta samby libcli_smb
Summary(pt_BR.UTF-8):	Ferramentas de desenvolvimento para clientes samba
Group:		Development/Libraries
Requires:	libcli_smb = %{epoch}:%{version}-%{release}

%description devel
Header files for libcli_smb.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcli_smb.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão necessários para desenvolver aplicativos clientes
para o samba.

%prep
%setup -q -n samba-%{version}%{subver}

%build
cd source4
./autogen.sh
%configure \
	-C \
	--enable-developer \
	--enable-socket-wrapper \
	--enable-fhs \
	--with-privatedir=%{_sysconfdir}/samba

%{__make} basics
%{__make} proto
%{__make} bin/shared/libdcerpc.so.0.0.1
%{__make} headers


%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_libdir} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/auth/{credentials,gensec} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/lib/{cmdline,events,popt,replace,smbreadline,tevent,util/charset} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/libcli/{nbt,raw,resolve,rpc,security,util} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/librpc/{gen_ndr,ndr,rpc} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/{param,system,talloc}

cp -a source4/bin/shared/libdcerpc* $RPM_BUILD_ROOT%{_libdir}
ln -sf %{_libdir}/libdcerpc.so.0.0.1 $RPM_BUILD_ROOT%{_libdir}/libdcerpc.so.0
ln -sf %{_libdir}/libdcerpc.so.0.0.1 $RPM_BUILD_ROOT%{_libdir}/libdcerpc.so

cp lib/popt/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/popt
cp lib/replace/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/replace
cp lib/replace/system/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/system
cp lib/talloc/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp lib/talloc/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/talloc
cp lib/tevent/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/tevent
cp lib/util/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/util
cp lib/util/charset/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/util/charset
cp libcli/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli
cp libcli/util/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/util
cp libcli/nbt/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/nbt
cp libcli/security/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/security
cp librpc/gen_ndr/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/librpc/gen_ndr
cp librpc/ndr/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/librpc/ndr
cp source4/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source4/auth/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth
cp source4/auth/credentials/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth/credentials
cp source4/auth/gensec/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth/gensec
cp source4/include/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source4/libcli/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source4/lib/cmdline/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/cmdline
cp source4/lib/events/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/events
cp source4/lib/ldb/include/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source4/lib/smbreadline/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/smbreadline
cp source4/libcli/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli
cp source4/libcli/libcli_proto.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli
cp source4/libcli/raw/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/raw
cp source4/libcli/resolve/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/resolve
cp source4/libcli/security/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/security
cp source4/libcli/util/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/util
cp source4/librpc/gen_ndr/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/librpc/gen_ndr
cp source4/librpc/rpc/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/librpc/rpc
cp source4/param/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source4/param/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/param

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdcerpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libdcerpc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdcerpc.so
%{_includedir}/samba4
