GetSccSzCnt
'''''''''''

.. function:: GetSccSzCnt(Graph, SccSzCnt)

Returns a distribution of strongly connected component sizes.

Parameters:

- *Graph*: graph (input)
	A Snap.py graph or network type

- *SccSzCnt*: TIntPrV (output)
	Returns a set of pairs (number of nodes in the component, number of such components)

Return Value:

- None

The following example shows how to obtain the distribution of strongly connected component sizes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	SccSzCnt = snap.TIntPrV()
	GetSccSzCnt(Graph, SccSzCnt)
	print "SCC size distribution in a random directed graph:"
	for p in SccSzCnt:
		print "Size of SCC = %d, No. of SCCs = %d" % (p.GetVal1(), p.GetVal2())

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
	SccSzCnt = snap.TIntPrV()
	GetSccSzCnt(UGraph, SccSzCnt)
	print "SCC size distribution in a random undirected graph:"
	for p in SccSzCnt:
		print "Size of SCC = %d, No. of SCCs = %d" % (p.GetVal1(), p.GetVal2())

	NGraph = snap.GenRndGnm(snap.PNEANet, 10, 50)
	SccSzCnt = snap.TIntPrV()
	GetSccSzCnt(NGraph, SccSzCnt)
	print "SCC size distribution in a random directed network:"
	for p in SccSzCnt:
		print "Size of SCC = %d, No. of SCCs = %d" % (p.GetVal1(), p.GetVal2())