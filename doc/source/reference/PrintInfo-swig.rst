PrintInfo (SWIG)
''''''''''''''''

.. function:: PrintInfo(Graph, Desc, OutFNm="", Fast=True)
   :noindex:

Prints basic *Graph* statistics to standard output or to a file named *OutFNm*. Additional extensive statistics which is computationally more expensive is computed when *Fast* is False.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *Desc*: string (input)
    Graph description. Do not provide an empty string "" for this parameter, it might cause your program to crash.

- *OutFNm*: string (input)
    Optional file name for output. If not specified, output is printed to standard output. Do not provide an empty string "" for this parameter, it might cause your program to crash. To print to standard output on Mac OS X or Linux, provide "/dev/stdout" as a file name. This method does not work on Windows.


- *Fast*: bool (input)
    Optional flag specifing whether basic (True) or extended (False) statistics should be printed. Currently, it is not possible to have extended statistics printed out to standard output on Windows, since *OutFNm* must be non-empty, if specified.

Return value:

- None


The following example shows how to calculate graph statistics
for random graphs of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # print extended statistics to file 'info-pngraph.txt'
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PrintInfo(Graph, "Python type PNGraph", "info-pngraph.txt", False)

    # print basic statistics to file 'info-pungraph.txt'
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PrintInfo(UGraph, "Python type PUNGraph", "info-pungraph.txt")

    # print basic statistics to standard output
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PrintInfo(Network, "Python type PNEANet")

