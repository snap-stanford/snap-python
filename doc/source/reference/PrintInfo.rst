PrintInfo
'''''''''

.. function:: PrintInfo(Desc, OutFNm="", Fast=True)

A graph method that prints basic graph statistics to standard output or to a file named *OutFNm*. If *Fast* is False, then additional, computationally more expensive statistics is computed.

Parameters:

- *Desc*: string
    Graph description. Do not provide an empty string "" for this parameter, it might cause your program to crash.

- (optional) *OutFNm*: string
    Optional file name for output. If not specified, output is printed to standard output. Do not provide an empty string "" for this parameter, it might cause your program to crash. To print to standard output on Mac OS X or Linux, provide "/dev/stdout" as a file name. Standard output does not work on Windows.

- (optional) *Fast*: bool
    Optional flag specifing whether basic (True) or extended (False) statistics should be printed. Currently, it is not possible to have extended statistics printed out to standard output on Windows, since *OutFNm* must be non-empty, if specified.

Return value:

- None


The following example shows how to calculate graph statistics
for random graphs of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # print extended statistics to file 'info-pngraph.txt'
    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.PrintInfo("Python type TNGraph", "info-pngraph.txt", False)

    # print basic statistics to file 'info-pungraph.txt'
    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.PrintInfo("Python type TUNGraph", "info-pungraph.txt")

    # print basic statistics to standard output
    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.PrintInfo("Python type TNEANet")

