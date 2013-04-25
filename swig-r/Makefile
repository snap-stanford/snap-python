#
# Makefile for SWIG processing of SNAP
# 

# set the path to your SNAP directory here
GITDIR = ../snapr

include $(GITDIR)/Makefile.config

SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
  # Linux flags
  CXXFLAGS += -fPIC -shared -D__STDC_LIMIT_MACROS
  #LDFLAGS += -lrt
  LIBS += -lrt
else ifeq ($(UNAME), Darwin)
  # OS X flags
  LDFLAGS += -dynamiclib
  LIBS += -lpython
else ifeq ($(shell uname -o), Cygwin)
  # Cygwin flags
  CXXFLAGS += -shared -D__STDC_LIMIT_MACROS
  #LDFLAGS += -lpython2.6
  LIBS += -lpython2.6
endif

#SWIGFILES = getassessment.cpp

all: python

python: Snap.o snap.i
	swig -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -D_CMPWARN -I$(SNAPDIR) -I$(GLIBDIR) snap.i
	$(CC) $(CXXFLAGS) -c snap_wrap.cxx $(SWIGFILES) -I$(SNAPDIR) -I$(GLIBDIR) -I/usr/include/python2.6 -I/usr/include/python2.7
	$(CC) $(LDFLAGS) $(CXXFLAGS) snap_wrap.o Snap.o $(LIBS) -o _snap.so

Snap.o: 
	$(CC) $(CXXFLAGS) -c $(SNAPDIR)/Snap.cpp -I$(SNAPDIR) -I$(GLIBDIR)
clean:
	rm -f *.o *_wrap.cxx _*.so *.pyc

