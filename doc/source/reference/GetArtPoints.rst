GetArtPoints
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetArtPoints(InGraph,ArtNidV)

Returns articulation points of an undirected *InGraph*

Parameters:

- *InGraph*: PUNGraph (input)
    A Snap.py undirected graph.

- *ArtNidV*: a vector of integers (output)
    retutned articulation points.

Return value:

- None

For more info see: http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

The following example shows how to find articulation points in a graph of type
:class:`TNGraph`::

    import snap 
    
    InGraph = snap.GenRndGnm(snap.PUNGraph, 1000, 5000) 
    ArtNidV = snap.TIntV() 
    snap.GetArtPoints(InGraph, ArtNidV) 
    
    print "Articulation points of a random Undirected Graph : " 
    for item in ArtNidV:print item

