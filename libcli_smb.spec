
Summary:	libcli_smb - samba client library
Summary(pl.UTF-8):	libcli_smb - biblioteka klienta samby
Name:		libcli_smb
Version:	4.0.0
Release:	0.alpha1.1
Epoch:		1
License:	GPL v3
Group:		Libraries
Source0:	http://us1.samba.org/samba/ftp/samba4/samba-4.0.0alpha1.tar.gz
# Source0-md5:	a72ddbc13bf2c95e303a2e609e8161b0
URL:		http://www.samba.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcli_smb - library that allows to use samba clients functions.

%description -l pl.UTF-8
libcli_smb - biblioteka pozwalająca korzystać z funcji klienta
samby.

%package devel
Summary:	libcli_smb - samba client library
Summary(pl.UTF-8):	libcli_smb - biblioteka klienta samby
Summary(pt_BR.UTF-8):	Ferramentas de desenvolvimento para clientes samba
Group:		Development/Libraries
Requires:	libcli_smb = %{epoch}:%{version}-%{release}

%description devel
Header files for libcli_smb.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libcli_smb.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão, bibliotecas e documentação necessários para
desenvolver aplicativos clientes para o samba.

%prep
%setup -q -n samba-4.0.0alpha1

%build
cd source
%configure \
	 -C \
	--enable-developer \
	--enable-socket-wrapper \
	--with-privatedir=%{_sysconfdir}/samba
	                 
%{__make} proto
%{__make} bin/shared/libcli_smb.so.0.0.1
%{__make} headers

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_libdir} \
	$RPM_BUILD_ROOT%{_includedir}/samba4/auth/credentials \
	$RPM_BUILD_ROOT%{_includedir}/samba4/auth/gensec \
	$RPM_BUILD_ROOT%{_includedir}/samba4/lib/charset \
	$RPM_BUILD_ROOT%{_includedir}/samba4/system \
	$RPM_BUILD_ROOT%{_includedir}/samba4/lib/util \
	$RPM_BUILD_ROOT%{_includedir}/samba4/lib/replace \
	$RPM_BUILD_ROOT%{_includedir}/samba4/libcli/raw \
	$RPM_BUILD_ROOT%{_includedir}/samba4/libcli/util \
	$RPM_BUILD_ROOT%{_includedir}/samba4/librpc/gen_ndr \
	$RPM_BUILD_ROOT%{_includedir}/samba4/param

cp -a source/bin/shared/libcli_smb* $RPM_BUILD_ROOT%{_libdir}

cp source/include/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source/libcli/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source/param/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source/auth/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth
cp source/auth/gensec/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth/gensec
cp source/auth/credentials/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/auth/credentials
cp source/lib/charset/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/charset
cp source/lib/ldb/include/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source/lib/replace/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/replace
cp source/lib/replace/system/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/system
cp source/lib/talloc/*.h $RPM_BUILD_ROOT%{_includedir}/samba4
cp source/lib/util/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/lib/util
cp source/libcli/libcli_proto.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli
cp source/libcli/raw/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/raw
cp source/libcli/util/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/libcli/util
cp source/librpc/gen_ndr/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/librpc/gen_ndr
cp source/param/*.h $RPM_BUILD_ROOT%{_includedir}/samba4/param

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcli_smb.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcli_smb.so
%{_includedir}