GenConfModel (SWIG)
''''''''''''''''''''''

.. function:: GenConfModel(DegSeqV, Rnd=TRnd)

Generates a random undirected graph with the given degree sequence *DegSeqV* using the configuration model.

Parameters:

- *DegSeqV*: :class:`TIntV`, a vector of ints (input)
	The degree sequence vector.

- *Rnd*: :class:`TRnd` (input)
	Random number generator.

Return value:

- undirected graph
    A random Snap.py undirected graph with degree sequence given by *DegSeqV*.


The following example generates a random undirected graph with degree sequence 1, 2, 3::

    import snap

    DegSeqV = snap.TIntV()
    DegSeqV.Add(1)
    DegSeqV.Add(2)
    DegSeqV.Add(3)
    Rnd = snap.TRnd()

    UGraph = snap.GenConfModel(DegSeqV, Rnd)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
