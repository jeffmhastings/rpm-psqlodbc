Summary: A complete ODBC driver manager for Linux
Name: psqlodbc95
Version: %{?version}%{!?version:09.05.0100}
Release: 1%{?dist}
Group: System Environment/Libraries
URL: https://odbc.postgresql.org/
License: LGPLv2+

Source: https://ftp.postgresql.org/pub/odbc/versions/src/psqlodbc-%{version}.tar.gz

Conflicts: postgresql-odbc postgresql95-odbc psqlodbc
BuildRequires: automake autoconf libtool postgresql95-devel
BuildRequires: unixODBC-devel >= 2.3.4-1
Requires: unixODBC >= 2.3.4-1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package installs the PostgreSQL ODBC library

%prep
%setup -q

%build
%configure --enable-pthreads --with-libpq=/usr/pgsql-9.5 --with-unixodbc=/usr/bin/odbc_config
make all

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%make_install

# Remove unpackaged files
rm -f %{buildroot}%{_libdir}/*.la

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/psqlodbcw.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
