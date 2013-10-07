LoadPajek
'''''''''

.. function:: PGraph LoadPajek(GraphType, InFNm)

Loads a (directed, undirected or multi) *GraphType* from Pajek .PAJ format file from
the filename in *InFNm*. Function supports both the 1 edge per line (<source>
<destination> <weight>) as well as the 1 node per line (<source> <destination1>
<destination2> ...) formats.

Parameters:

- *GraphType*
    The expected type of graph (undirected, directed, multi)

- *InFNm*
    Filename of source Pajek .PAJ file.
    
Return value:

- PGraph
    A graph of the specified type representing the Pajek data

For more information on the Pajek format see: http://pajek.imfm.si/doku.php

The following example shows how to load a Pajek file:

.. testsetup::

   import snap

   output = open("example.paj", "w")
   output.write("""*Vertices      9
      1 "1"    0.3034    0.7561
      2 "2"    0.4565    0.6039
      3 "3"    0.4887    0.8188
   *Arcs
   *Edges
       1      2       1
       1      3       1
       2      3       1
   """)
   output.close()

.. testcode::

   Graph = snap.LoadPajek(snap.PNGraph, 'example.paj')
   print '%s' % ', '.join(str(x.GetId()) for x in Graph.Nodes())

   Graph = snap.LoadPajek(snap.PUNGraph, 'example.paj')
   print '%s' % ', '.join(str(x.GetId()) for x in Graph.Nodes())

   Graph = snap.LoadPajek(snap.PNEANet, 'example.paj')
   print '%s' % ', '.join(str(x.GetId()) for x in Graph.Nodes())

.. testoutput::
   :hide:

   1, 2, 3
   1, 2, 3
   1, 2, 3
