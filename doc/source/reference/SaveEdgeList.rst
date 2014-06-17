SaveEdgeList
''''''''''''

.. function:: SaveEdgeList(Graph, Filename, Description="")

Saves lists of edges from a given graph into a file.  Each line contains two columns and encodes a single edge. Creates a file named *Filename*.

Parameters:

- *Graph*: graph (input) 
    A Snap.py graph or a network.

- *Filename*: string (input)
    The name of the file to save the graph to.
	
- *Description*: string (input)
    An optional description that will be written to the top of the file in a commented section.

Return value: 

- None


The following example shows how to save edge lists with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.SaveEdgeList(Graph, 'mygraph.txt')

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SaveEdgeList(UGraph, 'undirected_mygraph.txt')

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SaveEdgeList(Network, 'network_mygraph.txt')
