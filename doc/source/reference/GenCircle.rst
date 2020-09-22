GenCircle
'''''''''

.. function:: GenCircle(GraphType, Nodes, OutDegree, IsDir=True)

Generate a circular graph of type *GraphType* with *Nodes* nodes.  The generated graph will have an edge from each node to the subsequent *OutDegree* nodes.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`TNGraph`, :class:`TNEANet`, or :class:`TUNGraph`.

- *Nodes*: int (input)
    Number of nodes in the generated graph.

- *OutDegree*: int (input)
    The number of edges to be added to each node.  This number does not include reciprocal edges.

- *IsDir*: bool (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

Return value:

- graph
    A Snap.py graph of the specified type.


The following example shows how to generate circular graphs for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenCircle(snap.TNGraph, 100, 10)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenCircle(snap.TUNGraph, 100, 10)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenCircle(snap.TNEANet, 100, 10)
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
