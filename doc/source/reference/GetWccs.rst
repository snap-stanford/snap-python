GetWccs
'''''''

.. function:: GetWccs ()

A graph method that returns all weakly connected components in a graph.

Parameters:

- None

Return value:

- *CnComV*: :class:`TCnComV`, a vector of connected components
    Vector of all weakly-connected components. Each component consists of a TIntV vector of node ids.


The following example shows how to calculate all weakly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Components = Graph.GetWccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 1000, 50)
    Components = UGraph.GetWccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    Network = snap.GenRndGnm(snap.TNEANet, 1000, 300)
    Components = Network.GetWccs()
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())
            

