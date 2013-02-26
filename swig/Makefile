#
# Makefile for SWIG processing of SNAP
#

GITDIR = ../../snap
include $(GITDIR)/Makefile.config

SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
  # Linux flags
  CXXFLAGS += -fPIC -shared -D__STDC_LIMIT_MACROS
  LDFLAGS += -lrt
else ifeq ($(UNAME), Darwin)
  # OS X flags
  LDFLAGS += -lpython -dynamiclib
else ifeq ($(shell uname -o), Cygwin)
  # Cygwin flags
endif

#SWIGFILES = getassessment.cpp

all: python

python: Snap.o snap.i
	swig -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -D_CMPWARN -I$(SNAPDIR) -I$(GLIBDIR) snap.i
	g++ $(CXXFLAGS) -c snap_wrap.cxx $(SWIGFILES) -I$(SNAPDIR) -I$(GLIBDIR) -I/usr/include/python2.6 -I/usr/include/python2.7
	g++ $(LDFLAGS) $(CXXFLAGS) snap_wrap.o Snap.o -o _snap.so

Snap.o: 
	$(CC) -c $(CXXFLAGS) $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(GLIBDIR)

clean:
	rm -f *.o *_wrap.cxx _*.so *.pyc

