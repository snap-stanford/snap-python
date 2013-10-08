CommunityGirvanNewman
'''''''''''''''''''''

.. function:: CommunityGirvanNewman(Graph, CmtyV)

.. note::

    This function is not yet supported.

Girvan-Newman community detection algorithm based on Betweenness centrality.See: Girvan M. and Newman M. E. J., Community structure in social and biological networks, Proc. Natl. Acad. Sci. USA99, 7821-7826 (2002)

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *CmtyV*: vector of connected component (output)
    Community being detected

Return value:

- double
    modularity

The following example shows how to detect communities using Girvan-Newman algorithm in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    communities = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(graph, communities)
    for community in communities:
      print [node for node in community]

    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    communities = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(graph, communities)
    for community in communities:
      print [node for node in community]

    graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    communities = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(graph, communities)
    for community in communities:
      print [node for node in community]
