#
#	Top level Python SNAP Makefile
#

.PHONY: swig test examples

#all: swig-r swig-sw test examples
all: swig test examples

# run SWIG and create Python interface code
swig:
	make -C swig

# run tests
test:
	make -C test

examples:
	make -C examples
  
clean:
	make -C swig clean
	make -C swig clean
	make -C test clean
	make -C examples clean
