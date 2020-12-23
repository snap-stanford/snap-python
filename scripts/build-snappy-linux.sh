#!/bin/bash

#
# compiles snap.py Linux packages for python 2.7, 3.5 .. 3.9
# requirements:
#	SWIG, current 4.0.2
#	docker
#	quay.io/pypa/manylinux1_x86_64 (docker container)
#

export WORKDIR=$HOME/build

mkdir -p $WORKDIR
cd $WORKDIR

# get a fresh copy of SNAP repositories, rename any existing repositories
mv -f snap snap.bak
mv -f snap-python snap-python.bak
git clone git@github.com:snap-stanford/snap.git
git clone git@github.com:snap-stanford/snap-python.git

# run SWIG, it is required only once
cd $WORKDIR/snap-python/swig
make snap_wrap3.cxx

# compile the extensions and build all the wheels
docker run -it -v $WORKDIR:/src --user "$(id -u):$(id -g)" quay.io/pypa/manylinux1_x86_64 /src/snap-python/scripts/build-packages-linux.sh

