GetWccSzCnt
'''''''''''
.. function:: GetWccSzCnt ( PGraph, &WccSzCnt)

Returns a distribution of weakly connected component sizes.

Parameters:

- *PGraph*: graph (input)
    Graph or network to be analyzed

- *WccSzCnt*: A vector of int pairs (output)
    Set of pairs (number of nodes in the component, number of such components)


Return value:

- None

The following example shows how to get the distribution of weakly connected component sizes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap
	#undirected graph
	UNgraph = snap.GenRndGnm(snap.PUNGraph, 1000, 50)
	UNcomponentDist = TIntPrV()
	GetWccSzCnt (UNgraph, UNcomponentDist)
	for comp in UNcomponentDist:
		print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())

	#directed graph
	Dgraph = snap.GenRndGnm(snap.PNGraph, 1000, 150)
	DcomponentDist = TIntPrV()
	GetWccSzCnt (Dgraph, DcomponentDist)
	for comp in DcomponentDist:
		print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())

	#network
	NET = snap.GenRndGnm(snap.PNEANet, 1000, 300)
	NETcomponentDist = TIntPrV()
	GetWccSzCnt (NET, NETcomponentDist)
	for comp in NETcomponentDist:
		print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())
