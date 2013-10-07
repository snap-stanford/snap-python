Get1CnCom
'''''''''''

.. function:: Get1CnCom(Graph, Cn1ComV)

Returns 1-components: maximal connected components of that can be disconnected from the Graph by removing a single edge.

We find such components as follows: Find all bridge edges, remove them from the Graph, find largest component K and add back all bridges that do not touch K. Now, find the connected components of this graph. 

Parameters:

- *Graph*: PUNGraph graph (input)
    An undirected Snap.py graph or a network

- *Cn1ComV*: vector of TCnCom connected components (output)
    The vector of 1-components, each of which consists of a vector of node ids.

The following example shows how to calculate Betweenness Centrality scores for nodes and edges in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Connected1Components = snap.TCnComV()
    snap.GetCn1Com(Graph, Connected1Components)

    for component in Connected1Components:
      for nodeid in component:
        print nodeid
