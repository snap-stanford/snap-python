GenConfModel 
''''''''''''

.. function:: PUNGraph GenConfModel (const PUNGraph &G)

Generate a random undirected graph using (approximately) the same node degrees as in G using the configuration model.


Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network


Return value:

- *PUNGraph* : a random graph using (approximately) the same node degrees as in G using the configuration model.



The following example shows how to generate a random undirected graph of the same node degrees in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    G1 = snap.GenConfModel(Graph)

