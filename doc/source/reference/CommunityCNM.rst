CommunityCNM
''''''''''''


.. function:: CommunityCNM (Graph, CmtyV)

Uses the Clauset-Newman-Moore community detection method for large networks. At every step of the algorithm two communities that contribute maximum positive value to global modularity are merged. Fills *CmtyV* with all the communities detected and returns the modularity of the network.

Parameters:

- Graph: undirected graph (input)
    A Snap.py undirected graph

- CmtyV: TCnComV, a vector of connected component (output)
    A vector of all the communities that are detected by the CNM method. Each community is represented as a vector of node IDs

Return value:

- float:
    The modularity of the network

The following example shows how to detect communities using CNM algorithm in :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityCNM(Graph, CmtyV)
    for Cmty in CmtyV:
        print "Community: "
        for NI in Cmty:
            print NI
    print "The modularity of the network is %f" % modularity
 
