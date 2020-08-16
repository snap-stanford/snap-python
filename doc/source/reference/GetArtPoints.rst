GetArtPoints
''''''''''''

.. function:: GetArtPoints()

A graph method for undirected graphs that returns articulation points of a graph.

Parameters:

- None

Return value:

- *ArtNIdV*: :class:`TIntV`, a vector of ints
    The node ids of the articulation points in the graph.

For more info see: http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/


The following example shows how to find articulation points in a graph of type
:class:`TUNGraph`::

    import snap 
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 1000, 10) 
    ArtNIdV = UGraph.GetArtPoints() 
    print("Articulation points of a random Undirected Graph : ")
    for NI in ArtNIdV:
        print("node: %d" % NI)

