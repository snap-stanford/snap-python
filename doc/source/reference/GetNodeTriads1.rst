GetNodeTriads
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: int GetNodeTriads(Graph, NId, ClosedTriads, OpenTriads)

.. note::

    This function is not yet supported.

Returns the number of Open and Closed triads that a node NId participates in.  Note that this function is currently overloaded in the C++ SNAP definition: there are other GetNodeTriads functions which take other arguments.  In addition, this function calls either GetNodeTriads_PNGraph, GetNodeTriads_PUNGraph, or GetNodeTriads_PNEANet (depending on the type of *Graph*), and none of these functions are defined (see below for error report).

Considers the *Graph* as undirected.

Parameters:

- *Graph*: PGraph (input)
    A Snap.py PGraph (considered as undirected)

- *NId*: int (input)
	The Id of the node of interest in *Graph*

- *ClosedTriads*: int (input)
	Number of closed triads

- *OpenTriads*: int (input)
	Number of open triads

Return value:

- int (output)
    Returns number of closed triads, and sets *OpenTriads* and *ClosedTriads* to the number of open and closed triads that *NId* participates in in *Graph*

The following example shows how to compute the number of Open and Closed triads that a node NId participates in for the :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` classes::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 10)
    closed = snap.TInt()
    open = snap.TInt()
    print snap.GetNodeTriads(Graph, 2, closed, open)

    Graph = snap.GenRndGnm(snap.PUNGraph, 10, 10)
    closed = snap.TInt()
    open = snap.TInt()
    print snap.GetNodeTriads(Graph, 2, closed, open)

    Graph = snap.GenRndGnm(snap.PNEANet, 10, 10)
    closed = snap.TInt()
    open = snap.TInt()
    print snap.GetNodeTriads(Graph, 2, closed, open)

The error report produced from the calls to GetNodeTriads is::

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Library/Python/2.7/site-packages/snap.py", line 170480, in GetNodeTriads
    if type(tspec) == PNGraph : return GetNodeTriads_PNGraph(tspec, *args)
    NameError: global name 'GetNodeTriads_PNGraph' is not defined
	
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Library/Python/2.7/site-packages/snap.py", line 170479, in GetNodeTriads
    if type(tspec) == PUNGraph: return GetNodeTriads_PUNGraph(tspec, *args)
    NameError: global name 'GetNodeTriads_PUNGraph' is not defined
	
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Library/Python/2.7/site-packages/snap.py", line 170481, in GetNodeTriads
    if type(tspec) == PNEANet : return GetNodeTriads_PNEANet(tspec, *args)
    NameError: global name 'GetNodeTriads_PNEANet' is not defined
