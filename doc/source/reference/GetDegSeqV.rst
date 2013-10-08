GetDegSeqV
''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetDegSeqV(Graph, DegV)

Computes the degree sequence vector for nodes in *Graph*. The degree sequence vector is stored in *DegV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegV*: a vector of int values (output)
    Degrees for the nodes in the graph.

Return value:

- None

The following example shows how to calculate degrees for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegV = snap.TIntV()
    snap.GetDegSeqV(Graph, DegV)
    for deg in DegV:
        print deg

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegV = snap.TIntV()
    snap.GetDegSeqV(Graph, DegV)
    for deg in DegV:
        print deg

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegV = snap.TIntV()
    snap.GetDegSeqV(Graph, DegV)
    for deg in DegV:
        print deg
