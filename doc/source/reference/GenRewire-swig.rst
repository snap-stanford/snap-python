GenRewire (SWIG)
''''''''''''''''''

.. function:: GenRewire (Graph, NSwitch, Rnd=TRnd)

Rewires an undirected *Graph* by randomly rewiring its edges while keeping the degrees the same.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NSwitch*: int (input)
    An integer that specifies the number of switches.

- *Rnd*: :class:`TRnd` (input)
    Random number generator.

Return value:

- undirected graph
    The Snap.py undirected rewired graph.


The following example shows how to use :func:`GenRewire` with nodes in
:class:`TUNGraph`::

    import snap

    GIn = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for EI in GIn.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Rnd = snap.TRnd()
    GOut = snap.GenRewire(Graph, 100, Rnd)
    for EI in GOut.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
