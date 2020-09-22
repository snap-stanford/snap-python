CommunityCNM
''''''''''''

.. function:: CommunityCNM ()

A graph method for undirected graphs that uses the Clauset-Newman-Moore community detection method for large networks and returns the modularity of the network and detected communities. At every step of the algorithm two communities that contribute maximum positive value to global modularity are merged.

Parameters:

- None

Return value:

- float
    The modularity of the network.

- *CmtyV*: :class:`TCnComV`, a vector of connected components
    A vector of all the communities that are detected by the CNM method. Each community is represented as a vector of node ids.


The following example shows how to detect communities using CNM algorithm in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    modularity, CmtyV = UGraph.CommunityCNM()
    for Cmty in CmtyV:
        print("Community: ")
        for NI in Cmty:
            print(NI)
    print("The modularity of the network is %f" % modularity)
 
