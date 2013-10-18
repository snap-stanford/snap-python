GetEigVec
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetEigVec(Graph, EigVecV)

.. note::

    This function is not yet supported.

Computes leading eigenvector of the adjacency matrix representing an undirected *Graph*


Parameters:

- *Graph*: PUNGraph (input)
    A Snap.py graph or a network

- *EigVecV*: TFltV (output)
    A leading eigenvector of the adjacency matrix representing the given *Graph*

Return value:

- None

The following example shows how to get leading eigenvector of the adjacency matrix for 
:class:`TUNGraph``::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigvV =  snap.TFltV()
    snap.GetEigVec(Graph, EigvV)
    index = 0
    for Vl in EigvV:
        index += 1
        print "%d: %.6f" % (index, v)
