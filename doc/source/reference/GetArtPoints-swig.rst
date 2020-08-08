GetArtPoints (SWIG)
'''''''''''''''''''

.. function:: GetArtPoints(InGraph,ArtNIdV)

Returns articulation points of an undirected *InGraph*.

Parameters:

- *InGraph*: undirected graph (input)
    A Snap.py undirected graph.

- *ArtNIdV*: :class:`TIntV`, a vector of ints (output)
    The node ids of the articulation points in the grpah *InGraph*.

Return value:

- None

For more info see: http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/


The following example shows how to find articulation points in a graph of type
:class:`TNGraph`::

    import snap 
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 1000, 10) 
    ArtNIdV = snap.TIntV() 
    snap.GetArtPoints(UGraph, ArtNIdV) 
    
    print("Articulation points of a random Undirected Graph : ")
    for NI in ArtNIdV:
        print("node: %d" % NI)

