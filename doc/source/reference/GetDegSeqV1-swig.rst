GetDegSeqV (SWIG)
'''''''''''''''''

.. function:: GetDegSeqV(Graph, InDegV, OutDegV)
   :noindex:

Computes the in- and out- degree sequence vector for nodes in *Graph*. The degree sequence vectors are stored in *InDegV* and *OutDegV*, respectively.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *InDegV*: :class:`TIntV`, a vector of ints (output)
    In-degree sequence vector.

- *OutDegV*: :class:`TIntV`, a vector of ints (output)
    Out-degree sequence vector.

Return Value:

- None


The following examples shows how to compute the in- and out-degree sequence vectors for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` (Note that the resulting vectors are not ordered by the node IDs, their elements can be in an arbitrary order. Nodes in the printout are just vector indexes.)::


    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result_in_degree = snap.TIntV()
    result_out_degree = snap.TIntV()
    snap.GetDegSeqV(Graph, result_in_degree, result_out_degree)
    for i in range(0, result_in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, result_in_degree[i], result_out_degree[i]))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result_in_degree = snap.TIntV()
    result_out_degree = snap.TIntV()
    snap.GetDegSeqV(UGraph, result_in_degree, result_out_degree)
    for i in range(0, result_in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, result_in_degree[i], result_out_degree[i]))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result_in_degree = snap.TIntV()
    result_out_degree = snap.TIntV()
    snap.GetDegSeqV(Network, result_in_degree, result_out_degree)
    for i in range(0, result_in_degree.Len()):
      print("Node %s has in-degree %s and out-degree %s" % (i, result_in_degree[i], result_out_degree[i]))

