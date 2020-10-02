GenDegSeq (SWIG)
''''''''''''''''

.. function:: GenDegSeq(DegSeqV, Rnd=TRnd)
   :noindex:

Generates an undirected random graph with the exact degree sequence given by *DegSeqV*.

Parameters:

- *DegSeqV*: :class:`TIntV`, a vector of ints (input)
    The desired degree sequence, sorted in descending order.

- *Rnd*: :class:`TRnd` (input)
    Random number generator.

Return value:

- undirected graph
    A Snap.py undirected graph generated with the degree sequence given by *DegSeqV*.


The following example shows how to generate a random :class:`TUNGraph` with
exact degree sequence::

    import snap

    DegSeqV = snap.TIntV()
    DegSeqV.Add(3)
    DegSeqV.Add(2)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    DegSeqV.Add(1)
    Rnd = snap.TRnd()
    UGraph = snap.GenDegSeq(DegSeqV, Rnd)

    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

