#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : speex
Version  : 1.2.1
Release  : 30
URL      : https://ftp.osuosl.org/pub/xiph/releases/speex/speex-1.2.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/xiph/releases/speex/speex-1.2.1.tar.gz
Summary  : An open-source, patent-free speech codec
Group    : Development/Tools
License  : BSD-3-Clause
Requires: speex-bin = %{version}-%{release}
Requires: speex-filemap = %{version}-%{release}
Requires: speex-lib = %{version}-%{release}
Requires: speex-license = %{version}-%{release}
Requires: speex-man = %{version}-%{release}
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : speexdsp-dev

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package bin
Summary: bin components for the speex package.
Group: Binaries
Requires: speex-license = %{version}-%{release}
Requires: speex-filemap = %{version}-%{release}

%description bin
bin components for the speex package.


%package dev
Summary: dev components for the speex package.
Group: Development
Requires: speex-lib = %{version}-%{release}
Requires: speex-bin = %{version}-%{release}
Provides: speex-devel = %{version}-%{release}
Requires: speex = %{version}-%{release}

%description dev
dev components for the speex package.


%package doc
Summary: doc components for the speex package.
Group: Documentation
Requires: speex-man = %{version}-%{release}

%description doc
doc components for the speex package.


%package filemap
Summary: filemap components for the speex package.
Group: Default

%description filemap
filemap components for the speex package.


%package lib
Summary: lib components for the speex package.
Group: Libraries
Requires: speex-license = %{version}-%{release}
Requires: speex-filemap = %{version}-%{release}

%description lib
lib components for the speex package.


%package license
Summary: license components for the speex package.
Group: Default

%description license
license components for the speex package.


%package man
Summary: man components for the speex package.
Group: Default

%description man
man components for the speex package.


%prep
%setup -q -n speex-1.2.1
cd %{_builddir}/speex-1.2.1
pushd ..
cp -a speex-1.2.1 buildavx2
popd
pushd ..
cp -a speex-1.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656515527
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -ftree-loop-vectorize -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -ftree-loop-vectorize -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -ftree-loop-vectorize -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffast-math -ffat-lto-objects -flto=auto -fno-semantic-interposition -ftree-loop-vectorize -mprefer-vector-width=256 "
%configure --disable-static --enable-sse
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-sse
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static --enable-sse
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656515527
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/speex
cp %{_builddir}/speex-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/speex/fc3b9b42abbb2f2b795ad9598708f3db0b3e9ae7
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/speexdec
/usr/bin/speexenc
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/speex/speex.h
/usr/include/speex/speex_bits.h
/usr/include/speex/speex_callbacks.h
/usr/include/speex/speex_config_types.h
/usr/include/speex/speex_header.h
/usr/include/speex/speex_stereo.h
/usr/include/speex/speex_types.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libspeex.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libspeex.so
/usr/lib64/libspeex.so
/usr/lib64/pkgconfig/speex.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/speex/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-speex

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libspeex.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libspeex.so.1.5.2
/usr/lib64/glibc-hwcaps/x86-64-v4/libspeex.so.1
/usr/lib64/glibc-hwcaps/x86-64-v4/libspeex.so.1.5.2
/usr/lib64/libspeex.so.1
/usr/lib64/libspeex.so.1.5.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/speex/fc3b9b42abbb2f2b795ad9598708f3db0b3e9ae7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/speexdec.1
/usr/share/man/man1/speexenc.1
