GenGrid
'''''''''''

.. function:: GenGrid(Rows, Cols, IsDir)

Generates a two-dimensional graph of rows and columns specified by Rows and Columns parameters

Parameters:

- *Rows*: int (input)
    Specifies number of Rows for graph

- *Cols*: int (input)
    Specifies number of Columns for graph

- *IsDir*: boolean = true (input)
	Indicates whether the graph is directed or undirected

Return value:

- None

The following example shows how to create a Pajek files for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GenGrid(10, 12, False)
	
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.GenGrid(10, 12, False)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.GenGrid(10, 12, False)
