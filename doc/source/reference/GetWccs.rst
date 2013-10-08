GetWccs
'''''''
.. note::

    This page is a draft and under revision.


.. function:: GetWccs (Graph, CnComV)

Returns all weakly connected components in a Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *CnComV*: a vector of all weakly-connected components (output)
    Vector of all weakly-connected components

Return value:

- None

A directed graph is weakly connected if, when all edges are considered bidirectional, the graph is connectd.

The following example shows how to calculate all weakly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    # NOT TESTED: as of the time this program is written, TCnComV has not been implemented in Snap.py

    import snap

    Graph = snap.TNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3); Graph.AddNode(4);
    Graph.AddEdge(1,2); Graph.AddEdge(2,3); Graph.AddEdge(3,1); Graph.AddEdge(3,4);
    CnComV = snap.TCnComV()
    MxWccGraph = snap.GetWcc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()

    Graph = snap.TUNGraph.New()
    Graph.AddNode(1); Graph.AddNode(2); Graph.AddNode(3);
    Graph.AddEdge(1,2);
    MxWccGraph = snap.GetWcc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()

    Graph = snap.GenRndGnm(snap.PNEANet, 10, 20)
    MxWccGraph = snap.GetWcc(Graph, CnComV)
    for CnCom in CnVomV:
      print CnCom.Len()
        
