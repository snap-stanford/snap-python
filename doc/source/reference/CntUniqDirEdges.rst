CntUniqDirEdges
'''''''''''''''


.. function:: CntUniqDirEdges(Graph)

Returns the number of unique directed edges in the graph *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int
    The number of unique directed edges in *Graph*.


The following example shows how to calculate the number of unique directed edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    count = snap.CntUniqDirEdges(Graph)
    print "Directed Graph: Count of unique directed edges is %d" % count

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    count = snap.CntUniqDirEdges(Graph)
    print "Undirected Graph: Count of unique Directed edges is %d" % count

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    count = snap.CntUniqDirEdges(Graph)
    print "Network Graph: Count of unique Directed edges is  %d" % count
