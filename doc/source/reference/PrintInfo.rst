PrintInfo
'''''''''''

.. function:: PrintInfo(Graph, Desc="", OutFNm="", Fast=True)

Prints some basic information about *Graph* to standard output or to a file on name *OutFNm*.
More expensive information is computed when *Fast* is False.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *Desc*: string (input)
    Optional description of graph to output alongside info.

- *OutFNm*: string (input)
    Optional file name for output. If specified as "", information will print to stdout.

- *Fast*: bool (input)
    Optional flag specifing whether basic (True) or expensive (False) information will be printed.

Return value:

- None

The following example shows how to output expensive information to
standard output for random graphs of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    for graph_type in [snap.PNGraph, snap.PUNGraph, snap.PNEANet]:
        graph = snap.GenRndGnm(graph_type, 10000, 1000)
        prefix = "Python type %s" % graph_type
        output_file = ""
        fast = False
        snap.PrintInfo(graph, prefix, output_file, fast)
