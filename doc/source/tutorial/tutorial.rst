Introduction
````````````

This document is a quick tutorial to key Snap.py functionality.

Snap.py is a Python interface for SNAP. SNAP is a general purpose,
high performance system for analysis and manipulation of large networks.
SNAP is written in C++ and optimized for maximum performance and
compact graph representation. It easily scales to massive networks
with hundreds of millions of nodes, and billions of edges.

Snap.py provides performance benefits of SNAP, combined with flexibility
of Python.Since Snap.py is mostly just a direct interface to SNAP C++
implementation, most of the SNAP functionality is available via Snap.py
in Python. There is a direct correspondence between the SNAP functions
and Snap.py functions. SNAP documentation is available here:
http://snap.stanford.edu/snap/doc/snapdev-ref/.


To use Snap.py in Python, import the **snap** module:

>>> import snap

The code in this document assumes that Snap.py has been imported as shown above.


Basic Types
```````````

Basic types in SNAP are :class:`TInt`, :class:`TFlt`, and :class:`TStr`.
In Snap.py, these types are converted to Python types
:class:`int`, :class:`float`, and :class:`str`, respectively. In general,
there is no need to explicitly work with SNAP types in Snap.py, since
Snap.py automatically converts these basic types to Python types.

.. note::

   Do not use an empty string literal `""` in Python, if a Snap.py
   function parameter is of type :class:`TStr`. SNAP handling of `TStr("")`
   is not compatible with Python, so an empty string literal will cause
   an error.

Vector Types
````````````

Vectors are sequences of values of the same type. Existing vector values can be accessed or changed by their index in the sequence. New values can be added at the end of a vector.

Vector types in Snap.py and SNAP use a naming convention of being named as `<type_name>`, followed by `V`. For example, a vector of integers is named :class:`TIntV`.

Below are the most commonly used vector operations:

- create an empty vector of integers

  >>> v = snap.TIntV()

- add a value at the end of a vector. 5 values are added below in positions 0..4:

  >>> v.Add(1)
  0
  >>> v.Add(2)
  1
  >>> v.Add(3)
  2
  >>> v.Add(4)
  3
  >>> v.Add(5)
  4

- get the number of values in the vector:

  >>> print v.Len()
  5

- get a value at a specific vector location

  >>> print "v[2] =", v[2]
  v[2] = 3

- change a value at a specific vector location

  >>> v.SetVal(2,6)
  >>> print "v[2] =", v[2]
  v[2] = 6

- print all values in a vector using an iterator

  >>> for item in v:
  >>>     print item
  1
  2
  6
  4
  5

- print all values in a vector using an index

  >>> for i in range(0, v.Len()):
  >>>     print i, v[i]
  0 1
  1 2
  2 6
  3 4
  4 5

.. seealso::

  SNAP C++ documentation has a complete list of vector methods. Search for :class:`TVec` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.


Hash Table Types
````````````````

Hash tables contain values of the same type. Each value has a user provided key associated with it. All the keys are of the same type.

Table values can be accessed or changed either their keys. New values can be added as `(key, value)` pairs.

Hash table types in Snap.py and SNAP use a naming convention of being named as `<key_type_name><value_type_name>`, followed by `H`. For example, a hash table with integer key and string values is named :class:`TIntStrH`. If `<key_type_name>` and `<value_type_name>` have the same type, only one type name might be used, such as :class:`TIntH`.

Below are the most commonly used hash table operations:

- create an empty hash table with integer keys and string values

  >>> h = snap.TIntStrH()

- add a value to the table. 5 values are added below:

  >>> h.AddDat(5,"five")
  >>> h.AddDat(3,"three")
  >>> h.AddDat(9,"nine")
  >>> h.AddDat(6,"six")
  >>> h.AddDat(1,"one")

- get the number of values in the table:

  >>> print h.Len()
  5

- get a value for a specific key

  >>> print "h[3] =", h[3].GetDat(3)
  h[3] = three

- change a value at a specific key

  >>> h.AddDat(3,"four")
  >>> print "h[3] =", h[3].GetDat(3)
  h[3] = four

- print all values in a table using an iterator

  >>> for item in h:
  >>>     print item.GetKey(), item.GetDat()
  5 five
  3 four
  9 nine
  6 six
  1 one

.. seealso::

  SNAP C++ documentation has a complete list of hash table methods. Search for :class:`THash` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.

Pair Types
``````````
Pairs contain two values. Each value has its own type.

Pair types in Snap.py and SNAP use a naming convention of being named as `<type1><type2>`, followed by `Pr`. For example, a pair of (integer, string) is named :class:`TIntStrPr`. If `<type1>` and `<type2>` have the same type, only one type name might be used, such as :class:`TIntPr`.

Below are the most commonly used hash table operations:

- create a pair of an integer and a string:

  >>> p = snap.TIntStrPr(1, "one")

- print the first value:

  >>> print p.GetVal1()
  1

- print the second value:

  >>> print p.GetVal2()
  2

.. seealso::

  SNAP C++ documentation has a complete list of pair methods. Search for :class:`TPair` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.


SNAP Types in Snap.py
`````````````````````

The following is a list of SNAP types that are used in Snap.py functions:

- :class:`PNGraph`, a directed graph;
- :class:`PUNGraph`, an undirected graph;
- :class:`PNEANet`, a directed network;
- :class:`PGraph`, one of :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`;
- :class:`TCnComV`, a vector of connected components;
- :class:`TFltPrV`, a vector of float pairs;
- :class:`TFltV`, a vector of floats;
- :class:`TGVizLayout`, one of `gvlDot`, `gvlNeato`, `gvlTwopi`, `gvlCirco`, `gvlSfdp`;
- :class:`TIntFltH`, a hash table with integer keys and float values;
- :class:`TIntFltKdV`, a vector of (integer, float) values;
- :class:`TIntH`, a hash table with integer keys and values;
- :class:`TIntPrFltH`, a hash table with (integer, integer) pair keys and float values;
- :class:`TIntPrV`, a vector of (integer, integer) pairs;
- :class:`TIntSet`, a hash table with integer keys and no values;
- :class:`TIntStrH`, a hash table with integer keys and string values;
- :class:`TIntTrV`, a vector of (integer, integer, integer) triplets;
- :class:`TIntV`, a vector of integers;
- :class:`TRnd`, a random generator;
- :class:`TStrHash< TInt >`, a hash table woth string keys and integer values;
- :class:`TVec< TFltV >`, a vector of vectors of floats.

.. seealso::

  SNAP C++ documentation has more details on the types above. Search for :class:`<type_name>` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.



Graph and Network Types
```````````````````````

Snap.py supports *graphs* and *networks*. Graphs describe topologies,
where nodes have unique integer ids and directed/undirected/multiple edges
connect the nodes of the graph.
Networks are graphs with data on nodes and/or edges of the network.
Data types that reside on nodes and edges are simply passed as template
parameters which provides a very fast and convenient way to implement
various kinds of networks with rich data on nodes and edges.

Graph classes in SNAP:

* :class:`TUNGraph`: undirected graphs (single edge between an unordered pair of nodes)
* :class:`TNGraph`: directed graphs (single directed edge between an ordered pair of nodes)

Network classes in SNAP:

* :class:`TNEANet`: directed graphs like :class:`TNGraph` but with attributes for nodes and edges

.. seealso::

  SNAP C++ documentation has a complete list of graph and network methods. Search for :class:`TUNGraph`, :class:`TNGraph`, or :class:`TNEANet` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.

Snap.py does not directly use instances of the graph and network classes,
but utilizes smart pointers to those instances instead. The actual
instances in the Python program are of type :class:`PUNGraph`,
:class:`PNGraph`, or :class:`PNEAnet` and correspond to :class:`TUNGraph`,
:class:`TNGraph`, and :class:`TNEAnet`, respectively.

In general, if you need to call a class method, use **T** and
if you need to specify an instance type, use **P**. For example:

>>> G1 = snap.TNGraph.New()
>>> G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)

You can read more about smart pointers here:
http://snap.stanford.edu/snap/doc/snapdev-guide/#Smart_Pointers.

Graph Creation
``````````````

Graphs are created with the :meth:`New()` method.
Examples of how to create graphs and networks:

>>> G1 = snap.TUNGraph.New()
>>> G2 = snap.TNGraph.New()
>>> N1 = snap.TNEANet.New()


Adding Nodes and Edges
``````````````````````

Nodes are added with the :meth:`AddNode()` method.

>>> G1.AddNode(1)
>>> G1.AddNode(5)
>>> G1.AddNode(32)

Nodes have unique integer node ids.
There is no restriction for node ids to be contiguous integers starting at 0. 

Edges are added with the :meth:`AddEdge()` method.

>>> G1.AddEdge(1,5)
>>> G1.AddEdge(5,1)
>>> G1.AddEdge(5,32)

In TUNGraph and TNGraph edges have no explicit ids -- edges are identified by a pair of node ids.


Traversing Nodes and Edges
``````````````````````````

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
`````````````````````````

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

>>> G5 = snap.LoadEdgeList(snap.PNGraph, "test.txt", 0, 1)

Graph Manipulation
``````````````````

Snap.py provides rich functionality to efficiently manipulate graphs and networks. Most functions support all graph and network types. Below are a few examples of graph operations.

Generate a random Erdos-Renyi directed graph on 10000 nodes and with 5000 edges:

>>> G6 = snap.GenRndGnm(snap.PNGraph, 10000, 5000)

Convert a directed graph to an undirected graph:

>>> G7 = snap.ConvertGraph(snap.PUNGraph, G6)

Get the largest weakly connected component:

>>> WccG = snap.GetMxWcc(G6)

Generate a network using Forest Fire model:

>>> G8 = snap.GenForestFire(1000, 0.35, 0.35)

Get a subgraph induced on nodes {0,1,2,3,4}:

>>> SubG = snap.GetSubGraph(G8, snap.TIntV.GetV(0,1,2,3,4))

Get 3-core of G:

>>> Core3 = snap.GetKCore(G8, 3)

Delete nodes of out-degree 3 and in-degree 2:

>>> snap.DelDegKNodes(G8, 3, 2)

Computing Structural Properties
```````````````````````````````

Snap.py provides rich functionality to efficiently compute structural properties of networks. Most functions support all graph and network types.

Generate a random Erdos-Renyi directed graph on 10000 nodes and with 1000 edges:

>>> G9 = snap.GenRndGnm(snap.PNGraph, 10000, 1000)

Define a vector of pairs of integers (size, count) and get a distribution of connected components (component size, count):

>>> CntV = snap.TIntPrV()
>>> snap.GetWccSzCnt(G9, CntV)
>>> for p in CntV:
>>>     print "size %d: count %d" % (p.GetVal1(), p.GetVal2())

Get degree distribution pairs (out-degree, count):

>>> snap.GetOutDegCnt(G9, CntV)
>>> for p in CntV:
>>>     print "degree %d: count %d" % (p.GetVal1(), p.GetVal2())

Generate a Preferential Attachment graph on 100 nodes and out-degree of 3:

>>> G10 = snap.GenPrefAttach(100, 3)

Define a vector of floats and get first eigenvector of graph adjacency matrix:

>>> EigV = snap.TFltV() 
>>> snap.GetEigVec(G10, EigV)
>>> nr = 0
>>> for f in EigV:
>>>     nr += 1
>>>     print "%d: %.6f" % (nr, f)

Get an approximation of graph diameter:

>>> diam = snap.GetBfsFullDiam(G10, 10)

Count the number of triads:

>>> triads = snap.GetTriads(G10)

Get the clustering coefficient:

>>> cf = snap.GetClustCf(G10)

