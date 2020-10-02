GetNodeClustCfAll
'''''''''''''''''

.. function:: GetNodeClustCfAll()

A graph method that computes the clustering coefficient of each node. Considers the graph as undirected.

Parameters:

- None

Return value:

- :class:`TIntFltH`: a hash table of int keys and float values
    Clustering Coefficients. Keys are node ids, values are the node's computed clustering coefficients.


The following example shows how to calculate the clustering coefficient for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NIdCCfH = Graph.GetNodeClustCfAll()
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NIdCCfH = UGraph.GetNodeClustCfAll()
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NIdCCfH = Network.GetNodeClustCfAll()
    for item in NIdCCfH:
        print(item, NIdCCfH[item])

