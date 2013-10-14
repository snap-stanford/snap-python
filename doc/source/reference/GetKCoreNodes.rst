GetKCoreNodes
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetKCoreNodes(Graph, TIntPrV)

Returns the number of nodes in each core of order K (where K=0, 1, ...)

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or directed graph

- *TIntPrV*: Integer Pair Vector(input)
    A Snap.py integer pair vector

Return value:

- None

The following example shows how to use GetKCoreNodes for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    CoresV = snap.TIntPrV()
    snap.GetKCoreNodes(G,CoresV)
    for p in CoresV:
    	print "Order %d: Number of nodes %d"  % (p.GetVal1(),p.GetVal2()) 
