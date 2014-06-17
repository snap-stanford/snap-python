GetEigVec
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetEigVec(Graph, EigVecs, EigValV, EigVecV)

.. note::

    This function is not yet supported.

Computes top EigVecs eigenvalues and eigenvectors of the adjacency matrix representing a given undirected Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py undirected Graph.

- *EigVecs*: int (input)
    Rank of eigenvalues and eigenvectors that should be outputted.

- *EigValV*: TFltV, a vector of floats (output)
    Eigenvalues.

- *EigVecV*: TVec<TFltV> (output)
    Eigenvectors.

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/GetEigVec

The following example shows how to calculate the top 2 eigenvalues and eigenvectors for :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Eigval = snap.TFlt()
    Eigvec = snap.TFltV()
    snap.GetEigVec(Graph, 2, Eigval, Eigvec)

    print "Eigenvalue: ", Eigval.Val

    print "Eigenvector: "
    for i in Eigvec:
	print i
