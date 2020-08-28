GetEigVals
''''''''''

.. function:: GetEigVals(EigVals)

Computes top *EigVals* eigenvalues of the adjacency matrix representing the given undirected graph *Graph*.

Parameters:

- *EigVals*: int
    The number of eigenvalues.

Return value:

- :class:`TFltV`, a vector of floats
    The eigenvector of floating point values.


The following example shows how to calcualte the top *EigVals* eigenvalues for :class:`TUNGraph`::

	import snap

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	EigVals = 5
	PEigV = UGraph.GetEigVals(EigVals)
	for item in PEigV:
	    print(item)