GetDegSeqV
''''''''''

.. function:: GetDegSeqV(Graph, DegV)

Computes the degree sequence vector for nodes in *Graph*. The degree sequence vector is stored in *DegV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegV*: TIntV, a vector of ints (output)
    A vector containing the degree for each node in the graph.

Return value:

- None

The following example shows how to compute the sequence vector for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result_degree = snap.TIntV()
    snap.GetDegSeqV(Graph, result_degree)
    for i in range(0, result_degree.Len()):
        print "Node %s has degree %s" % (i,result_degree[i])

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result_degree = snap.TIntV()
    snap.GetDegSeqV(Graph, result_degree)
    for i in range(0, result_degree.Len()):
        print "Node %s has degree %s" % (i,result_degree[i])

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result_degree = snap.TIntV()
    snap.GetDegSeqV(Graph, result_degree)
    for i in range(0, result_degree.Len()):
        print "Node %s has degree %s" % (i,result_degree[i])
