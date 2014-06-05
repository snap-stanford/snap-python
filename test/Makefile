#
#	Makefile for running 
#
PYTHON=python
PYTHONPATH=../swig

all: tneanet epinions

epinions: 
	$(PYTHON) printstat.py data/p2p-Gnutella08.txt epinions

tneanet:
	$(PYTHON) tneanet.py 

clean:
	rm -f test.graph *.txt *.html

