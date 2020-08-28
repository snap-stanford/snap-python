GetEigVecs
'''''''''''

.. function:: GetEigVecs(EigVecs)

Computes top EigVecs eigenvalues and eigenvectors of the adjacency matrix representing a given undirected Graph.

Parameters:

- *Graph*: graph
    A Snap.py undirected Graph.

- *EigVecs*: int
    Rank of eigenvalues and eigenvectors that should be outputted.

Return value:

- *EigValV*: :class:`TFltV`, a vector of floats
    Eigenvalues.

- *EigVecV*: :class:`TFltVFltV`, a vector of vector of floats
    Eigenvectors.

For more info see: http://en.wikipedia.org/wiki/GetEigVec

The following example shows how to calculate the top 2 eigenvalues and eigenvectors for :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigValV, EigVecV = Graph.GetEigVecs(10)

    i = 0
    for item in EigValV:
        i += 1
        print("Eigenvalue %d: %.6f" % (i, item))

    i = 0
    for v in EigVecV:
        i += 1
        print("=== Eigenvector: %d ===" % (i))
        for item in v:
            print(item)

