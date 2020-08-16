GetSccSzCnt
'''''''''''

.. function:: GetSccSzCnt()

A graph method that returns a distribution of strongly connected component sizes.

Parameters:

- None

Return Value:

- *SccSzCnt*: :class:`TIntPrV`, a vector of (int, int) pairs
    Vector of pairs (number of nodes in the component, number of such components).


The following example shows how to get the distribution of strongly-connected component sizes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	ComponentDist = Graph.GetSccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	ComponentDist = UGraph.GetSccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))

	Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
	ComponentDist = Network.GetSccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))
