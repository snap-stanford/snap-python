GetTriadsByNode
''''''''''

.. function:: GetTriadsByNode(SampleNodes=-1)

Computes the number of closed and open triads for every node in *Graph*. Considers the graph as undirected.

Parameters:

- *SampleNodes*: integer
    If !=-1 then compute triads only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value:

- :class:`TIntTrV`: a vector of triplets (integer, integer, integer)
    A triple contains (node id, number of closed triads, number of open triads). Closed triads are pairs of node's neighbors that are connected between themselves. Open triads are pairs of node's neighbors that are not connected.

The following example shows how to compute the number of closed and open triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())