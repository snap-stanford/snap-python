GetBiCon
''''''''

.. function:: GetBiCon()

A graph method for undirected graphs that returns all bi-connected components of a graph.

Parameters:

- None

Return value:

- *BiCnComV*: :class:`TCnComV`, a vector of connected components
    A vector of bi-connected components. Each component is defined by the ids of its member nodes.  


The following example shows how to print out representations of the bi-connected components of a :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    V = UGraph.GetBiCon()
    for CnCom in V:
      for NI in CnCom:
        print(NI)
      print("---------------")
