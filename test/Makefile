#
#	Makefile for running 
#
PYTHON=python
PYTHONPATH=../swig

test: TestAll

all: tneanet epinions

TestAll:
	cp ../swig/_snap.so .
	cp ../swig/snap.py .
	./test-snappy.sh

epinions: 
	$(PYTHON) printstat.py data/p2p-Gnutella08.txt epinions

tneanet:
	$(PYTHON) tneanet.py 

clean:
	rm -f test.graph *.txt *.html

