GenRndDegK
''''''''''

.. function:: GenRndDegK(Nodes, NodeDeg, NSwitch=100, Rnd=TRnd)

Generates a random graph with *Nodes* nodes, which each have a degree of exactly *NodeDeg*.

Parameters:

- *Nodes*: int (input)
    Number of nodes desired in output graph

- *NodeDeg*: int (input)
    Degree of nodes desired in output graph

- *NSwitch*: int (input)
    Average number of switches to make per edge. More switches means a more random graph.

- *Rnd*: TRnd (input)
    Random number generator

Return value:

- PUNGraph

The following example shows how to generate random graphs with control
over the aforementioned attributes::

    import snap

    # Generate graph
    Graph1 = snap.GenRndDegK(1000, 10) # Default randomness

    # Confirm expected behavior
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph1, DegToCntV)
    for item in DegToCntV:
        print "degree %d: count %d" % (item.GetVal1(), item.GetVal2())
