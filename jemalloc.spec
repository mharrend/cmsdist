### RPM external jemalloc 4.2.0
Source: http://www.canonware.com/download/jemalloc/jemalloc-%realversion.tar.bz2 

%prep
%setup -n %n-%{realversion}

%build
perl -p -i -e 's|-no-cpp-precomp||' configure
./configure --disable-stats --prefix %i

%define drop_files %i/share
