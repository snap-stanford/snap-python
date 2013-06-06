#
#	Makefile for running 
#

all: tneanet epinions

epinions: p2p-Gnutella08.txt
	python printstat.py data/p2p-Gnutella08.txt epinions

tneanet:
	python tneanet.py 

p2p-Gnutella08.txt:
	gunzip -c data/p2p-Gnutella08.txt.gz > data/p2p-Gnutella08.txt

clean:
	rm -f test.graph *.txt *.html

