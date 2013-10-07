GetTriads
'''''''''''

.. function:: GetTriads(Graph, NIdCOTriadV, SampleNodes = -1)

Computes the number of open and closed triads for every node in *Graph*. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdCOTriadV*: a vector of (integer, integer, integer) triplets (output)
    Triple (node id, open triads: number of pairs of node's neighbors that are not connected, closed triads: number of pairs of node's neighbors that are connected between themselves).

- *SampleNodes*: integer (input)
    If !=-1 then compute triads only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value:

- None

The following example shows how to compute the number of open and closed triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    TriadV = snap.TIntTrV()
    snap.GetTriads(Graph, TriadV)
    for triple in TriadV:
        print triple.Val1(), triple.Val2(), triple.Val3()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    TriadV = snap.TIntTrV()
    snap.GetTriads(Graph, TriadV)
    for triple in TriadV:
        print triple.Val1(), triple.Val2(), triple.Val3()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    TriadV = snap.TIntTrV()
    snap.GetTriads(Graph, TriadV)
    for triple in TriadV:
        print triple.Val1(), triple.Val2(), triple.Val3()