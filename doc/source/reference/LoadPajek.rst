LoadPajek
'''''''''

.. function:: LoadPajek(GraphType, InFNm)

Loads a *GraphType* from Pajek .PAJ format file from
the filename in *InFNm*. Function supports both the 1 edge per line (<source>
<destination> <weight>) as well as the 1 node per line (<source> <destination1>
<destination2> ...) formats.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string
    Filename with the description of the graph edges.
    
Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.

For more information on the Pajek format see: http://pajek.imfm.si/doku.php


The following example shows how to load a Pajek file::

   import snap

   output = open("example.paj", "w")
   output.write("""*Vertices      9
      1 "1"    0.3034    0.7561
      2 "2"    0.4565    0.6039
      3 "3"    0.4887    0.8188
   *Arcs
       1      2       1
       1      3       1
       2      3       1
   """)
   output.close()

   Graph = snap.LoadPajek(snap.PNGraph, 'example.paj')
   for NI in Graph.Nodes():
       print(NI.GetId())

   UGraph = snap.LoadPajek(snap.PUNGraph, 'example.paj')
   for NI in UGraph.Nodes():
       print(NI.GetId())

   Network = snap.LoadPajek(snap.PNEANet, 'example.paj')
   for NI in Network.Nodes():
       print(NI.GetId())

