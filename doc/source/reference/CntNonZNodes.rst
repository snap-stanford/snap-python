CntNonZNodes 
''''''''''''

.. function:: CntNonZNodes () 

A graph method that returns the number of nodes in a graph with degree greater than 0.

Parameters:

- None

Return value: 

- int
    The number of nodes in a graph with degree greater than 0.


The following example shows how to calculate the number of non-zero nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntNonZNodes()
    print("Directed Graph: Count of nodes with degree greater than 0 is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntNonZNodes()
    print("Undirected Graph: Count of nodes with degree greater than 0 is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntNonZNodes()
    print("Network Graph: Count of nodes with degree greater than 0 is %d" % Count)

