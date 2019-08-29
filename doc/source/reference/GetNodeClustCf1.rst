GetNodeClustCf
''''''''''''''

.. function:: GetNodeClustCf(Graph, NIdCCfH)

Computes clustering coefficient of each node in *Graph*. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdCCfH*: :class:`TIntFltH`, a hash table of int keys and float values (output)
    Clustering Coefficients. Keys are node IDs, values are the node's computed clustering coefficients.

Return value:

- None


The following example shows how to calculate the clustering coefficient for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(Graph, NIdCCfH)
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(UGraph, NIdCCfH)
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(Network, NIdCCfH)
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

