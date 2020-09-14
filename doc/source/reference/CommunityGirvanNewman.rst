CommunityGirvanNewman
'''''''''''''''''''''

.. function:: CommunityGirvanNewman()

A graph method for undirected graphs that uses the Girvan-Newman community detection algorithm based on betweenness centrality to detect communities and returns the modularity of the network and detected communities.

Parameters:

- None

Return value:

- float
    The modularity of the network.

- *CmtyV*: :class:`TCnComV`, a vector of connected components
    A vector of all the communities that are detected by the Girvan-Newman method. Each community is represented as a vector of node ids.


The following example shows how to detect communities using Girvan-Newman algorithm in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    modularity, CmtyV = UGraph.CommunityGirvanNewman()
    for Cmty in CmtyV:
        print("Community: ")
        for NI in Cmty:
            print(NI)
    print("The modularity of the network is %f" % modularity)
