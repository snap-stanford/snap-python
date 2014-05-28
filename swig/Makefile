#
# Makefile for SWIG processing of SNAP Python
#	Use this Makefile to compile SNAP Python from scratch
#
# Build instructions for Mac OS X and Linux:
#		make
#		make dist
# 
# Build instructions for Windows:
#	- run swig in Cygwin to generate snap_wrap.cxx and snap.py
#		make swig-win
#	- build Snappy solution in Visual Studio to generate _snap.pyd
#		- open snappy-VS12
#		- add VC++ include path for snap-core, glib-core
#		- build
#	- run setup.py in Cygwin to generate the package,
#	  NOT OVER SSH, but locally
#		make dist-win

# set the path to your SNAP directory here
GITDIR = ../../snap
SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)
SNAPADVDIR = $(GITDIR)/$(SNAPADV)

# include compilation parameters
include $(GITDIR)/Makefile.config
include ../Makefile.config

all: snap.py _snap.so

snap_wrap.cxx: snap.i snap_types.i tvec.i pneanet.i pungraph.i pngraph.i pgraph.i \
	snapswig.h snap_types.h printgraph.h goodgraph.cpp
	swig $(SWIGFLAGS) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) snap.i

snap_wrap.o: snap_wrap.cxx
	g++ $(CXXFLAGS) -c snap_wrap.cxx -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)  -I/usr/include/python2.6 -I/usr/include/python2.7

Snap.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

cliques.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/cliques.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

agm.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agm.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

agmfast.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agmfast.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

agmfit.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agmfit.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

_snap.so: snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o
	g++ $(LDFLAGS) -o _snap.so snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o $(LIBS)

snap.py: snap_wrap.cxx

install: setup.py snap.py _snap.so
	sudo python setup.py install

dist: setup.py snap.py _snap.so
	cp MANIFEST.nx MANIFEST
	python setup.py sdist

swig-win: snap_wrap.cxx

install-win: setup.py snap.py _snap.pyd
	/cygdrive/c/Python27/python.exe setup.py install

dist-win: setup.py snap.py _snap.pyd
	cp MANIFEST.win MANIFEST
	/cygdrive/c/Python27/python.exe setup.py sdist
	chmod 0644 dist/*.zip

clean:
	rm -f *.o *_wrap.cxx _*.so *.pyc snap.py _snap.*

