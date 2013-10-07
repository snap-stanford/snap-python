GenForestFire
'''''''''''

.. function:: GenForestFire(Nodes, FwdProb, BckProb)

Generates a random Forest Fire, directed graph with given probabilities.

Parameters:

- *Nodes*: number of nodes (input)
    Number of nodes in the directed graph

- *FwdProb*: forward probability (input)
    Forward probability of an edge

- *BckProb*: backward probability (input)
    Backward probability of an edge

Return value:

- *Graph*: returns a directed graph (PNGraph)

See below for example uses::

    import snap

    # creates a graph with 100 nodes, and forward and backward probabilities of .5
    G0 = snap.GenForestFire(100, 0.5, 0.5)
