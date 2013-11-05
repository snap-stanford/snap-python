LoadConnList 
'''''''''''''''

.. function:: LoadConnList(GraphType,InFNm)

Loads a graph from a text file *InFNm*. The file format is a line per node.
Each line contains a node id, followed by the ids of its neighbors. Ids are
separated by whitespace. Note that this format allows for saving isolated nodes.

Parameters:

- *GraphType*: class (input)
    Type of graph to create: :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *InFNm*: string (input)
    File Name with the description of the graph nodes and edges.

Return value:

- graph
	A Snap.py graph of the specified type loaded by LoadConnList.

The following example shows how to load a graph using :func:`LoadConnList` from a file named "test.txt"::

    import snap

    Graph = snap.LoadConnList(snap.PNGraph, "test.txt")
    for EI in Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Graph = snap.LoadConnList(snap.PUNGraph, "test.txt")
    for EI in Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Graph = snap.LoadConnList(snap.PNEANet, "test.txt")
    for EI in Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
	
