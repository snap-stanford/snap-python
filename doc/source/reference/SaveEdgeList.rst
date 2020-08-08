SaveEdgeList
''''''''''''

.. function:: SaveEdgeList(Filename, Description="")

A graph method that saves lists of edges from a given graph into a file.  Each line contains two columns and encodes a single edge. Creates a file named *Filename*.

Parameters:

- *Filename*: string (input)
    The name of the file to save the graph to.
	
- (optional) *Description*: string (input)
    A description that will be written to the top of the file in a commented section.

Return value: 

- None


The following example shows how to save edge lists with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.SaveEdgeList('mygraph.txt')

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.SaveEdgeList('undirected_mygraph.txt')

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.SaveEdgeList('network_mygraph.txt')
