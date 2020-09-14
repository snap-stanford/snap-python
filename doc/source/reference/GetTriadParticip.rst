GetTriadParticip
''''''''''''''''

.. function:: GetTriadParticip()

A graph method that calculates triangle participation ratio. It counts for each node how many triangles it participates in and then returns a vector of pairs (number of triangles, number of such nodes). Considers the graph as undirected.

Parameters:

- None

Return value:

- :class:`TIntPrV`, a vector of (int, int) pairs (output)
    Pairs of (number of triangles, number of nodes).


The following example shows how to compute the triangles participation ratio for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    TriadCntV = Graph.GetTriadParticip()
    for pair in TriadCntV:
        print(pair.Val1(), pair.Val2())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    TriadCntV = UGraph.GetTriadParticip()
    for pair in TriadCntV:
        print(pair.Val1(), pair.Val2())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    TriadCntV = Network.GetTriadParticip()
    for pair in TriadCntV:
        print(pair.Val1(), pair.Val2())
