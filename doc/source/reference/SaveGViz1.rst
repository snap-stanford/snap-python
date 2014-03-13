SaveGViz
'''''''''''

.. function:: SaveGViz(Graph, OutFNm, Desc, NIdLabelH)

Saves *Graph* to the .DOT file format used by GraphViz. Use ".dot" as file extension for *OutFNm*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Name of the output file.

- *Desc*: string (input)
    Description of the Graph.

- *NIdLabelH*: TIntStrH, a hash table with int keys and string values (input)
    Maps node ids to node string labels.
    
Return value:

- None

For more info about Graph Viz see: http://www.graphviz.org.


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
    snap.SaveGViz(Graph, "graph1.dot", "Graph file", NIdLabelH)

    UGraph = snap.TUNGraph.New()
    UGraph.AddNode(1)
    UGraph.AddNode(2)
    UGraph.AddEdge(1, 2)
    NIdLabelH = snap.TIntStrH()     
    NIdLabelH.AddDat(1, "one")
    NIdLabelH.AddDat(2, "two")
    snap.SaveGViz(UGraph, "graph2.dot", "Graph file", NIdLabelH)

    Network = snap.TNEANet.New()
    Network.AddNode(1)
    Network.AddNode(2)
    Network.AddEdge(1, 2)
    NIdLabelH = snap.TIntStrH()     
    NIdLabelH.AddDat(1, "one")
    NIdLabelH.AddDat(2, "two")
    snap.SaveGViz(Network, "graph3.dot", "Graph file", NIdLabelH)
