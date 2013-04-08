#
#	Top level Python SNAP Makefile
#

.PHONY: swig-r swig-sw test

all: swig-r swig-sw test

# run SWIG and create Python interface code
swig-r:
	make -C swig-r

swig-sw:
	make -C swig-sw

# run tests
test:
	make -C test

examples:
	make -C examples
  
clean:
	make -C swig-r clean
	make -C swig-sw clean
	make -C test clean
