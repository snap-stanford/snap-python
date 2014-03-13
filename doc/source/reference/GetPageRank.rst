GetPageRank
'''''''''''

.. function:: GetPageRank(Graph, PRankH, C=0.85, Eps=1e-4, MaxIter=100)

Computes the PageRank score of every node in *Graph*. The scores are stored in *PRankH*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *PRankH*: TIntFltH, a hash of int keys and float values (output)
    PageRank scores. Keys are node IDs, values are computed PageRank scores.

- *C*: float (input)
    Damping factor.

- *Eps*: float (input)
    Convergence difference.

- *MaxIter*: int (input)
    Maximum number of iterations.

Return value:

- None


The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    PRankH = snap.TIntFltH()
    snap.GetPageRank(Graph, PRankH)
    for item in PRankH:
        print item, PRankH[item]

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    PRankH = snap.TIntFltH()
    snap.GetPageRank(UGraph, PRankH)
    for item in PRankH:
        print item, PRankH[item]

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    PRankH = snap.TIntFltH()
    snap.GetPageRank(Network, PRankH)
    for item in PRankH:
        print item, PRankH[item]

