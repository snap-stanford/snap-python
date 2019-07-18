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
#		- open ~/build/snap-python/swig/snappy-VS12
#		- add VC++ include path for snap-core, glib-core, snap-adv,
#		  or 'subst S: <path_to_snap>':
#			  subst s: /cygwin/home/rok/build/snap
#		- build
#	- run setup.py in Cygwin to generate the package,
#	  NOT OVER SSH, but locally
#		make dist-win

# set the path to your SNAP directory here
#GITDIR = ../../snap
GITDIR = ../../snap
SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)
#SNAPADVDIR = $(GITDIR)/$(SNAPADV)
SNAPEXPDIR = $(GITDIR)/$(SNAPEXP)

# include compilation parameters
include $(GITDIR)/Makefile.config
include ../Makefile.config

all: snap.py _snap.so

all3: snap3.py _snap3.so

snap.py: snap_wrap.cxx

snap3.py: snap_wrap3.cxx

_snap.so: snap_wrap.o Snap.o 
	g++ $(LDFLAGS) -o _snap.so snap_wrap.o Snap.o  $(LIBS)

_snap3.so: snap_wrap3.o Snap.o 
	g++ $(LDFLAGS3) -o _snap.so snap_wrap3.o Snap.o  $(LIBS)
	ln -f _snap.so _snap3.so

snap_wrap.cxx: snap.i snap_types.i tvec.i pneanet.i tmodenet.i tcrossnet.i pungraph.i pngraph.i pgraph.i pngraphmp.i pneanetmp.i\
	snapswig.h snap_types.h printgraph.h goodgraph.cpp
	swig $(SWIGFLAGS) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) snap.i

snap_wrap3.cxx: snap.i snap_types.i tvec.i pneanet.i tmodenet.i tcrossnet.i pungraph.i pngraph.i pgraph.i pngraphmp.i pneanetmp.i\
	snapswig.h snap_types.h printgraph.h goodgraph.cpp
	swig $(SWIGFLAGS3) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(GLIBDIR) snap.i
	ln -f snap_wrap.cxx snap_wrap3.cxx

snap_wrap.o: snap_wrap.cxx
	g++ $(CXXFLAGS) -c snap_wrap.cxx -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -I/usr/include/python2.6 -I/usr/include/python2.7 -I/usr/lib/python2.7/dist-packages/numpy/core/include -I/usr/lib/python2.7/dist-packages/numpy/core/include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/ -I/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/numpy/core/include 

snap_wrap3.o: snap_wrap3.cxx
	g++ $(CXXFLAGS) -c snap_wrap3.cxx -I$(SNAPDIR)  -I$(GLIBDIR) -I/usr/local/include/python3.6m -I/usr/include/python3.6m -I/usr/local/Frameworks/Python.framework/Versions/3.7/include/python3.7m -I/usr/local/Frameworks/Python.framework/Versions/3.7/Headers/Python.h -o snap_wrap.o

	ln -f snap_wrap.o snap_wrap3.o

Snap.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(GLIBDIR)

cliques.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/cliques.cpp -I$(SNAPDIR) -I$(GLIBDIR)

agm.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agm.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

agmfast.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agmfast.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

agmfit.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/agmfit.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

biasedrandomwalk.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/biasedrandomwalk.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

word2vec.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/word2vec.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

n2v.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPADVDIR)/n2v.cpp -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)

#_snap.so: snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o biasedrandomwalk.o word2vec.o n2v.o
#	g++ $(LDFLAGS) -o _snap.so snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o biasedrandomwalk.o word2vec.o n2v.o $(LIBS)

#_snap3.so: snap_wrap3.o Snap.o 
#	g++ $(LDFLAGS3) -o _snap3.so snap_wrap3.o Snap.o $(LIBS)

snap.py: snap_wrap.cxx

install: setup.py snap.py _snap.so
	sudo python setup.py install

dist: setup.py snap.py _snap.so
	cp $(MANIFEST) MANIFEST
	python setup.py sdist

dist3: setup.py snap3.py _snap3.so
	cp _snap3.so _snap.so
	cp $(MANIFEST) MANIFEST
	python3 setup.py sdist

swig-win: snap_wrap.cxx

install-win: setup.py snap.py _snap.pyd
	/cygdrive/c/Python27/python.exe setup.py install

dist-win: setup.py snap.py _snap.pyd
	cp $(MANIFEST) MANIFEST
	/cygdrive/c/Python27/python.exe setup.py sdist
	chmod 0644 dist/*.zip

clean:
	rm -f *.o *_wrap*.cxx _*.so *.pyc snap*.py _snap*.*

pip: dist/*
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
