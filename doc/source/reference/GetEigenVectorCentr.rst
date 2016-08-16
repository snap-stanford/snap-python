GetEigenVectorCentr
'''''''''''''''''''

.. function:: GetEigenVectorCentr(Graph, NIdEigenH, Eps = 1e-4, MaxIter = 100)

Computes eigenvector centrality of all nodes in *Graph* and stores it in *NIdEigenH*. Eigenvector Centrality of a node N is defined recursively as the average of centrality values of N's neighbors in the network.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *NIdEigenH*: :class:`TIntFltH`, a hash table of int keys and float values (output)
    Hash table mapping node ids to their corresponding eigenvector centrality values.

- *Eps*: float (input)
    Epsilon (stop when accumulated difference in eigenvector centrality value for all nodes in an interation is less than epsilon).

- *MaxIter*: int (input)
    Maximum number of iterations (stop when exceeding this number of iterations).

Return value:

- None


The following example shows how to calculate eigenvector centrality values for nodes in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdEigenH = snap.TIntFltH()
    snap.GetEigenVectorCentr(UGraph, NIdEigenH)
    for item in NIdEigenH:
        print "node: %d centrality: %f" % (item, NIdEigenH[item])
