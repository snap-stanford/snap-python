SaveGViz
'''''''''''

.. function:: SaveGViz(OutFNm, Desc, Labels)

A graph method that saves a graph to the .DOT file format used by GraphViz. Use ".dot" as file extension for *OutFNm*.

Parameters:

- *OutFNm*: string (input)
    Name of the output file.

- *Desc*: string (input)
    Description of the Graph.

- *Labels*: Python dictionary or :class:`TIntStrH`, a hash table with int keys and string values (input)
    Maps node ids to node string labels.
    
Return value:

- None

For more info about Graph Viz see: http://www.graphviz.org.


The following example shows how to save graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` for GraphViz::

    import snap

    Labels = { 0: "zero", 1: "one", 2: "two", 3: "three" }

    Graph = snap.GenRndGnm(snap.PNGraph, 4, 6)
    Graph.SaveGViz("graph1.dot", "Graph file", Labels)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 4, 6)
    UGraph.SaveGViz("graph2.dot", "Graph file", Labels)

    Network = snap.GenRndGnm(snap.PNEANet, 4, 6)
    Network.SaveGViz("graph3.dot", "Graph file", Labels)
