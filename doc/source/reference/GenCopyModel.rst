GenCopyModel
''''''''''''

.. function:: GenCopyModel (Nodes, Beta, Rnd=TRnd)

Generates a random scale-free network with *Nodes* nodes using the Copying Model. The generating process operates as follows: Node u is added to a graph, it selects a random 
node v, and with probability *Beta* it links to v, with 1 - *Beta* links u links to 
neighbor of v. 

Parameters:

- *Nodes*: int (input)
    Number of nodes in the generated graph.

- *Beta*: float (input)
    Probability used in the generating process.

- *Rnd*: :class:`TRnd` (input)
	Random number generator.

Return value:

- directed graph
    A Snap.py directed graph generated using the Copying Model.


The following example shows how to generate a :class:`TNGraph` using :func:`GenCopyModel`::

    import snap

    Graph = snap.GenCopyModel(20, 0.4, snap.TRnd())
    print("Resulting Graph: Nodes %d, Edges %d" % (Graph.GetNodes(), Graph.GetEdges()))
