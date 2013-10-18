GetSngVals
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetSngVals(Graph, SngVals, SngValV)

Computes largest SngVals singular values of the adjacency matrix representing a directed Graph.

Parameters:

- *Graph*: PNGraph (input)
    A Snap.py directed graph

- *SngVals*: int (input)
    number of singular valuesx

- *SngValV*: TFltV (vector) of floats (output)
    Vector of singular values

Return value:

- None

The following example shows how to calculate singular values for :class:`TNGraph`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	SngVals = 4
	SngValV = snap.TFltV() 
	snap.GetSngVals(Graph, SngVals, SngValV)
	for item in SngValV:
	    print item

