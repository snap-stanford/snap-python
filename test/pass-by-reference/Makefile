
#
# Small makefile for testing with non-Microsoft compilers
#

include ./Makefile.config

all: Snap.o snap.py _snap.so

Snap.o: *.h 
	$(CC) -c $(CXXFLAGS) Snap.cpp -I$(CGLIB)

lib: Snap.o
	rm -f libsnap.a
	ar -cvq libsnap.a Snap.o

libinstall: lib
	cp libsnap.a /usr/local/lib/libsnap.a

clean:
	rm -f *.o *.a testSnap testSnap.exe *.plt *.tab *.png *.o *_wrap.cxx _*.so *.pyc snap.py _snap.*

include ./Makefile-python.config

GITDIR = .
SNAPDIR = .
GLIBDIR = .
SNAPADVDIR = .

snap_wrap.cxx: snap.i snap_types.i  
	swig $(SWIGFLAGS) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) snap.i

snap_wrap.o: snap_wrap.cxx
	g++ $(CXXFLAGS) -c snap_wrap.cxx -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR)  -I/usr/include/python2.6 -I/usr/include/python2.7

_snap.so: snap_wrap.o Snap.o
	g++ $(LDFLAGS) -o _snap.so snap_wrap.o Snap.o $(LIBS)

snap.py: snap_wrap.cxx

