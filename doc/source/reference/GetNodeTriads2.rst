GetNodeTriads
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodeTriads(Graph, NId, GroupSet, InGroupEdges, InOutGroupEdges, OutGroupEdges)

.. note::

    This function is not yet supported.

Returns the number of triads between a node NId and a subset of its neighbors GroupSet

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Id of the node

- *GroupSet*: set (input)
    A subset of its neighbors of node NId

- *InGroupEdges*: int (output)
    Number of triads (NId, G1, G2), where G1 and G2 are in GroupSet

- *InOutGroupEdges*: int (output)
    Number of triads (NId, G1, O1), where G1 in GroupSet and O1 not in GroupSet

- *OutGroupEdges*: int (output)
    Number of triads (NId, O1, O2), where O1 and O2 are not in GroupSet

Return value:

- None

Unexpected behaviors:

- The data structure for GroupSet (TIntSet) is not implemented

- GetNodeTriads method calls three sub-methods (GetNodeTriads_PUNGraph, GetNodeTriads_PNGraph and GetNodeTriads_PNEANet). None of these three are actually implemented, causing errors like "NameError: global name 'GetNodeTriads_PNGraph' is not defined"

The following example shows how to calculate the number of triads between a node NId and a subset of its neighbors GroupSet::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NId = Graph.Nodes().next().GetId()
    GroupSet = snap.TIntSet()
    
    inGroupEdges = snap.TInt()
    inOutGroupEdges = snap.TInt()
    outGroupEdges = snap.TInt()
    
    snap.GetNodeTriads(Graph, NId, GroupSet, inGroupEdges, inOutGroupEdges, outGroupEdges)
