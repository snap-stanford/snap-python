#
#	Makefile for running 
#

all: benchmark

benchmark:
	python benchmark.py -v -n 1 -g -d -r 4-5 -t rmat,rand_neagraph -o results/results.txt

clean:
	rm -rf results *.graph
