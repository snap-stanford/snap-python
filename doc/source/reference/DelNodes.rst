DelNodes
''''''''

.. function:: DelNodes(Graph, NIdV)

Removes the nodes contained in the vector *NIdV* from *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: TIntV, vector of ints (input)
    A vector of node ids to be deleted from *Graph*


Return value:

- None

The following example shows how to delete nodes from
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    ### Directed Graph ###
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    
    # Create vector of nodes to delete
    Vec = snap.TIntV()
    for i in range(10):
        Vec.Add(i)

    # Delete nodes in Vec from Graph
    snap.DelNodes(Graph, Vec)

    for NI in Vec:
        if Graph.IsNode(NI):
            print "Node %d found in graph." % NI

    ### Undirected Graph ###
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    
    # Create vector of nodes to delete
    Vec = snap.TIntV()
    for i in range(10):
        Vec.Add(i)

    # Delete nodes in Vec from Graph
    snap.DelNodes(Graph, Vec)

    for NI in Vec:
        if Graph.IsNode(NI):
            print "Node %d found in graph." % NI

    ### Network ###
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    
    # Create vector of nodes to delete
    Vec = snap.TIntV()
    for i in range(10):
        Vec.Add(i)

    # Delete nodes in Vec from Graph
    snap.DelNodes(Graph, Vec)

    for NI in Vec:
        if Graph.IsNode(NI):
            print "Node %d found in graph." % NI
