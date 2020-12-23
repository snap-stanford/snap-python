#!/bin/bash

#
# compiles snap.py Windows packages for python 2.7, 3.5 .. 3.9
# requirements:
#	cygwin
#       SWIG, current 4.0.2
#	Visual Studio 2019
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

# go to the working swig directory
cd $WORKDIR/snap-python/swig
mkdir -p x64/Release

# compile Python 2.7
export SNAP_PY=2.7
$WORKDIR/snap-python/scripts/build-package27-win.bat
time make whldist-win

# compile Python 3.5
export SNAP_PY=3.5
$WORKDIR/snap-python/scripts/build-package35-win.bat
time make whldist-win

# compile Python 3.6
export SNAP_PY=3.6
$WORKDIR/snap-python/scripts/build-package36-win.bat
time make whldist-win

# compile Python 3.7
export SNAP_PY=3.7
$WORKDIR/snap-python/scripts/build-package37-win.bat
time make whldist-win

# compile Python 3.8
export SNAP_PY=3.8
$WORKDIR/snap-python/scripts/build-package38-win.bat
time make whldist-win

# compile Python 3.9
export SNAP_PY=3.9
$WORKDIR/snap-python/scripts/build-package39-win.bat
time make whldist-win

