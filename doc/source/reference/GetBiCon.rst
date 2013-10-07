GetBiCon
''''''''

.. function:: GetBiCon(Graph, BiCnComV)

Returns all bi-connected components of a Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or network.

- *BiCnComV*: TCnComV (output)
    A vector of bi-connected components. Each component is defined by the IDs of its member nodes.  

Return value:

- None

The following example shows how to print out representations of the bi-connected components of a :class:`TUNGraph`, but would work with any other type of Snap.py graph or network as well.::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    v = snap.TCnComV()
    
    snap.GetBiCon(Graph, v)

    for com in v:
      for nodeID in com.NIdV:
        print nodeID
      print "---------------"
