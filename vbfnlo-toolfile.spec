### RPM external vbfnlo-toolfile 1.0
Requires: vbfnlo
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/vbfnlo.xml
<tool name="vbfnlo" version="@TOOL_VERSION@">
  <lib name="VBFNLO"/>
  <client>
    <environment name="VBFNLO_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$VBFNLO_BASE/lib"/>
    <environment name="INCLUDE" default="$VBFNLO_BASE/include"/>
  </client>
  <runtime name="ROOT_INCLUDE_PATH" value="$INCLUDE" type="path"/>
  <use name="root_cxxdefaults"/>
  <use name="lhapdf"/>
  <use name="gsl"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post

