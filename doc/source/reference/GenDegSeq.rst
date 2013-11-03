GenDegSeq
'''''''''

.. function:: GenDegSeq(DegSeqV, Rnd=TInt::Rnd)

Generates a random graph with the exact degree sequence.

Parameters:

- *DegSeqV*: TIntV (input)
    The desired degree sequence, sorted in descending order.

- *Rnd*: TRnd (input)
    Random number generator

Return value:

- PUNGraph

The following example shows how to generate a random :class:`TUNGraph` with exact
degree sequence::

    import snap

    DegSeqV = snap.TIntV()
    DegSeqV.Add(3)
    DegSeqV.Add(2)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    Rnd = snap.TRnd()
    Graph = snap.GenDegSeq(DegSeqV, Rnd)

    for e in Graph.Edges():
      print "edge (%d, %d)" % (e.GetSrcNId(), e.GetDstNId())

