GetTriadsByNode
''''''''''

.. function:: GetTriadsByNode(SampleNodes=-1)

A graph method that computes the number of closed and open triads for every node. Considers the graph as undirected.

Parameters:

- (optional) *SampleNodes*: integer
    If *SampleNodes* is -1 (default value), then compute triads for all the nodes. Otherwise, compute triads only for a random sample of *SampleNodes* nodes.

Return value:

- :class:`TIntTrV`: a vector of triplets (integer, integer, integer)
    A triple contains (node id, number of closed triads, number of open triads). Closed triads are pairs of node's neighbors that are connected between themselves. Open triads are pairs of node's neighbors that are not connected.

The following example shows how to compute the number of closed and open triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())

    Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())

    Graph = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    TriadV = Graph.GetTriadsByNode()
    for triple in TriadV:
        print(triple.Val1(), triple.Val2(), triple.Val3())
