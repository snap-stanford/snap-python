GetSngVals
'''''''''''

.. function:: GetSngVals(SngVals)

A graph method that computes *SngVals* largest singular values of the adjacency matrix representing the directed graph graph.

Parameters:

- *SngVals*: int
    The number of singular values to compute.

Return value:

- :class:`TFltV`, a vector of floats
    The vector of singular values.

The following example shows how to calculate singular values for :class:`TNGraph`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	SngVals = 4
	SngValV = Graph.GetSngVals(SngVals)
	for item in SngValV:
	    print(item)

