GenRewire
'''''''''''

.. function:: GenRewire (Graph, NSwitch, Rnd)

Rewires an undirected *Graph* by randomly rewiring its edges while keeping the degrees the same.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *NSwitch*: int (input)
    An integer that specifies the number of switches 

- *Rnd*: TRnd (input)
    Random number generator

Return value:

- PUNGraph
    The rewired graph 

The following example shows how to use :func:`GenRewire` with nodes in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    Rnd = snap.TRnd()
    snap.GenRewire(Graph, 100, Rnd)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
