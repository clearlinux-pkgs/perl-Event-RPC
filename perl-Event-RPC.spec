#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Event-RPC
Version  : 1.10
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/J/JR/JRED/Event-RPC-1.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JR/JRED/Event-RPC-1.10.tar.gz
Source1  : http://cdn-fastly.deb.debian.org/debian/pool/main/libe/libevent-rpc-perl/libevent-rpc-perl_1.10-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Event-RPC-license = %{version}-%{release}
Requires: perl-Event-RPC-perl = %{version}-%{release}
Requires: perl(CBOR::XS)
Requires: perl(Sereal)
BuildRequires : buildreq-cpan
BuildRequires : perl(AnyEvent)
BuildRequires : perl(Sereal)

%description
NAME
Event::RPC - Event based transparent Client/Server RPC framework
SYNOPSIS
#-- Server Code
use Event::RPC::Server;
use My::TestModule;
my $server = Event::RPC::Server->new (
port    => 5555,
classes => { "My::TestModule" => { ... } },
);
$server->start;

%package dev
Summary: dev components for the perl-Event-RPC package.
Group: Development
Provides: perl-Event-RPC-devel = %{version}-%{release}
Requires: perl-Event-RPC = %{version}-%{release}

%description dev
dev components for the perl-Event-RPC package.


%package license
Summary: license components for the perl-Event-RPC package.
Group: Default

%description license
license components for the perl-Event-RPC package.


%package perl
Summary: perl components for the perl-Event-RPC package.
Group: Default
Requires: perl-Event-RPC = %{version}-%{release}

%description perl
perl components for the perl-Event-RPC package.


%prep
%setup -q -n Event-RPC-1.10
cd %{_builddir}
tar xf %{_sourcedir}/libevent-rpc-perl_1.10-1.debian.tar.xz
cd %{_builddir}/Event-RPC-1.10
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Event-RPC-1.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Event-RPC
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Event-RPC/8d40e13044547a6933a93ee41a53ce9cf9f90e42
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Event::RPC.3
/usr/share/man/man3/Event::RPC::Client.3
/usr/share/man/man3/Event::RPC::Connection.3
/usr/share/man/man3/Event::RPC::LogConnection.3
/usr/share/man/man3/Event::RPC::Logger.3
/usr/share/man/man3/Event::RPC::Loop.3
/usr/share/man/man3/Event::RPC::Loop::AnyEvent.3
/usr/share/man/man3/Event::RPC::Loop::Event.3
/usr/share/man/man3/Event::RPC::Loop::Glib.3
/usr/share/man/man3/Event::RPC::Message.3
/usr/share/man/man3/Event::RPC::Message::CBOR.3
/usr/share/man/man3/Event::RPC::Message::JSON.3
/usr/share/man/man3/Event::RPC::Message::Negotiate.3
/usr/share/man/man3/Event::RPC::Message::Sereal.3
/usr/share/man/man3/Event::RPC::Message::SerialiserBase.3
/usr/share/man/man3/Event::RPC::Message::Storable.3
/usr/share/man/man3/Event::RPC::Server.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Event-RPC/8d40e13044547a6933a93ee41a53ce9cf9f90e42

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/AuthPasswdHash.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Client.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Connection.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/LogConnection.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Logger.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Loop.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Loop/AnyEvent.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Loop/Event.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Loop/Glib.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/CBOR.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/JSON.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/Negotiate.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/Sereal.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/SerialiserBase.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Message/Storable.pm
/usr/lib/perl5/vendor_perl/5.34.0/Event/RPC/Server.pm
