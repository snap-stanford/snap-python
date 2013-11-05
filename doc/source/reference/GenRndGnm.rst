GenRndGnm
'''''''''

.. function:: GenRndGnm(GraphType, Nodes, Edges, IsDir=True, Rnd=TInt.Rnd)

Generates an Erdos-Renyi random graph of the specified *GraphType*.

Parameters:

- *GraphType*: class (input)
    Type of graph to create: :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Nodes*: int (input)
    Number of nodes in the generated graph

- *Edges*: int (input)
    Number of edges in the genereated graph

- *IsDir*: bool (input)
    True for a directed graph, false for an undirected graph

- *Rnd*: TRnd (input)
    Random number generator 

Return value:

- graph
    A Snap.py graph of the specified type

The following example shows how to generate random graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
