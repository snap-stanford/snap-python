GetBiCon (SWIG)
'''''''''''''''

.. function:: GetBiCon(Graph, BiCnComV)

Returns all bi-connected components of a Graph.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *BiCnComV*: :class:`TCnComV`, a vector of connected components (output)
    A vector of bi-connected components. Each component is defined by the IDs of its member nodes.  

Return value:

- None


The following example shows how to print out representations of the bi-connected components of a :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    V = snap.TCnComV()
    snap.GetBiCon(UGraph, V)
    for CnCom in V:
      for NI in CnCom:
        print(NI)
      print("---------------")
