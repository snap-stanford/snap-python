GetAnf
'''''''''''

.. function:: GetAnf(Graph,SrcNId,DistNbrsV,MxDist,IsDir,Napprox)


Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SrcNId*: int (input)
    
- *DistNbrsV*: vector of (integer,float) values (input)

- *MxDist*: int (input)
    
- *isDir*: bool (input)

- *Napprox*: int (input)

Return value:

- None

The following example shows how count number of self edges in :class:`Graph`::

    import snap

    G1 = snap.PNGraph.New()
	G1.AddNode(0)
	G1.AddNode(1)
	G1.AddEdge(0,1)
	G1.AddEdge(1,1)

	snap.GetAnf(G1)


