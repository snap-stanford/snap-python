GetNodeTriads
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodeTriads(Graph, NId)

.. note::

    This function is not yet supported.

Returns number of triads a node *NId* participates in.

Considers the graph as undirected. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Node ID

Return value:

- int

The following example shows the number of triads for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    vGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print '%d %d' % (vNodeIter.GetId(), \
                         snap.GetNodeTriads(vGraph, vNodeIter.GetId()))
    
    vGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print '%d %d' % (vNodeIter.GetId(), \
                         snap.GetNodeTriads(vGraph, vNodeIter.GetId()))

    vGraph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print '%d %d' % (vNodeIter.GetId(), \
                         snap.GetNodeTriads(vGraph, vNodeIter.GetId()))

