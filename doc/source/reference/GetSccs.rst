GetSccs
'''''''

.. function:: GetSccs ()

A graph method that returns all strongly connected components in a graph.

Parameters:

- None

Return value:

- *CnComV*: :class:`TCnComV`, a vector of connected components
    Vector of all strongly-connected components. Each component consists of a TIntV vector of node ids.


The following example shows how to calculate all strongly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Components = Graph.GetSccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 1000, 50)
    Components =UGraph.GetSccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    Network = snap.GenRndGnm(snap.TNEANet, 1000, 300)
    Components = Network.GetSccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())
            
