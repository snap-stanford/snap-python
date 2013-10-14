GenStar
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenStar (Nodes, IsDir=true)

Generates a graph with star topology. Node id 0 is in the center and then links to all other nodes.

Parameters:

- *Nodes*: int (input)
    Number of nodes in the star graph, including the center node.

- *IsDir*: boolean (input)
    Indicates whether the star graph is directed or undirected. Defaults to directed. 

Return value:

- PGraph

The following example shows how to generate a star graph with five nodes using GenStar::

    import snap

    StarGraph = snap.GenStar(snap.PNGraph, 5)
    print StarGraph
    for NI in StarGraph.Nodes():
        for Id in NI.GetOutEdges():
            print "edge (%d %d)" % (NI.GetId(), Id)