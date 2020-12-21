#
# Makefile for SWIG processing of SNAP Python
#	Use this Makefile to compile SNAP Python from scratch
#
# Build instructions for py2 on macOS and Linux:
#		make all2            # apply SWIG and compile the code
#		make srcdist         # build source distribution
#		make whldist         # build wheel distribution
#		make pip-test        # upload to private test pip
#		make pip-public      # upload to public release pip
# Build instructions for py3 on macOS and Linux:
#		make all3            # apply SWIG and compile the code
#		make srcdist3        # build source distribution for py3
#		make whldist3        # build wheel distribution for py3
#		make pip3-test       # upload to private test pip
#		make pip3-public     # upload to public release pip
#
# NOTE: python2 build on macOS
#	- use system python on macOS to compile
#	- use system/brew python on macOS to build the source distribution
#	- use brew python on macOS to build the wheel distribution
#	- TODO: test cross system/brew install
# NOTE: python3 build on macOS
#	- use brew python for all the steps
#	- the final packages requires brew
# 
# Build instructions for py2 on Windows:
#	- run swig in Cygwin to generate snap_wrap.cxx and snap.py
#		make swig-win
#	- build Snappy solution in Visual Studio to generate _snap.pyd
#		- open snappy-VS19
#		- add VC++ include path for snap-core, glib-core, snap-adv
#		  - create drive shares S: and P:, use Command Prompt:
#		    subst S: <path_to_snap>
#			example path: C:\cygwin\home\<user>\git\snap-dev-64
#		    subst P: <path_to_snap_python>
#			example path: C:\cygwin\home\<user>\git\snap-python-64
#		- build
#		  - use Configuration
#		    Release, x64
#	- run setup.py in Cygwin to generate the package,
#	  EXECUTE LOCALLY DIRECTLY IN CYGWIN ON THE HOST, NOT OVER SSH
#		make srcdist-win      # build Windows source distribution
#		make whldist-win      # build Windows wheel distribution
#		make pip-test         # upload to private test pip
#				      # EXECUTE MANUALLY FROM COMMAND PROMPT
#		make pip-public       # upload to public release pip
#				      # EXECUTE MANUALLY FROM COMMAND PROMPT
# Build instructions for py3 on Windows:
#	- run swig in Cygwin to generate snap_wrap.cxx and snap.py
#		make swig3-win
#	- build Snappy solution in Visual Studio to generate _snap.pyd
#		- open snappy3-VS19
#		- add VC++ include path for snap-core, glib-core, snap-adv
#		  - create drive shares S: and P:, use Command Prompt:
#		    subst S: <path_to_snap>
#			example path: C:\cygwin\home\<user>\git\snap-dev-64
#		    subst P: <path_to_snap_python>
#			example path: C:\cygwin\home\<user>\git\snap-python-64
#		- build
#		  - use Configuration
#		    Release, x64
#	- run setup.py in Cygwin to generate the package,
#	  EXECUTE LOCALLY DIRECTLY IN CYGWIN ON THE HOST, NOT OVER SSH
#		make srcdist3-win     # build Windows source distribution
#		make whldist3-win     # build Windows wheel distribution
#		make pip3-test        # upload to private test pip
#				      # EXECUTE MANUALLY FROM COMMAND PROMPT
#		make pip3-public      # upload to public release pip
#				      # EXECUTE MANUALLY FROM COMMAND PROMPT

# set the path to your SNAP directory here
GITDIR = ../../snap
SNAPDIR = $(GITDIR)/$(SNAP)
GLIBDIR = $(GITDIR)/$(GLIB)
SNAPADVDIR = $(GITDIR)/$(SNAPADV)
SNAPEXPDIR = $(GITDIR)/$(SNAPEXP)

WHLFILE := $(shell ls -rt dist/*.whl | tail -1)

# include compilation parameters
include $(GITDIR)/Makefile.config
include ../Makefile.config

all: all3

all2: snap.py _snap.so

all3: snap3.py _snap3.so

snap.py: snap_wrap.cxx

snap3.py: snap_wrap3.cxx

_snap.so: snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o biasedrandomwalk.o word2vec.o n2v.o
	$(CC) $(LDFLAGS) $(LIBS) snap_wrap.o Snap.o cliques.o agm.o agmfast.o agmfit.o biasedrandomwalk.o word2vec.o n2v.o -o _snap.so

_snap3.so: snap_wrap3.o Snap.o 
	$(CC) $(LDFLAGS3) $(LIBS) snap_wrap3.o Snap.o -o _snap.so
	ln -f _snap.so _snap3.so

snap_wrap.cxx: snap.i snap_types.i tvec.i pneanet.i tmodenet.i tcrossnet.i pungraph.i pngraph.i pgraph.i pngraphmp.i pneanetmp.i pylayer.i\
	snapswig.h snap_types.h printgraph.h goodgraph.cpp
	swig $(SWIGFLAGS) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(GLIBDIR) snap.i

snap_wrap3.cxx: snap.i snap_types.i tvec.i pneanet.i tmodenet.i tcrossnet.i pungraph.i pngraph.i pgraph.i pngraphmp.i pneanetmp.i pylayer.i\
	snapswig.h snap_types.h printgraph.h goodgraph.cpp
	swig $(SWIGFLAGS3) -python -c++ -w302,312,317,325,362,383,384,389,401,503,508,509 -O -I$(SNAPDIR) -I$(GLIBDIR) snap.i
	ln -f snap_wrap.cxx snap_wrap3.cxx

snap_wrap.o: snap_wrap.cxx
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(GLIBDIR) $(IFLAGS) -c snap_wrap.cxx

snap_wrap3.o: snap_wrap3.cxx
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(GLIBDIR) $(IFLAGS3) -c snap_wrap3.cxx -o snap_wrap.o
	ln -f snap_wrap.o snap_wrap3.o

Snap.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(GLIBDIR) -c $(SNAPDIR)/Snap.cpp

cliques.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/cliques.cpp

agm.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/agm.cpp

agmfast.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/agmfast.cpp

agmfit.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/agmfit.cpp

biasedrandomwalk.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/biasedrandomwalk.cpp

word2vec.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/word2vec.cpp

n2v.o: 
	$(CC) $(CXXFLAGS) -I$(SNAPDIR) -I$(SNAPADVDIR) -I$(GLIBDIR) -c $(SNAPADVDIR)/n2v.cpp

install: setup.py snap.py _snap.so
	sudo $(PYTHON) setup.py install

srcdist: $(SETUP) snap.py _snap.so
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON) $(SETUP) sdist

whldist: $(SETUP) snap.py _snap.so
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON) $(SETUP) bdist_wheel
ifeq ($(UNAME), Linux)
	# change name '-linux_' to '-linuxmany1_' as required by pip
	mv dist/*-linux_* `ls dist/*-linux_* | sed -e "s/-linux_/-manylinux1_/g"`
endif

srcdist3: $(SETUP) snap3.py _snap3.so snap.py
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON3) $(SETUP) sdist

whldist3: $(SETUP) snap3.py _snap3.so snap.py
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON3) $(SETUP) bdist_wheel
ifeq ($(UNAME), Linux)
	# change name '-linux_' to '-linuxmany1_' as required by pip
	mv dist/*-linux_* `ls dist/*-linux_* | sed -e "s/-linux_/-manylinux1_/g"`
endif

swig-win: snap_wrap.cxx

swig3-win: snap_wrap3.cxx

install-win: setup.py snap.py _snap.pyd
	$(PYTHON) setup.py install

srcdist-win: setup.py snap.py _snap.pyd
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON) setup.py sdist --formats=zip
	chmod 0644 dist/*.zip

srcdist3-win: setup.py snap.py _snap.pyd
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	"$(PYTHON3)" setup.py sdist --formats=zip
	chmod 0644 dist/*.zip

whldist-win: setup.py snap.py _snap.pyd
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	$(PYTHON) setup.py bdist_wheel

whldist3-win: setup.py snap.py _snap.pyd
	cp $(MANIFEST) MANIFEST
	cp $(MANIFEST_IN) MANIFEST.in
	"$(PYTHON3)" setup.py bdist_wheel

clean:
	rm -f *.o *_wrap*.cxx _*.so *.pyc snap*.py _snap*.*

clean-obj:
	rm -f snap_*.o _snap.so

pip-test: dist/*
	@echo TESTING uploading test file ${WHLFILE}
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ ${WHLFILE}

pip3-test: dist/*
	@echo TESTING uploading test file ${WHLFILE}
	"$(PYTHON3)" -m twine upload --repository-url https://test.pypi.org/legacy/ ${WHLFILE}

pip-public: dist/*
	@echo PUBLIC RELEASE uploading file ${WHLFILE}
	$(PYTHON) -m twine upload ${WHLFILE}

pip3-public: dist/*
	@echo PUBLIC RELEASE uploading file ${WHLFILE}
	"$(PYTHON3)" -m twine upload ${WHLFILE}

