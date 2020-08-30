GetLeadEigVec
'''''''''''

.. function:: GetLeadEigVec()

A graph method that computes the leading eigenvector of the adjacency matrix representing an undirected graph.

Parameters:

- None

Return value:

- :class:`TFltV`, a vector of floats
    The leading eigenvector of the adjacency matrix representing the given graph.

The following example shows how to get the leading eigenvector of the adjacency matrix for 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigVec =  UGraph.GetLeadEigVec()
    for Val in EigVec:
        print(Val)
