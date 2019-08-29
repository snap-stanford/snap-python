CntNonZNodes 
''''''''''''

.. function:: CntNonZNodes (Graph) 

Returns the number of nodes in *Graph* with degree greater than 0.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value: 

- int
    The number of nodes in *Graph* with degree greater than 0.


The following example shows how to calculate the number of non-zero nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Count = snap.CntNonZNodes(Graph)
    print("Directed Graph: Count of nodes with degree greater than 0 is %d" % Count)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Count = snap.CntNonZNodes(UGraph)
    print("Undirected Graph: Count of nodes with degree greater than 0 is %d" % Count)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Count = snap.CntNonZNodes(Network)
    print("Network Graph: Count of nodes with degree greater than 0 is %d" % Count)

