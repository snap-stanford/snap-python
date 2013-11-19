GetTriadParticip
''''''''''''''''

.. function:: GetTriadParticip(Graph, TriadCntV)

Calculater triangle participation ratio. For each node counts how many triangles it participates in and then returns a vector of pairs (number of triangles, number of such nodes). Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *TriadCntV*: TIntPrV, a vector of (int, int) pairs (output)
    Pairs of (number of triangles, number of nodes)

Return value:

- None

The following example shows how to compute the triangles participation ratio for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    TriadCntV = snap.TIntPrV()
    snap.GetTriadParticip(Graph, TriadCntV)
    for pair in TriadCntV:
        print pair.Val1(), pair.Val2()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    TriadCntV = snap.TIntPrV()
    snap.GetTriadParticip(Graph, TriadCntV)
    for pair in TriadCntV:
        print pair.Val1(), pair.Val2()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    TriadCntV = snap.TIntPrV()
    snap.GetTriadParticip(Graph, TriadCntV)
    for pair in TriadCntV:
        print pair.Val1(), pair.Val2()
