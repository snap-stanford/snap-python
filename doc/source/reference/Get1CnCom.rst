Get1CnCom
'''''''''''

.. function:: Get1CnCom(Graph, Cn1ComV)

Returns 1-components: maximal connected components of that can be disconnected from the *Graph* by removing a single edge.


Parameters:

- *Graph*: undirected graph (input)
    An undirected Snap.py graph

- *Cn1ComV*: TCnComV, a vector of connected components (output)
    The vector of 1-components, each of which consists of a vector of node ids.

The following example shows how to get the 1-components with
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Connected1Components = snap.TCnComV()
    snap.Get1CnCom(Graph, Connected1Components)

    for component in Connected1Components:
        for nodeid in component:
            print nodeid
