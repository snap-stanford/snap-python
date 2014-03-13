GetEigVec
'''''''''''

.. function:: GetEigVec(Graph, EigVecV)

Computes leading eigenvector of the adjacency matrix representing an undirected *Graph*.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EigVecV*: TFltV, a vector of floats (output)
    A leading eigenvector of the adjacency matrix representing the given *Graph*.

Return value:

- None


The following example shows how to get leading eigenvector of the adjacency matrix for 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigvV =  snap.TFltV()
    snap.GetEigVec(UGraph, EigvV)
    for Val in EigvV:
        print Val
