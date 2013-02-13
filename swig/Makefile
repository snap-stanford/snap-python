#
# Makefile for SWIG processing of SNAP
#

GITDIR = ../../snap-sw
include $(GITDIR)/Makefile.config

SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
  # Linux flags
  CXXFLAGS += -fPIC -shared -D__STDC_LIMIT_MACROS
else ifeq ($(UNAME), Darwin)
  # OS X flags
else ifeq ($(shell uname -o), Cygwin)
  # Cygwin flags
endif

all: python

python: Snap.o snap.i
	swig -python -c++ -O -D_CMPWARN -I$(SNAPDIR) -I$(GLIBDIR) snap.i
	g++ $(CXXFLAGS) -c snap_wrap.cxx -I/usr/include/python2.6 -I$(SNAPDIR) -I$(GLIBDIR)
	g++ $(CXXFLAGS) snap_wrap.o Snap.o -lrt -o _snap.so

Snap.o: 
	$(CC) -c $(CXXFLAGS) $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(GLIBDIR)

clean:
	rm -f *.o *_wrap.cxx _*.so *.pyc

