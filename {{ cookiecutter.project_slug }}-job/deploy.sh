#!/bin/bash
VERSION="{{ cookiecutter.version }}"

PY_RUN="{{ cookiecutter.project_name }}_run.py"
WHEEL="{{ cookiecutter.project_name }}-$VERSION-py3-none-any.whl"
LOCAL_WHEEL="dist/$WHEEL"
LIBRARY="dbfs:/libraries/wheels/{{ cookiecutter.project_name }}/$WHEEL"
PY_SCRIPT="dbfs:/python/scripts/$PY_RUN"

conf=`cat << EOM
$DATABRICKS_HOST
$DATABRICKS_TOKEN0
EOM`

echo "$conf" | databricks configure --token
echo "Removing...$LIBRARY"
eval "dbfs rm $LIBRARY"
echo "Copying $LOCAL_WHEEL to dbfs"
eval "dbfs cp $LOCAL_WHEEL $LIBRARY"
echo "Removing...$PY_SCRIPT"
eval "dbfs rm $PY_SCRIPT"
echo "Copying $PY_RUN to dbfs"
eval "dbfs cp $PY_RUN $PY_SCRIPT"