SaveGViz
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: SaveGViz(Graph, OutFNm, Desc, NIdLabelH)

Save a graph in GraphVizp .DOT format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: string (input)
    The filename to save the graph

- *Desc*: string (input)
    The file description

- *NIDLabelH*: hash table with integer keys and string values (input)
    Maps node ids to node string labels
    
Return value:

- None

The following example shows how to save for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.TNGraph.New()
    Graph.AddNode(1)
    Graph.AddNode(2)
    Graph.AddEdge(1, 2)
    NIdLabelH = snap.TIntStrH()     
    NIdLabelH.AddDat(1, "one")
    NIdLabelH.AddDat(2, "two")
    snap.SaveGViz(Graph, "graph.dot", "Graph file", NIdLabelH)

    Graph = snap.TUNGraph.New()
    Graph.AddNode(1)
    Graph.AddNode(2)
    Graph.AddEdge(1, 2)
    NIdLabelH = snap.TIntStrH()     
    NIdLabelH.AddDat(1, "one")
    NIdLabelH.AddDat(2, "two")
    snap.SaveGViz(Graph, "graph.dot", "Graph file", NIdLabelH)

    Graph = snap.TNEANet.New()
    Graph.AddNode(1)
    Graph.AddNode(2)
    Graph.AddEdge(1, 2)
    NIdLabelH = snap.TIntStrH()     
    NIdLabelH.AddDat(1, "one")
    NIdLabelH.AddDat(2, "two")
    snap.SaveGViz(Graph, "graph.dot", "Graph file", NIdLabelH)
