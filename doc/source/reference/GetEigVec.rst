GetEigVec
'''''''''''

.. function:: GetEigVec(Graph, EigVec)

Computes leading eigenvector of the adjacency matrix representing an undirected *Graph*.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EigVec*: :class:`TFltV`, a vector of floats (output)
    A leading eigenvector of the adjacency matrix representing the given *Graph*.

Return value:

- None


The following example shows how to get leading eigenvector of the adjacency matrix for 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigVec =  snap.TFltV()
    snap.GetEigVec(UGraph, EigVec)
    for Val in EigVec:
        print(Val)
