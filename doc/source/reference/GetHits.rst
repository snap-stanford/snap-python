GetHits
'''''''

.. function:: GetHits (MaxIter = 20)

A graph method that returns the Hubs and Authorities score of every node.


Parameters

- (optional) *MaxIter*: int
    Maximum number of iterations.

Return value:

- *NIdHubH*: :class:`TIntFltH`, a hash table of int keys and float values
    The keys are the node ids and the values are the hub scores as outputed by the HITS algorithm.

- *NIdAuthH*: :class:`TIntFltH`, a hash table of int keys and float values
    The keys are the node ids and the values are the authority scores as outputed by the HITS algorithm.   


The following example shows how to calculate Hub and Authority scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NIdHubH, NIdAuthH = Graph.GetHits()
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NIdHubH, NIdAuthH = UGraph.GetHits()
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NIdHubH, NIdAuthH = Network.GetHits()
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])
