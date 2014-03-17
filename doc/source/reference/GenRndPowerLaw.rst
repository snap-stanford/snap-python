GenRndPowerLaw
''''''''''''''

.. function:: GenRndPowerLaw (Nodes, PowerExp, ConfModel=True, Rnd=TRnd)

Generates a random scale-free graph with power-law degree distribution with exponent *PowerExp*. The method uses either the Configuration model (fast but the result is approximate) or the Edge Rewiring method (slow but exact).

Parameters:

- *Nodes*: int (input)
    Number of nodes.

- *PowerExp*: float (input)
    Power exponent, which must be greater than 1.

- *ConfModel*: bool (input)
    Whether the method uses the Configuration model.

- *Rnd*: :class:`TRnd` (input)
    Random number generator.

Return value:

- undirected graph
    A Snap.py undirected, random, scale-free graph.


The following example shows how to create :class:`PUNGraph` with this function::

    import snap

    UGraph1 = snap.GenRndPowerLaw (9, 10)
    for NI in UGraph1.Nodes():
        print "node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

    UGraph2 = snap.GenRndPowerLaw (5, 2, False)
    for NI in UGraph2.Nodes():
        print "node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
