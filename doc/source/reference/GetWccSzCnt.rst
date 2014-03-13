GetWccSzCnt
'''''''''''

.. function:: GetWccSzCnt(Graph, WccSzCnt)

Returns a distribution of weakly connected component sizes.

Parameters:

- *Graph*: graph (input)
	A Snap.py graph or a network.

- *WccSzCnt*: TIntPrV, a vector of (int, int) pairs (output)
    Vector of pairs (number of nodes in the component, number of such components).

Return Value:

- None


The following example shows how to get the distribution of weakly-connected component sizes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	ComponentDist = snap.TIntPrV()
	snap.GetWccSzCnt(Graph, ComponentDist)
	for comp in ComponentDist:
	    print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	ComponentDist = snap.TIntPrV()
	snap.GetWccSzCnt(UGraph, ComponentDist)
	for comp in ComponentDist:
	    print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())

	Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
	ComponentDist = snap.TIntPrV()
	snap.GetWccSzCnt(Network, ComponentDist)
	for comp in ComponentDist:
	    print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())
