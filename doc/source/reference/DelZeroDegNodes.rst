DelZeroDegNodes 
'''''''''''''''

.. function:: DelZeroDegNodes(Graph)

Removes all the zero-degree nodes from *Graph*.

Parameters:

- *Graph*: graph (input and output)
    A Snap.py graph or a network

Return value:

- None

The following example shows how to delete all zero-degree nodes from 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    ### Directed Graph ###
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 10)

    for NI in Graph.Nodes():
        if NI.GetOutDeg() + NI.GetInDeg() == 0:
            print "Node %d has degree 0." % NI.GetId()

    # Delete zero degree nodes
    snap.DelZeroDegNodes(Graph)

    print "0-degree nodes deleted."
    for NI in Graph.Nodes():
        if N.GetOutDeg() + N.GetInDeg() == 0:
            print "Node %d has degree 0." % N.GetId()
    
    ### Undirected Graph ###
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 10)

    for NI in Graph.Nodes():
        if NI.GetOutDeg() + NI.GetInDeg() == 0:
            print "Node %d has degree 0." % NI.GetId()

    # Delete zero degree nodes
    snap.DelZeroDegNodes(Graph)

    print "0-degree nodes deleted."
    for NI in Graph.Nodes():
        if N.GetOutDeg() + N.GetInDeg() == 0:
            print "Node %d has degree 0." % N.GetId()

    ### Network ###
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 10)

    for NI in Graph.Nodes():
        if NI.GetOutDeg() + NI.GetInDeg() == 0:
            print "Node %d has degree 0." % NI.GetId()

    # Delete zero degree nodes
    snap.DelZeroDegNodes(Graph)

    print "0-degree nodes deleted."
    for NI in Graph.Nodes():
        if N.GetOutDeg() + N.GetInDeg() == 0:
            print "Node %d has degree 0." % N.GetId()
