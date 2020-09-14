GetEigenVectorCentr
'''''''''''''''''''

.. function:: GetEigenVectorCentr(Eps = 1e-4, MaxIter = 100)

A graph method for undirected graphs that returns eigenvector centrality of all nodes. Eigenvector Centrality of a node N is defined recursively as the average of centrality values of N's neighbors in the network.

Parameters:

- (optional) *Eps*: float
    Epsilon (stop when accumulated difference in eigenvector centrality value for all nodes in an iteration is less than epsilon).

- (optional) *MaxIter*: int
    Maximum number of iterations (stop when exceeding this number of iterations).

Return value:

- *NIdEigenH*: :class:`TIntFltH`, a hash table of int keys and float values
    Hash table mapping node ids to their corresponding eigenvector centrality values.


The following example shows how to calculate eigenvector centrality values for nodes in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NIdEigenH = UGraph.GetEigenVectorCentr()
    for item in NIdEigenH:
        print("%node: d centrality: %f" % (item, NIdEigenH[item]))
