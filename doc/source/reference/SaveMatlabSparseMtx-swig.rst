SaveMatlabSparseMtx (SWIG)
''''''''''''''''''''''''''

.. function:: SaveMatlabSparseMtx(Graph, OutFNm)
   :noindex:

Saves a graph in a MATLAB sparse matrix format.

Each line contains a tuple of 3 values: <source node id><tab><destination node id><tab>1.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Name of the output file.

Return value:

- None

The following example shows how to save a graph of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` in a MATLAB sparse matrix format::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 1000, 500)
    snap.SaveMatlabSparseMtx(Graph, "TNGraph.mat")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 1000, 500)
    snap.SaveMatlabSparseMtx(UGraph, "TUNGraph.mat")

    Network = snap.GenRndGnm(snap.PNEANet, 1000, 500)
    snap.SaveMatlabSparseMtx(Network, "TNEANet.mat")
