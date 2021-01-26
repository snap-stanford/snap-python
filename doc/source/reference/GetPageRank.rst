GetPageRank
'''''''''''

.. function:: GetPageRank(C=0.85, Eps=1e-4, MaxIter=100)

A graph method that returns the PageRank score of every node.

Parameters:

- *C*: float
    Damping factor.

- *Eps*: float
    Convergence difference.

- *MaxIter*: int
    Maximum number of iterations.

Return value:

- *PRankH*: :class:`TIntFltH`, a hash of int keys and float values
    PageRank scores. Keys are node ids, values are computed PageRank scores.


The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    PRankH = Graph.GetPageRank()
    for item in PRankH:
        print(item, PRankH[item])

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    PRankH = UGraph.GetPageRank()
    for item in PRankH:
        print(item, PRankH[item])

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    PRankH = Network.GetPageRank()
    for item in PRankH:
        print(item, PRankH[item])

