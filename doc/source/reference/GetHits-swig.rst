GetHits (SWIG)
''''''''''''''

.. function:: GetHits (Graph, NIdHubH, NIdAuthH, MaxIter = 20)
   :noindex:

Computes the Hubs and Authorities score of every node in *Graph*. The scores are stored in *NIdHubH* and *NIdAuthH*.


Parameters

- *Graph*: graph (input)
    A Snap.py graph or a network.
    
- *NIdHubH*: :class:`TIntFltH`, a hash table of int keys and float values (output)
    The keys are the node ids and the values are the hub scores as outputed by the HITS algorithm.

- *NIdAuthH*: :class:`TIntFltH`, a hash table of int keys and float values (output)
    The keys are the node ids and the values are the authority scores as outputed by the HITS algorithm.   

- *MaxIter*: int (input)
    Maximum number of iterations.

Return value:

- None


The following example shows how to calculate Hub and Authority scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Graph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(UGraph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Network, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print(item, NIdHubH[item])
    for item in NIdAuthH:
        print(item, NIdAuthH[item])
