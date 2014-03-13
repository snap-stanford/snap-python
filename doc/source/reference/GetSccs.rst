GetSccs
'''''''

.. function:: GetSccs (Graph, CnComV)

Returns all strongly connected components in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *CnComV*: TCnComV, a vector of connected components (output)
    Vector of all strongly-connected components. Each component consists of a TIntV vector of node ids.

Return value:

- None


The following example shows how to calculate all strongly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # Directed Graph
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Components = snap.TCnComV()
    snap.GetSccs(Graph, Components)
    for comp in Components:
        print "Size of component: %d" % comp.Len()


    # Undirected Graph
    Graph = snap.GenRndGnm(snap.PUNGraph, 1000, 50)
    Components = snap.TCnComV()
    snap.GetSccs(Graph, Components)
    for comp in Components:
        print "Size of component: %d" % comp.Len()


    # Network
    Graph = snap.GenRndGnm(snap.PNEANet, 1000, 300)
    Components = snap.TCnComV()
    snap.GetSccs(Graph, Components)
    for comp in Components:
        print "Size of component: %d" % comp.Len()
            
