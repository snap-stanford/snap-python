GetEigenVectorCentr
'''''''''''''''''''

.. function:: GetEigenVectorCentr(Graph, NIdEigenH, Eps = 1e-4, MaxIter = 100)

Computes Eigenvector Centrality of all nodes in the network. Eigenvector Centrality of a node N is defined recursively as the average of centrality values of N's neighbors in the network.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NIdEigenH*: a hash of int keys and float values (output)
    Hash table mapping node ids to their corresponding eigenvector centrality values.

- *Eps*: float (input)
    Epsilon (stop when accumulated difference in eigenvector centrality value for all nodes in an interation is less than epsilon).

- *MaxIter*: int (input)
    Maximum number of iterations (stop when exceeding this number of iterations).

Return value:

- None

The following example shows how to calculate betweenness centrality values for nodes and edges in
:class:`TUNGraph`

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdEigenH = snap.TIntFltH()
    snap.GetEigenVectorCentr(Graph, NIdEigenH)
    for item in NIdEigenH:
        print item.GetKey(), item.GetDat()
