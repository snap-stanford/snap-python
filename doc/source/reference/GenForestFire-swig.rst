GenForestFire (SWIG)
''''''''''''''''''''

.. function:: GenForestFire(Nodes, FwdProb, BckProb)
   :noindex:

Generates a random Forest Fire, directed graph with given probabilities.

Parameters:

- *Nodes*: int (input)
    Number of nodes in the directed graph,

- *FwdProb*: float (input)
    Forward probability of an edge.

- *BckProb*: float (input)
    Backward probability of an edge.

Return value:

- directed graph
    A Snap.py directed graph generated using the Forest Fire model.


The following example shows how to use :func:`GenForestFire`::
	
    import snap 

    Graph = snap.GenForestFire(100, 0.5, 0.5)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
