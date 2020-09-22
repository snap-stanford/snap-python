GetWccSzCnt
'''''''''''

.. function:: GetWccSzCnt()

A graph method that returns a distribution of weakly connected component sizes.

Parameters:

- None

Return Value:

- *WccSzCnt*: :class:`TIntPrV`, a vector of (int, int) pairs
    Vector of pairs (number of nodes in the component, number of such components).


The following example shows how to get the distribution of weakly-connected component sizes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
	ComponentDist = Graph.GetWccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))

	UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
	ComponentDist = UGraph.GetWccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))

	Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
	ComponentDist = Network.GetWccSzCnt()
	for comp in ComponentDist:
	    print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))
