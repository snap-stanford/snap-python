GetAnfEffDiam
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetAnfEffDiam(Graph, IsDir, Percentile, NApprox)

.. note::

    This function is not yet supported.

Returns a given *Percentile* of the shortest path length distribution of a *Graph* (based on a single run of ANF of approximation quality *NApprox*)

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *IsDir*: boolean (input)
    Use false to consider links as undirected

- *Percentile*: float (input)
    Percentile of the shortest path length distribution of a Graph

- *NApprox*: int (input)
    Quality of approximation. See the ANF paper.

Return value:

- float

References CalcEffDiam() and GetGraphAnf()

The following example shows how to use this function 
with graphs :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000) 
	snap.GetAnfEffDiam(Graph, False, 0.9, 16)

	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000) 
	snap.GetAnfEffDiam(Graph, False, 0.9, 16)
	
	Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000) 
	snap.GetAnfEffDiam(Graph, False, 0.9, 16)
