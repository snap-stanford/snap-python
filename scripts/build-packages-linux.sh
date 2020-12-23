#!/bin/bash

# go to the working swig directory
cd /src/snap-python/swig

# compile Python 2.7m
export SNAP_PY=2.7m
make clean-obj
time make whldist

# compile Python 2.7mu
export SNAP_PY=2.7mu
make clean-obj
time make whldist

# compile Python 3.5
export SNAP_PY=3.5
make clean-obj
time make whldist3

# compile Python 3.6
export SNAP_PY=3.6
make clean-obj
time make whldist3

# compile Python 3.7
export SNAP_PY=3.7
make clean-obj
time make whldist3

# compile Python 3.8
export SNAP_PY=3.8
make clean-obj
time make whldist3

# compile Python 3.9
export SNAP_PY=3.9
make clean-obj
time make whldist3

