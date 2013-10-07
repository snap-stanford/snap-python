GetSccs
'''''''

.. function:: GetSccs (Graph, CnComV)

Returns all strongly connected components in a Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *CnComV*: a vector of all strongly-connected components (output)
    Vector of all strongly-connected components

Return value:

- None

A directed graph is strongly connected if there exists a directed path from any vertex to any other vertex in the graph. See http://en.wikipedia.org/wiki/Strongly_connected_component 

The following example shows how to calculate all strongly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    # NOT TESTED: as of the time this program is written, TCnComV has not been implemented in Snap.py

    import snap

    Graph = snap.TNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3); Graph.AddNode(4);
    Graph.AddEdge(1,2); Graph.AddEdge(2,3); Graph.AddEdge(3,1); Graph.AddEdge(3,4);
    CnComV = snap.TCnComV()
    MxSccGraph = snap.GetScc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()

    Graph = snap.TUNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3);
    Graph.AddEdge(1,2);
    MxSccGraph = snap.GetScc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()

    Graph = snap.GenRndGnm(snap.PNEANet, 10, 20)
    MxSccGraph = snap.GetScc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()
            
