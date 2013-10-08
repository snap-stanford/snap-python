SaveEdgeList
''''''''''''

.. function:: SaveEdgeList(Graph, Filename, Description)

Saves lists of edges from a given graph into a file.  Each line contains two columns and encodes a single edge.

Parameters:

- *Graph*: (input) A Snap.py graph or a network

- *Filename*: string
	- the name of the file to save the graph to
	
- *Description*: string
	- an optional description that will be written to the top of the file in a commented section

Return value: 

- (none)

The following example shows how to save edge lists with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    g = snap.TNGraph.New()

    g.AddNode(1)
    g.AddNode(2)
    g.AddEdge(1,2)
    g.AddNode(3)
    g.AddEdge(1,3)

    snap.SaveEdgeList(g, 'mygraph.txt')

    ug = snap.ConvertGraph(snap.PUNGraph, g)
    snap.SaveEdgeList(ug, 'unordered_mygraph.txt')

    nw = snap.ConvertGraph(snap.PNEANet, g)
    snap.SaveEdgeList(nw, 'network_mygraph.txt')
