Get1CnCom
'''''''''''

.. function:: Get1CnCom()

A graph method for undirected graphs that returns 1-components: maximal connected components of that can be disconnected from a graph by removing a single edge.

Parameters:

- None

Return Value:

- *Cn1ComV*: :class:`TCnComV`, a vector of connected components
    The vector of 1-components, each of which consists of a vector of node ids.


The following example shows how to get the 1-components with
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    CnComs = UGraph.Get1CnCom()
    for CnCom in CnComs:
        for NI in CnCom:
            print(NI)
