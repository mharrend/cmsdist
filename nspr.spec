### RPM external nspr 4.9.5
Source: https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%{realversion}/src/%{n}-%{realversion}.tar.gz
%define strip_files %{i}/lib

%define isamd64 %(case %{cmsplatf} in (*amd64*) echo 1 ;; (*) echo 0 ;; esac)

%build
pushd mozilla/nsprpub
CONF_OPTS="--disable-static --prefix=%{i} --build=%{_build} --host=%{_host}"
%if %isamd64
CONF_OPTS="${CONF_OPTS} --enable-64bit"
%endif

./configure ${CONF_OPTS}
make %{makeprocesses}
popd

%install
pushd mozilla/nsprpub
make install
popd
