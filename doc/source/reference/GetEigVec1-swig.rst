GetEigVec (SWIG)
''''''''''''''''

.. function:: GetEigVec(Graph, EigVecs, EigVal, EigVecV)
   :noindex:

Computes top EigVecs eigenvalues and eigenvectors of the adjacency matrix representing a given undirected Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py undirected Graph.

- *EigVecs*: int (input)
    Rank of eigenvalues and eigenvectors that should be outputted.

- *EigValV*: TFltV, a vector of floats (output)
    Eigenvalues.

- *EigVecV*: TFltVFltV> (output)
    Eigenvectors.

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/GetEigVec

The following example shows how to calculate the top 2 eigenvalues and eigenvectors for :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EigValV = snap.TFltV()
    EigVecV = snap.TFltVFltV()
    snap.GetEigVec(Graph, 10, EigVal, EigVecV)

    i = 0
    for item in EigVal:
        i += 1
        print("Eigenvalue %d: %.6f" % (i, item))

    i = 0
    for v in EigVecV:
        i += 1
        print("=== Eigenvector: %d ===" % (i))
        for item in v:
            print(item)

