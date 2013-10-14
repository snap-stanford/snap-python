GenRndDegK
''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenRndDegK(Nodes, NodeDeg, NSwitch = 100, Rnd = Rnd)

Generates a random graph where each node has degree exactly NodeDeg.

Parameters:

- *Nodes*: int (input)
    Number of nodes desired in output graph

- *NodeDeg*: int (input)
    Degree of nodes desired in output graph

- *NSwitch*: int (input)
    Average number of switches to make per edge. More switches means a more random graph,
    as :py:func:`GenRndDegK` works by randomly rewiring a non-random starting graph.
    (Note that this is different from the C++ implementation, where
    the parameter is not optional and ``2 * NSwitch`` switches are made
    on average per edge)

- *Rnd*: :class:`TRnd` (input)
    A random number generator whose Seed and Steps can be specified

Return value:

- A :class:`PUNGraph` as described above

The following example shows how to generate random graphs with control
over the aforementioned attributes::

    import snap

    # Generate graph
    Graph1 = snap.GenRndDegK(1000, 10) # Default randomness
    Graph2 = snap.GenRndDegK(1000, 10, 200) # More random than default
    Graph3 = snap.GenRndDegK(1000, 10, 100, snap.TRnd(2, 1)) # Custom random Seed and Steps

    # Confirm expected behavior
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph1, DegToCntV)
    for item in DegToCntV:
        print "degree %d: count %d" % (item.GetVal1(), item.GetVal2())
    # Outputs "degree 10: count 1000" for all of the graphs generated