GenRndGnm
'''''''''

.. function:: GenRndGnm(GraphType, Nodes, Edges, IsDir=True, Rnd=TRnd)

Generates an Erdos-Renyi random graph of the specified *GraphType*.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`TNGraph`, :class:`TNEANet`, or :class:`TUNGraph`.

- *Nodes*: int (input)
    Number of nodes in the generated graph.

- *Edges*: int (input)
    Number of edges in the genereated graph.

- *IsDir*: bool (input)
    Indicates whether to consider the edges as directed or undirected. Defaults to directed. 

- *Rnd*: :class:`TRnd` (input)
    Random number generator.

Return value:

- graph
    A Snap.py graph of the specified type.


The following example shows how to generate random graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
