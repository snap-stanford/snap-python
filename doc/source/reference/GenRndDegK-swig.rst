GenRndDegK (SWIG)
'''''''''''''''''

.. function:: GenRndDegK(Nodes, NodeDeg, NSwitch=100, Rnd=TRnd)

Generates a random graph with *Nodes* nodes, which each have a degree of exactly *NodeDeg*.

Parameters:

- *Nodes*: int (input)
    Number of nodes desired in output graph.

- *NodeDeg*: int (input)
    Degree of nodes desired in output graph.

- *NSwitch*: int (input)
    Average number of switches to make per edge. More switches means a more random graph.

- *Rnd*: :class:`TRnd` (input)
    Random number generator.

Return value:

- undirected graph

    A Snap.py undirected graph randomly generated.

The following example shows how to generate random graphs with control
over the aforementioned attributes::

    import snap

    UGraph = snap.GenRndDegK(1000, 10)

    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(UGraph, DegToCntV)
    for item in DegToCntV:
        print("degree %d: count %d" % (item.GetVal1(), item.GetVal2()))
