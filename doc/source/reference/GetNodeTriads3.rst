GetNodeTriads
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodeTriads(Graph, NId, GroupSet)

Returns the number of closed triads a node *NId* participates in. OR, if the parameter *GroupSet* is included, returns the number of triads between *NId* and a subset of its neighbors (given by *GroupSet*). Considers *Graph* to be undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    NId of the node of interest

- *GroupSet*: TIntSet (input) (optional)
    Set of NIds representing a subset of the neighbors of the node of interest


Return value:

- *ClosedTriads*: int
	Number of triads the node of interest (*NId*) participates in

OR

- *InGroupEdges*: int
	Number of triads between the node of interest (*NId*) and a subset of its neighbors (*GroupSet*)

.. note::

   This function does not currently perform as indicated. It is not yet implemented in SNAP.py. The error message is as follows: "if type(tspec) == PNGraph : return GetNodeTriads_PNGraph(tspec, * args)
   NameError: global name 'GetNodeTriads_PNGraph' is not defined." The example code below is theoretical and has not been tested.

The following example shows how to calculate the number of triads a node participates in for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NId = 1
    print GetNodeTriads(Graph, NId)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NId = 1
    print GetNodeTriads(Graph, NId)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NId = 1
    print GetNodeTriads(Graph, NId)
