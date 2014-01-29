GetBiCon
''''''''

.. function:: GetBiCon(Graph, BiCnComV)

Returns all bi-connected components of a Graph.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *BiCnComV*: TCnComV, a vector of connected components (output)
    A vector of bi-connected components. Each component is defined by the IDs of its member nodes.  

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Biconnected_graph

The following example shows how to print out representations of the bi-connected components of a :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    V = snap.TCnComV()
    
    snap.GetBiCon(Graph, V)

    for Com in V:
      for NId in Com.NIdV:
        print NId
      print "---------------"
