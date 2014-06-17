LoadDyNet
'''''''''

.. function:: LoadDyNet(FNm)

Loads a directed network in the DyNetML format. Loads only the first network in the file *FNm*.

Parameters:

- *InFNm*: string (input)
    Filename with the description of the graph.

Return value:

- directed graph
    A directed Snap.py graph.

For more info, see ORA Network Analysis Data (http://www.casos.cs.cmu.edu/computational_tools/data2.php) 


The following example shows how to get PNGraph object for nodes in
:class:`TNGraph`::

    import snap
    import sys
    
    GOut = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    
    fname = "test.xml"
    f = open(fname, "w")
    f.write("<network>\n")
    
    for EI in GOut.Edges():
        src = EI.GetSrcNId()
        dst = EI.GetDstNId()
        f.write("\t<link source='" + str(src) + "' target='" + str(dst) + "'/> \n")
    
    f.write("</network>\n")
    f.close()
    
    GIn = snap.LoadDyNet(fname)
    
    if (GIn.GetNodes() == GOut.GetNodes()):
        print ("true")
