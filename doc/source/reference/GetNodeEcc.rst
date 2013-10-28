GetNodeEcc
'''''''''''


.. function:: GetNodeEcc(Graph, NId, IsDir = False)

Returns node eccentricity, the largest shortest-path distance from the node *NId* to any other node in the *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId*: int (output)
    The id of targeted node.

- *IsDir*: boolean (input)
    Determines if *Graph* is treated as directed. i.e. False considers links as undirected (drop link directions).

Return value:

- int
    The eccentricity of node *NId* within *Graph*.

The following example shows how to calculate eccentricity for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 10, 30)
    print([snap.GetNodeEcc(Graph,n.GetId(),True) for n in Graph.Nodes()]);
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 10, 30)
    print([snap.GetNodeEcc(Graph,n.GetId(),False) for n in Graph.Nodes()]);

    Graph = snap.GenRndGnm(snap.PNEANet, 10, 30)
    print([snap.GetNodeEcc(Graph,n.GetId(),True) for n in Graph.Nodes()]);

