### RPM external sherpa 2.2.1
%define tag bc0ccbfdf07f4df4f0368106aa9c793bb61e1def
%define branch cms/v%realversion
%define github_user cms-externals
Source: git+https://github.com/%github_user/%{n}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz
Requires: hepmc lhapdf blackhat sqlite fastjet openssl scons python
BuildRequires: mcfm swig

%if "%(case %cmsplatf in (slc*) echo true ;; (*) echo false ;; esac)" == "true"
Requires: openloops
%endif

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%if "%{?cms_cxxflags:set}" != "set"
%define cms_cxxflags -O2 -std=c++0x
%endif

%prep
%setup -q -n %{n}-%{realversion}

autoreconf -i --force

# Force architecture based on %%cmsplatf
case %cmsplatf in
  *_amd64_gcc*) ARCH_CMSPLATF="-m64" ;;
esac

case %cmsplatf in
  osx*)
    perl -p -i -e 's|-rdynamic||g' \
      configure \
      AddOns/Analysis/Scripts/Makefile.in
  ;;
esac

%build
./configure --prefix=%i --enable-analysis --disable-silent-rules \
            --enable-fastjet=$FASTJET_ROOT \
            --enable-mcfm=$MCFM_ROOT \
            --enable-hepmc2=$HEPMC_ROOT \
            --enable-lhapdf=$LHAPDF_ROOT \
            --enable-blackhat=$BLACKHAT_ROOT \
            --enable-pyext \
            --enable-ufo \
            ${OPENLOOPS_ROOT+--enable-openloops=$OPENLOOPS_ROOT}\
            --with-sqlite3=$SQLITE_ROOT \
            CXX="%cms_cxx" \
            CXXFLAGS="-fuse-cxa-atexit $ARCH_CMSPLATF %cms_cxxflags -I$LHAPDF_ROOT/include -I$BLACKHAT_ROOT/include -I$OPENSSL_ROOT/include" \
            LDFLAGS="-ldl -L$BLACKHAT_ROOT/lib/blackhat -L$QD_ROOT/lib -L$OPENSSL_ROOT/lib"

make %{makeprocesses}

%install
make install
find %{i}/lib -name '*.la' -delete
sed -i -e 's|^#!/.*|#!/usr/bin/env python|' %{i}/bin/Sherpa-generate-model

%post
%{relocateConfig}lib/python2.7/site-packages/ufo_interface/sconstruct_template
%{relocateConfig}bin/make2scons
%{relocateConfig}share/SHERPA-MC/makelibs
%{relocateConfig}bin/Sherpa-config
%{relocateConfig}bin/Sherpa-generate-model
%{relocateConfig}include/SHERPA-MC/ATOOLS/Org/CXXFLAGS.H
