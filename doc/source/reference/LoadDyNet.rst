LoadDyNet
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: LoadDyNet(FNm)

Loads a directed network in the DyNetML format. Loads only the first network in the file FNm.

Parameters:

- *FNm*: string (input)
    File name

Return value:

- PNGraph

For more info, see ORA Network Analysis Data (http://www.casos.cs.cmu.edu/computational_tools/data2.php) 

The following example shows how to get PNGraph object for nodes in
:class:`TNGraph`::

    import snap
    import sys
    
    Gout = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    
    fname = "test.xml"
    f = open(fname, "w")
    f.write("<network>\n")
    
    for EI in Gout.Edges():
       src = EI.GetSrcNId()
       dst = EI.GetDstNId()
       f.write("\t<link source=" + str(src) + " target=" + str(dst) + "/> \n")
    
    f.write("</network>\n")
    f.close()
    
    Gin = snap.LoadDyNet(fname)
    
    if (Gin.getNodes() == Gout.getNodes()):
        print ("true");
