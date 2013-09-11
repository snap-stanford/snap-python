Introduction
------------

Snap.py is a Python interface for SNAP. SNAP is a general purpose,
high performance system for analysis and manipulation of large networks.
SNAP is written in C++ and optimized for maximum performance and
compact graph representation. It easily scales to massive networks
with hundreds of millions of nodes, and billions of edges.

Snap.py provides performance benefits of SNAP, combined with flexibility
of Python. Most of the SNAP functionality is available via Snap.py in Python.
This document gives a quick tutorial to a range of Snap.py operations.

To use Snap.py in Python, import the **snap** module:

>>> import snap

The code below assumes that Snap.py has been imported as shown above.


Graph and Network Types
-----------------------

Snap.py supports *graphs* and *networks*. Graphs describe topologies,
where nodes have unique integer ids and directed/undirected/multiple edges
connect the nodes of the graph.
Networks are graphs with data on nodes and/or edges of the network.
Data types that reside on nodes and edges are simply passed as template
parameters which provides a very fast and convenient way to implement
various kinds of networks with rich data on nodes and edges.

Graph types in SNAP:

* **TUNGraph**: undirected graphs (single edge between an unordered pair of nodes)
* **TNGraph**: directed graphs (single directed edge between an ordered pair of nodes)

Network types in SNAP:

* **TNEANet**: directed graphs like TNGraph but with attributes for nodes and edges 


Graph Creation
--------------

Graphs are created with the **New()** method.
Examples of how to create graphs and networks:

>>> G1 = snap.TUNGraph.New()
>>> G2 = snap.TNGraph.New()
>>> N1 = snap.TNEANet.New()


Adding Nodes and Edges
----------------------

Nodes are added with the **AddNode()** method.

>>> G1.AddNode(1)
>>> G1.AddNode(5)
>>> G1.AddNode(32)

Nodes have unique integer node ids.
There is no restriction for node ids to be contiguous integers starting at 0. 

Edges are added with the **AddEdge()** method.

>>> G1.AddEdge(1,5)
>>> G1.AddEdge(5,1)
>>> G1.AddEdge(5,32)

In TUNGraph and TNGraph edges have no explicit ids -- edges are identified by a pair of node ids.


Traversing Nodes and Edges
--------------------------

Nodes and edges are traversed with iterators. Some examples of iterator usage in Snap.py are shown below.

Create a directed random graph on 100 nodes and 1000 edges:

>>> G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)

Traverse all the nodes using a node iterator:

>>> for NI in G2.Nodes():
>>>     print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

Traverse all the edges using an edge iterator:

>>> for EI in G2.Edges():
>>>     print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

Traverse the edges by traversing nodes and getting all their neighbors:

>>> for NI in G2.Nodes():
>>>     for Id in NI.GetOutEdges():
>>>         print "edge (%d %d)" % (NI.GetId(), Id)

Node iterators provide several useful methods:

* GetId(): returns node id
* GetOutDeg(): returns out-degree of a node
* GetInDeg(): returns in-degree of a node
* GetOutNId(e): returns node id of the endpoint of e-th out-edge
* GetInNId(e): returns node id of the endpoint of e-th in-edge
* IsOutNId(n): tests if there is an out-edge to node n
* IsInNId(n): tests if there is an in-edge from node n
* IsNbrNId(n): tests if node n is a neighbor

Saving and Loading Graphs
-------------------------

With Snap.py, it is easy to save and load networks in various formats.
Internally, SNAP saves networks in a compact binary format, but functions for loading and saving networks in various other text and XML formats are also available (see gio.h).

Snap.py code for saving and loading graphs looks as follows.

Create a directed random graph on 100 nodes and 1000 edges:

>>> G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)

Save the graph in a binary format:

>>> FOut = snap.TFOut("test.graph")
>>> G2.Save(FOut)
>>> FOut.Flush()

Load the graph in a binary format:

>>> FIn = snap.TFIn("test.graph")
>>> G4 = snap.TNGraph.Load(FIn)

Save the graph to a text file:

>>> snap.SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")

Load the graph from a text file:

>>> G5 = snap.LoadEdgeList(PNGraph, "test.txt", 0, 1)

Graph Manipulation
------------------

To be done.

Computing Structural Properties
-------------------------------

To be done.

