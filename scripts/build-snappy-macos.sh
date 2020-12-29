#!/bin/bash

#
# compiles snap.py Windows packages for python 2.7, 3.5 .. 3.9
# requirements:
#       SWIG, current 4.0.2
#	pyenv
#
export WORKDIR=$HOME/build

mkdir -p $WORKDIR
cd $WORKDIR

# get a fresh copy of SNAP repositories, rename any existing repositories
rm -rf snap.bak snap-python.bak
mv -f snap snap.bak
mv -f snap-python snap-python.bak
git clone git@github.com:snap-stanford/snap.git
git clone git@github.com:snap-stanford/snap-python.git

# run SWIG, it is required only once
cd $WORKDIR/snap-python/swig
make snap_wrap3.cxx

# compile Python 2.7
export SNAP_PY=2.7
pyenv global 2.7.18
make clean-obj
time make whldist

# compile Python 3.5
export SNAP_PY=3.5
pyenv global 3.5.10
make clean-obj
time make whldist3

# compile Python 3.6
export SNAP_PY=3.6
pyenv global 3.6.12
make clean-obj
time make whldist3

# compile Python 3.7
export SNAP_PY=3.7
pyenv global 3.7.9
make clean-obj
time make whldist3

# compile Python 3.8
export SNAP_PY=3.8
pyenv global 3.8.6
make clean-obj
time make whldist3

# compile Python 3.9
export SNAP_PY=3.9
pyenv global 3.9.0
make clean-obj
time make whldist3

