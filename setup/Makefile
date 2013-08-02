#
# Makefile for compilation of SNAP Python from SWIG output
# 

SNAPVER = 2.x

# set the path to your SNAP directory here
#GITDIR = ../Snap-$(SNAPVER)
GITDIR = ../snap
SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)

SWIGDIR = ../swig

# include compilation parameters
include $(GITDIR)/Makefile.config
include ../Makefile.config

all: _snap.so

snap_wrap.o: snap_wrap.cxx
	@if ! diff Version $(GITDIR)/Version >/dev/null ; then echo "*** Error: SNAP versions do not match"; exit 1; fi
	g++ $(CXXFLAGS) -c snap_wrap.cxx -I$(SWIGDIR) -I$(SNAPDIR) -I$(GLIBDIR)  -I/usr/include/python2.6 -I/usr/include/python2.7

Snap.o: 
	@if ! diff Version $(GITDIR)/Version >/dev/null ; then echo "*** Error: SNAP versions do not match"; exit 1; fi
	$(CC) $(CXXFLAGS) -c $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(GLIBDIR)

_snap.so: snap_wrap.o Snap.o
	g++ $(LDFLAGS) $(CXXFLAGS) snap_wrap.o Snap.o $(LIBS) -o _snap.so

snap.py: snap_wrap.cxx

install: setup.py snap.py _snap.so
	sudo python setup.py install

dist: setup.py snap.py _snap.so
	python setup.py sdist

build:
	swig -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -D_CMPWARN -outcurrentdir -I$(SWIGDIR) -I$(SNAPDIR) -I$(GLIBDIR) $(SWIGDIR)/snap.i
	cp $(GITDIR)/Version .

clean:
	rm -f *.o _*.so *.pyc

