GetEigVals
''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetEigVals(Graph, EigVals, PEigV)

Computes top EigVals eigenvalues of the adjacency matrix representing a given undirected Graph.

Parameters:

- *Graph*: PUNGraph (input)
  An undirected Snap.py graph.

- *EigVals*: int (input)
  The number of eigen values 

- *PEigV* : PFltV(output)
  The eigen vector of floating point values.

Return value:
- None

The following example shows how to calcualte the top EigVals eigenvalues of the adjacency matrix of a random undirected graph::

	import snap

	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	EigVals = 5
	PEigV = snap.TFltV()
	
	snap.GetEigVals(Graph, EigVals, PEigV)
