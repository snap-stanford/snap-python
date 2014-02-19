GenRndPowerLaw
''''''''''''''

.. function:: GenRndPowerLaw (Nodes, PowerExp, ConfModel=True, Rnd=TRnd)

Generates a random scale-free graph with power-law degree distribution with exponent *PowerExp*. The method uses either the Configuration model (fast but the result is approximate) or the Edge Rewiring method (slow but exact).

Parameters:

- *Nodes*: int (input)
    Number of nodes

- *PowerExp*: float (input)
    Power exponent, which must be greater than 1

- *ConfModel*: boolean (input)
    Whether the method uses the Configuration model

- *Rnd*: TRnd (input)
    Random number generator 


Return value:

- :class:`PUNGraph`
    the generated random scale-free graph 


The following example shows how to create :class:`PUNGraph` with this function::

    import snap

    #Generate a graph with 9 nodes and power exponent of 10 using the Configuration model
    G1 = snap.GenRndPowerLaw (9, 10)
    for NI in G1.Nodes():
        print "node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

    #Generate a graph with 5 nodes and power exponet of 2 using the Edge Rewiring method
    G2 = snap.GenRndPowerLaw (5, 2, False)
    for NI in G2.Nodes():
        print "node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
