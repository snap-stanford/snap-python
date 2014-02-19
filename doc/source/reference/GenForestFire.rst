GenForestFire
'''''''''''''

.. function:: GenForestFire(Nodes, FwdProb, BckProb)

Generates a random Forest Fire, directed graph with given probabilities.

Parameters:

- *Nodes*: int (input)
    Number of nodes in the directed graph

- *FwdProb*: float (input)
    Forward probability of an edge

- *BckProb*: float (input)
    Backward probability of an edge

Return value:

- :class:`PNGraph`
    A directed graph generated using the Forest Fire model

The following example shows how to use :func:`GenForestFire`::
	
    import snap 

    Graph = snap.GenForestFire(100, 0.5, 0.5)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
