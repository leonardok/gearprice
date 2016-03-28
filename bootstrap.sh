#!/bin/bash
# bootstrap
# =========
#
# Usage:  bootstrap [environment_name]
#
# Creates a new virtualenv named environment_name, and installs all the
# runtime and devtime dependencies.
#
# If environment_name is not specified, it defaults to "filter".
#

APPNAME=photoprice
VENV=virtualenv
VENV_VERSION=1.10.1
VENV_SYS_VERSION=`virtualenv --version`
VENV_PY_URL=https://pypi.python.org/packages/source/v/virtualenv/virtualenv-${VENV_VERSION}.tar.gz

here=$(cd $(dirname $0); /bin/pwd)
venv_name=${APPNAME}
venv_dir=${VIRTUAL_ENV-$here/.venv-$venv_name}
bin_dir=$venv_dir/bin
activate=$bin_dir/activate
pip="$bin_dir/pip install -r"

die() {
    echo "$*"
    exit 1
}


echo
echo ==================================================
echo
echo Building VENV
echo

if [ -f "$activate" ]
then
    venv_name=$(basename $venv_dir)
    venv_name=${venv_name#.venv-}
else
    venv_args=" --prompt=($venv_name) $venv_dir"

    #Also make sure proper version of virtualenv is available
    if [ -n "`which $VENV`" -a "$VENV_SYS_VERSION" = "$VENV_VERSION" ]
    then
        $VENV $venv_args || die "Could not create virtualenv"
    else
        echo "Retrieving virtualenv"
        curl -Os $VENV_PY_URL || die "Could not download virtualenv"
        tar -xzf virtualenv-${VENV_VERSION}.tar.gz || die "Failed to extract virtualenv"
        python virtualenv-${VENV_VERSION}/virtualenv.py $venv_args || die "Could not create virtualenv"
        echo "Removing virtualenv"
        rm -rf virtualenv-${VENV_VERSION} virtualenv-${VENV_VERSION}.tar.gz
    fi
fi

if [ -f "requirements.txt" ]
then
	$pip $here/requirements.txt || die "Could not install main dependencies"
fi

local_link=activate-$venv_name
ln -nsf $activate $here/$local_link

echo
echo ==================================================
echo
echo Dependencies installed to:  $venv_dir
echo Activate the virtualenv by running:
echo
echo "    source $local_link"
echo 
echo Then you can run:
echo "    ./manage.py syncdb"
echo "    ./manage.py migrate"
echo 
echo


