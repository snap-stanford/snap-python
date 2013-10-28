GetHits
'''''''''''''''


.. function:: GetHits (Graph, NIdHubH, NIdAuthH, MaxIter = 20)


Computes the Hubs and Authorities score of every node in *Graph*. The scores are stored in *NIdHubH* and *NIdAuthH*.


Parameters

- *Graph*: graph (input)
    A Snap.py graph or a network
    
- *NIdHubH*: TIntFltH, a hash of int keys and float values (output)
    The keys are the node ids and the values are the hub scores as outputed by the HITS algorithm

- *NIdAuthH*: TIntFltH, a hash of int keys and float values (output)
    The keys are the node ids and the values are the authority scores as outputed by the HITS algorithm    

- *MaxIter*: int (input)
    Maximum number of iterations

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/HITS_algorithm


The following example shows how to calculate Hub and Authority scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap


    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Graph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print item.GetKey(), item.GetDat()
    for item in NIdAuthH:
        print item.GetKey(), item.GetDat()


    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Graph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print item.GetKey(), item.GetDat()
    for item in NIdAuthH:
        print item.GetKey(), item.GetDat()


    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Graph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        print item.GetKey(), item.GetDat()
    for item in NIdAuthH:
        print item.GetKey(), item.GetDat()
