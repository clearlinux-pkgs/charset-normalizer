#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : charset-normalizer
Version  : 2.0.7
Release  : 7
URL      : https://files.pythonhosted.org/packages/9f/c5/334c019f92c26e59637bb42bd14a190428874b2b2de75a355da394cf16c1/charset-normalizer-2.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/c5/334c019f92c26e59637bb42bd14a190428874b2b2de75a355da394cf16c1/charset-normalizer-2.0.7.tar.gz
Summary  : The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
Group    : Development/Tools
License  : MIT
Requires: charset-normalizer-bin = %{version}-%{release}
Requires: charset-normalizer-license = %{version}-%{release}
Requires: charset-normalizer-python = %{version}-%{release}
Requires: charset-normalizer-python3 = %{version}-%{release}
Requires: unicodedata2
BuildRequires : buildreq-distutils3
BuildRequires : unicodedata2

%description
<h1 align="center">Charset Detection, for Everyone 👋 <a href="https://twitter.com/intent/tweet?text=The%20Real%20First%20Universal%20Charset%20%26%20Language%20Detector&url=https://www.github.com/Ousret/charset_normalizer&hashtags=python,encoding,chardet,developers"><img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"/></a></h1>

%package bin
Summary: bin components for the charset-normalizer package.
Group: Binaries
Requires: charset-normalizer-license = %{version}-%{release}

%description bin
bin components for the charset-normalizer package.


%package license
Summary: license components for the charset-normalizer package.
Group: Default

%description license
license components for the charset-normalizer package.


%package python
Summary: python components for the charset-normalizer package.
Group: Default
Requires: charset-normalizer-python3 = %{version}-%{release}

%description python
python components for the charset-normalizer package.


%package python3
Summary: python3 components for the charset-normalizer package.
Group: Default
Requires: python3-core
Provides: pypi(charset_normalizer)

%description python3
python3 components for the charset-normalizer package.


%prep
%setup -q -n charset-normalizer-2.0.7
cd %{_builddir}/charset-normalizer-2.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634003833
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/charset-normalizer
cp %{_builddir}/charset-normalizer-2.0.7/LICENSE %{buildroot}/usr/share/package-licenses/charset-normalizer/753eb879a99db2b65e384b3c1baec552b6134f26
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/normalizer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/charset-normalizer/753eb879a99db2b65e384b3c1baec552b6134f26

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
