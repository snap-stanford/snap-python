SaveGViz (SWIG)
'''''''''''''''

.. function:: SaveGViz(Graph, OutFNm, Desc, NodeLabels, NIdColorH)
   :noindex:

Saves *Graph* to the .DOT file format used by GraphViz. Use ".dot" as file extension for *OutFNm*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Name of the output file.

- *Desc*: string (input)
    Description of the Graph.

- *NodeLabels*: bool (input)
    Indicates whether to show the node labels.

- *NIdColorH*: :class:`TIntStrH`, a hash table with int keys and string values (input)
    Maps node ids to node colors (see GraphViz documentation for more details).

Return value:

- None

For more info about Graph Viz see: http://www.graphviz.org.


The following example shows how to save graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` for GraphViz::

    import snap

    H = snap.TIntStrH()
    H.AddDat(1, "blue")
    H.AddDat(2, "blue")
    H.AddDat(3, "red")
    H.AddDat(4, "red")

    Graph = snap.GenRndGnm(snap.PNGraph, 4, 6)
    snap.SaveGViz(Graph, "Graph1.dot", "Directed Random Graph", True, H)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 4, 6)
    snap.SaveGViz(UGraph, "Graph2.dot", "Undirected Random Graph", True, H)

    Network = snap.GenRndGnm(snap.PNEANet, 4, 6)
    snap.SaveGViz(Network, "Graph3.dot", "Directed Random Network with Attributes", True, H)

