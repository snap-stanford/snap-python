CommunityGirvanNewman (SWIG)
''''''''''''''''''''''''''''

.. function:: CommunityGirvanNewman(Graph, CmtyV)

Uses the Girvan-Newman community detection algorithm based on betweenness centrality on *Graph*. Fills *CmtyV* with all the communities detected and returns the modularity of the network.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *CmtyV*: :class:`TCnComV`, a vector of connected components (output)
    A vector of all the communities that are detected by the Girvan-Newman method. Each community is represented as a vector of node ids.

Return value:

- float
    The modularity of the network.


The following example shows how to detect communities using Girvan-Newman algorithm in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(UGraph, CmtyV)
    for Cmty in CmtyV:
        print("Community: ")
        for NI in Cmty:
            print(NI)
    print("The modularity of the network is %f" % modularity)
