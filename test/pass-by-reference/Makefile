
#
# Small makefile for testing with non-Microsoft compilers
#

include ./Makefile.config

all: Snap.o

Snap.o: *.h 
	$(CC) -c $(CXXFLAGS) Snap.cpp -I$(CGLIB)

lib: Snap.o
	rm -f libsnap.a
	ar -cvq libsnap.a Snap.o

libinstall: lib
	cp libsnap.a /usr/local/lib/libsnap.a

clean:
	rm -f *.o *.a testSnap testSnap.exe *.plt *.tab *.png
