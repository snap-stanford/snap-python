GetLeadEigVec
'''''''''''

.. function:: GetLeadEigVec()

Computes leading eigenvector of the adjacency matrix representing an undirected *Graph*.

Parameters:

- None

Return value:

- :class:`TFltV`, a vector of floats
    A leading eigenvector of the adjacency matrix representing the given *Graph*.

The following example shows how to get leading eigenvector of the adjacency matrix for 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigVec =  UGraph.GetLeadEigVec()
    for Val in EigVec:
        print(Val)
