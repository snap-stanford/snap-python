SaveGVizColor
'''''''''''''

.. function:: SaveGVizColor(OutFNm, Desc, Labels, Colors)

A graph method that saves a graph to the .DOT file format used by GraphViz. Use ".dot" as file extension for *OutFNm*.

Parameters:

- *OutFNm*: string
    Name of the output file.

- *Desc*: string
    Description of the Graph.

- *Labels*: bool
    Indicates whether to show the node labels.

- *Colors*: Python dictionary or :class:`TIntStrH`, a hash table with int keys and string values
    Maps node ids to node colors (see GraphViz documentation for more details).

Return value:

- None

For more info about GraphViz see: http://www.graphviz.org.


The following example shows how to save graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` for GraphViz::

    import snap

    Colors = { 0: "blue", 1: "blue", 2: "red", 3: "red" }

    Graph = snap.GenRndGnm(snap.TNGraph, 4, 6)
    Graph.SaveGVizColor("Graph1.dot", "Directed Random Graph", True, Colors)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 4, 6)
    UGraph.SaveGVizColor("Graph2.dot", "Undirected Random Graph", True, Colors)

    Network = snap.GenRndGnm(snap.TNEANet, 4, 6)
    Network.SaveGVizColor("Graph3.dot", "Directed Random Network with Attributes", True, Colors)

