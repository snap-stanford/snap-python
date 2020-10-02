GenConfModel  (SWIG)
''''''''''''''''''''

.. function:: GenConfModel (Graph)
   :noindex:

Generate a random undirected graph using (approximately) the same node degrees as in *Graph* using the configuration model.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

Return value:

- undirected graph
    A random Snap.py undirected graph with the approximate degree sequence as in *Graph*.


The following example shows how to generate a random undirected graph of the same node degrees in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in Graph.Nodes():
        print(NI.GetId(), NI.GetDeg())

    G1 = snap.GenConfModel(Graph)
    for NI in G1.Nodes():
        print(NI.GetId(), NI.GetDeg())

