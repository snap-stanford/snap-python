GetDegSeqV
''''''''''

.. function:: GetDegSeqV(Dir = False)

A graph method that returns the degree of nodes in *Graph*. The degrees are stored either in a single vector *DegV* for *Dir* being False, or in a pair of vectors *InDegV* and *OutDegV* for *Dir* being True.

Parameters:

- *Dir*: bool
    If False, edge direction is ignored. If True, edge direction is significant.

Return value:

- *DegV*: :class:`TIntV`, a vector of ints
    If *Dir* is False, a vector containing the degree for each node in the graph.

- *InDegV*: :class:`TIntV`, a vector of ints
    If *Dir* is True, a vector containing the in-degree for each node in the graph.

- *OutDegV*: :class:`TIntV`, a vector of ints
    If *Dir* is True, a vector containing the out-degree for each node in the graph.


Note that the resulting vectors are not ordered by the node ids, their elements can be in an arbitrary order. Nodes in the printout below are just vector indexes, not node ids.

The following example shows how to compute the sequence vector for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    degree = Graph.GetDegSeqV()
    for i in range(0, degree.Len()):
        print("Node %s has degree %s" % (i, degree[i]))
    in_degree, out_degree = Graph.GetDegSeqV()
    for i in range(0, in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, in_degree[i], out_degree[i]))


    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    degree = UGraph.GetDegSeqV()
    for i in range(0, degree.Len()):
        print("Node %s has degree %s" % (i, degree[i]))
    in_degree, out_degree = UGraph.GetDegSeqV()
    for i in range(0, in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, in_degree[i], out_degree[i]))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    degree = Network.GetDegSeqV()
    for i in range(0, degree.Len()):
        print("Node %s has degree %s" % (i, degree[i]))
    in_degree, out_degree = Network.GetDegSeqV()
    for i in range(0, in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, in_degree[i], out_degree[i]))

