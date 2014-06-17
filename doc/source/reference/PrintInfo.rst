PrintInfo
'''''''''''

.. function:: PrintInfo(Graph, Desc, OutFNm="", Fast=True)

Prints basic *Graph* statistics to standard output or to a file named *OutFNm*. Additional extensive statistics which is computationally more expensive is computed when *Fast* is False.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *Desc*: string (input)
    Graph description.

- *OutFNm*: string (input)
    Optional file name for output. By default or if specified as "", output is printed to stdout.

- *Fast*: bool (input)
    Optional flag specifing whether basic (True) or extended (False) statistics should be printed.

Return value:

- None


The following example shows how to output extensive graph statistics to
standard output for random graphs of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    output_file = ""
    fast = False

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    prefix = "Python type PNGraph"
    snap.PrintInfo(Graph, prefix, output_file, fast)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    prefix = "Python type PUNGraph"
    snap.PrintInfo(UGraph, prefix, output_file, fast)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    prefix = "Python type PNEANet"
    snap.PrintInfo(Network, prefix, output_file, fast)
