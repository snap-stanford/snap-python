GenConfModel 
''''''''''''

.. function:: GenConfModel (Graph)

Generate a random undirected graph using (approximately) the same node degrees as in *Graph* using the configuration model.


Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

Return value:

- :class:`PUNGraph`
    The randomly generated graph 



The following example shows how to generate a random undirected graph of the same node degrees in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for node in Graph.Nodes:
        print node.GetId(), node.GetDeg()

    G1 = snap.GenConfModel(Graph)
    for node in G1.Nodes:
        print node.GetId(), node.GetDeg()

