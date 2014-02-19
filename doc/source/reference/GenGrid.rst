GenGrid
'''''''''''

.. function:: GenGrid(GraphType, Rows, Cols, IsDir=True)

Generates a two-dimensional graph of rows and columns specified by Rows and Columns parameters

Parameters:

- *GraphType*: class (input)
    Type of graph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Rows*: int (input)
    Specifies number of rows for graph

- *Cols*: int (input)
    Specifies number of columns for graph

- *IsDir*: boolean (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

Return value:

graph
    A Snap.py graph of the specified type

The following example shows how to generate grid graphs for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenGrid(snap.PNGraph, 10, 12, False)
    for edge in G1.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
	
    G2 = snap.GenGrid(snap.PUNGraph, 10, 12, False)
    for edge in G2.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    G3 = snap.GenGrid(snap.PNEANet, 10, 12, False)
    for edge in G3.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())