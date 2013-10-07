GetMxSccs
'''''''''

.. function:: GetMxSccs (Graph)

Returns a graph representing the largest strongly connected component of an input Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- *Graph*: the maximum strongly-connected graph
    A Sanp.py graph representing the largest strongly-connected compotent of the input graph

A directed graph is strongly connected if there exists a directed path from any vertex to any other vertex in the graph. See http://en.wikipedia.org/wiki/Strongly_connected_component 

If an undirected graph is provided as input, this function will return the maximum connected component.

The following example shows how to calculate the maximum strongly-connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.TNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3); Graph.AddNode(4);
    Graph.AddEdge(1,2); Graph.AddEdge(2,3); Graph.AddEdge(3,1); Graph.AddEdge(3,4);
    MxSccGraph = snap.GetMxScc(Graph)
    for NI in MxSccGraph.Nodes():
      print NI.GetId() #1 2 3

    Graph = snap.TUNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3);
    Graph.AddEdge(1,2);
    MxSccGraph = snap.GetMxScc(Graph)
    for NI in MxSccGraph.Nodes():
      print NI.GetId() #1 2

    Graph = snap.GenRndGnm(snap.PNEANet, 10, 20)
    MxSccGraph = snap.GetMxScc(Graph)
    for NI in MxSccGraph.Nodes():
      print NI.GetId()

