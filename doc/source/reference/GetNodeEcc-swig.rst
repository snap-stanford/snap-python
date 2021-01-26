GetNodeEcc (SWIG)
'''''''''''''''''

.. function:: GetNodeEcc(Graph, NId, IsDir=False)
   :noindex:

Returns node eccentricity, the largest shortest-path distance from the node *NId* to any other node in the *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId*: int (output)
    A node id in *Graph*.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    The eccentricity of node *NId* within *Graph*.

The following example shows how to calculate eccentricity for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 10, 30)
    for NI in Graph.Nodes():
        print(NI.GetId(), snap.GetNodeEcc(Graph, NI.GetId(), True))
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 30)
    for NI in UGraph.Nodes():
        print(NI.GetId(), snap.GetNodeEcc(UGraph, NI.GetId(), False))

    Network = snap.GenRndGnm(snap.PNEANet, 10, 30)
    for NI in Network.Nodes():
        print(NI.GetId(), snap.GetNodeEcc(Network, NI.GetId(), True))

