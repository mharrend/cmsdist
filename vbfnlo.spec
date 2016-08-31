### RPM external vbfnlo 3.0.0beta2

# Download from official webpage
Source: https://www.itp.kit.edu/vbfnlo/wiki/lib/exe/fetch.php?media=download:vbfnlo-%{realversion}.tgz 

Requires: lhapdf
Requires: gsl
Requires: hepmc
Requires: root

%define keep_archives true

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx c++
%endif


%prep
%setup -q -n VBFNLO-%{realversion}


%build
CXX="$(which %{cms_cxx}) -fPIC"
CC="$(which gcc) -fPIC"
FC="$(which gfortran)"
PLATF_CONF_OPTS="--enable-shared=no"


./configure $PLATF_CONF_OPTS \
            --with-lhapdf=$LHAPDF_ROOT \
            --with-hepmc=$HEPMC_ROOT \
            --with-gsl=$GSL_ROOT \
	    --with-root=$ROOT_ROOT \
            --prefix=%{i} \
            CXX="$CXX" CC="$CC" FC="$FC"  \
	    --enable-kk \
  	    --enable-quad \
            --enable-processes=all



make %{makeprocesses}

%install
make install
