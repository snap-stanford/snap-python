Get1CnCom (SWIG)
''''''''''''''''''

.. function:: Get1CnCom(Graph, Cn1ComV)
   :noindex:

Returns 1-components: maximal connected components of that can be disconnected from the *Graph* by removing a single edge.

Parameters:

- *Graph*: undirected graph (input)
    An undirected Snap.py graph.

- *Cn1ComV*: :class:`TCnComV`, a vector of connected components (output)
    The vector of 1-components, each of which consists of a vector of node ids.

Return Value:

- None


The following example shows how to get the 1-components with
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CnComs = snap.TCnComV()
    snap.Get1CnCom(UGraph, CnComs)

    for CnCom in CnComs:
        for NI in CnCom:
            print(NI)
