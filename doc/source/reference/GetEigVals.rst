GetEigVals
''''''''''

.. function:: GetEigVals(Graph, EigVals, PEigV)

Computes top *EigVals* eigenvalues of the adjacency matrix representing the given undirected graph *Graph*.

Parameters:

- *Graph*: undirected graph (input)
    An undirected Snap.py graph.

- *EigVals*: int (input)
    The number of eigenvalues 

- *PEigV* : TFltV, a vector of floats(output)
    The eigenvector of floating point values

Return value:

- None

The following example shows how to calcualte the top *EigVals* eigenvalues for :class:`TUNGraph`::

	import snap

	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	EigVals = 5
	PEigV = snap.TFltV()
	snap.GetEigVals(Graph, EigVals, PEigV)
	for item in PEigV:
	    print item
