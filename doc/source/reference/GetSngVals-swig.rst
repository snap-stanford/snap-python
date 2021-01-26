GetSngVals (SWIG)
'''''''''''''''''

.. function:: GetSngVals(Graph, SngVals, SngValV)
   :noindex:

Computes *SngVals* largest singular values of the adjacency matrix representing the directed graph *Graph*.

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph.

- *SngVals*: int (input)
    The number of singular values to compute.

- *SngValV*: :class:`TFltV`, a vector of floats (output)
    The vector of singular values.

Return value:

- None


The following example shows how to calculate singular values for :class:`TNGraph`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	SngVals = 4
	SngValV = snap.TFltV() 
	snap.GetSngVals(Graph, SngVals, SngValV)
	for item in SngValV:
	    print(item)

