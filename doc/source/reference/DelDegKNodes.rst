DelDegKNodes
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: DelDegKNodes(Graph, OutDegK, InDegK)

.. note::

    This function is not yet supported.

Removes all nodes of out-degree OutDegK and all nodes of in-degree InDegK from the specified graph. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutDegK*: int (input)
    Specifies out-degree of nodes to be removed

- *InDegK*: int (input)
	Specifies in-degree of nodes to be removed
	
Return value:

- None

The following example shows how to create a Pajek files for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

        import snap

        Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())
	snap.DelDegKNodes(Graph, 3, 2)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())

        Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())
	snap.DelDegKNodes(Graph, 3, 2)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())

        Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())
	snap.DelDegKNodes(Graph, 3, 2)
	for N in Graph.Nodes():
	  If (N.GetOutDeg() == 3 and N.GetInDeg() == 2)
	    print "Node: %d, Out-degree %d, In-degree %d" % (N.GetId(), N.GetOutDeg(), N.GetInDeg())  
