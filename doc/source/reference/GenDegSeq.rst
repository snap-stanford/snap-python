GenDegSeq
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenDegSeq(DegSeqV, Rnd)

Generates a random graph with exact degree sequence.

Parameters:

- *DegSeqV*: TIntV (input)
    The desired degree sequence, sorted in descending order.

- *Rnd*: TRnd (input)
    Random number generator.

Return value:

- PUNGraph

The following example shows how to generate a random graph with exact
degree sequence::

    import snap

    DegSeqV = snap.TIntV()
    DegSeqV.Add(3)
    DegSeqV.Add(2)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    Graph = snap.GenDegSeq(DegSeqV)

    for e in Graph.Edges():
      print "edge (%d, %d)" % (e.GetSrcNId(), e.GetDstNId())

