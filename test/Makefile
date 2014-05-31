#
#	Makefile for running 
#
PYTHON=env PYTHONPATH=../swig python

all: tneanet epinions

epinions: 
	$(PYTHON) printstat.py data/p2p-Gnutella08.txt epinions

tneanet:
	$(PYTHON) tneanet.py 

clean:
	rm -f test.graph *.txt *.html

