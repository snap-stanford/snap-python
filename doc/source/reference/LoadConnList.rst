LoadConnList 
'''''''''''''''

.. function:: LoadConnList(GraphType,InFNm)

Loads a graph from a text file *InFNm*.

*InFNm* is a whitespace separated file of several columns: <source node id> <destination node id 1> <destination node id 2> ...
First column of each line contains a source node id followed by ids of the destination nodes. Node ids must be ints.
For example, '1 2 3' encodes edges 1-->2 and 1-->3.
Note that this format allows for saving isolated nodes.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string (input)
    Filename with the description of the graph nodes and edges.

Return value:

- graph
	A Snap.py graph of the specified type *GraphType*.

The following example shows how to load a graph using :func:`LoadConnList` from a file named "test.txt"::

    import snap

    Graph = snap.LoadConnList(snap.PNGraph, "test.txt")
    for EI in Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    UGraph = snap.LoadConnList(snap.PUNGraph, "test.txt")
    for EI in UGraph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Network = snap.LoadConnList(snap.PNEANet, "test.txt")
    for EI in Network.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
	
