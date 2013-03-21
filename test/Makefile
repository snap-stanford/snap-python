#
#	Makefile for running 
#

#all: tungraph epinions memory

epinions: p2p-Gnutella08.txt
	python printstat.py p2p-Gnutella08.txt epinions

tungraph:
	python tungraph.py 

memory: p2p-Gnutella08.txt
	python memtest.py p2p-Gnutella08.txt

p2p-Gnutella08.txt:
	gunzip -c data/p2p-Gnutella08.txt.gz > p2p-Gnutella08.txt

clean:
	rm -f test.graph *.txt *.html

