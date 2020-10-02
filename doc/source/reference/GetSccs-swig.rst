GetSccs (SWIG)
''''''''''''''

.. function:: GetSccs (Graph, CnComV)
   :noindex:

Returns all strongly connected components in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *CnComV*: :class:`TCnComV`, a vector of connected components (output)
    Vector of all strongly-connected components. Each component consists of a TIntV vector of node ids.

Return value:

- None


The following example shows how to calculate all strongly-connected components in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Components = snap.TCnComV()
    snap.GetSccs(Graph, Components)
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 1000, 50)
    Components = snap.TCnComV()
    snap.GetSccs(UGraph, Components)
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())

    Network = snap.GenRndGnm(snap.PNEANet, 1000, 300)
    Components = snap.TCnComV()
    snap.GetSccs(Network, Components)
    for CnCom in Components:
        print("Size of component: %d" % CnCom.Len())
            
