#
#	Makefile for running 
#

all: tneanet epinions

epinions: p2p-Gnutella08.txt
	python printstat.py data/p2p-Gnutella08.txt epinions

tneanet:
	python tneanet.py 

clean:
	rm -f test.graph *.txt *.html

