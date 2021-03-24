Attributes
`````````````````````
The :class:`TNEANet` is one of the three main graph types in SNAP. Unlike
:class:`TUNGraph` and :class:`TNGraph`, which are simple undirected and directed
graphs, respectively, :class:`TNEANet` is a multigraph with functionality for
storing additional data associated with nodes and edges. These additional data
are known as **attributes**, and open up a wide range of possibility for tackling
more complex graph-related problems.

SNAP currently supports node and edge attributes of type *TInt*, *TFlt*,
*TStr*, *TIntV*, *TFltV*, and *TStrV*. Attributes can be added dynamically
at runtime, and by default attributes are internally organized in a columnar store,
where each attribute column is defined for all the nodes or edges in the network.
It is also possible to explicitly define an attribute to be sparse. Sparse attributes
are not organized as columns, rather they are only stored for the nodes/edges for
which they are defined.

This tutorial will cover:

* creating a TNEANet,
* basic attribute types and methods,
* vector attributes,
* attribute iterators,
* and sparse attributes.

For a more detailed explanation of :class:`TNEANet` functionality, please refer to :class:`TNEANet`.

.. seealso::

  SNAP C++ documentation has a complete list of attribute-related methods. Search for :class:`TNEANet` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.

Creating a :class:`TNEANet`
===========================
To create a new :class:`TNEANet` object, use one of the :meth:`New()` methods.
We can construct a :class:`TNEANet` object from scratch using :meth:`AddNode()`
and :meth:`AddEdge()` as follows::

      >>> import snap

      >>> N = snap.TNEANet.New()
      >>> N.AddNode(1)
      1
      >>> N.AddNode(2)
      2
      >>> N.AddNode(5)
      5
      >>> N.AddEdge(1, 5)
      0
      >>> N.AddEdge(1, 2)
      1
      >>> N.AddEdge(1, 2)
      2

It is also possible to save and load :class:`TNEANet` objects in various formats,
including text, XML, and compact binary. See http://snap.stanford.edu/snappy/doc/tutorial/tutorial.html#saving-and-loading-graphs
for how to save and load SNAP graphs/networks.

Basic Attributes
================
:class:`TNEANet` supports node and edge attributes for the three basic types in SNAP:
:class:`TInt`, :class:`TFlt`, and :class:`TStr`. To define a new integer, float, or
string node attribute, use the :meth:`AddIntAttrN()`, :meth:`AddFltAttrN()`,
and :meth:`AddStrAttrN()` methods, respectively. The analogous edge attribute
methods are :meth:`AddIntAttrE()`, :meth:`AddFltAttrE()`,
and :meth:`AddStrAttrE()`. You can think of calling one of these methods
as adding a new column into the underlying attribute table structure.
These methods return 0 on success and -1 on failure, for example if the attribute already exists.
Example usage of these methods is shown below::

    >>> N.AddIntAttrN('num_apples')
    0
    >>> N.AddFltAttrN('node_weight')
    0
    >>> N.AddStrAttrN('color')
    0
    >>> N.AddStrAttrN('color')  # this attribute already exists
    -1
    >>> N.AddIntAttrE('num_oranges')
    0
    >>> N.AddFltAttrE('edge_weight')
    0
    >>> N.AddStrAttrE('color')  # OK for an edge and node attribute to have the same name
    0

Note that it is not strictly necessary to define an attribute before assigning
a value to it for a node/edge since doing so automatically defines
the attribute if it did not previously exist. However, for clarity of code, we
recommend first defining all necessary attributes and then setting attribute values.
Attribute values can be set using the :meth:`AddIntAttrDatN()` and
other similar functions as follows::

    >>> N.AddIntAttrDatN(1, 100, 'num_apples')
    0
    >>> N.AddFltAttrDatN(2, 3.14, 'node_weight')
    0
    >>> N.AddStrAttrDatN(5, 'pink', 'color')
    0
    >>> N.AddIntAttrDatE(0, 42, 'num_oranges')
    0
    >>> N.AddFltAttrDatE(0, 1.23, 'edge_weight')
    0
    >>> N.AddStrAttrDatE(0, 'turqoise', 'color')
    0

Once attribute values have been set, it is possible to retrieve a vector of names
of attributes for a given node/edge as well as the values of these attributes.
Note that only attributes with an assigned value for the specified node/edge
are provided.

    >>> v = snap.TStrV()
    >>> N.AttrNameEI(0, v)  # get name of all attributes for edge 0 (1 --> 5)
    >>> for attr in v:
    ...   print(attr)
    num_oranges
    edge_weight
    color
    >>> N.FltAttrNameNI(2, v)  # there are also methods for specific types of attributes
    >>> for attr in v:
    ...   print(attr)
    node_weight
    >>> N.AttrValueEI(0, v)  # get value of all attributes for edge 0 (converted to string)
    >>> for val in v:
    ...   print(val)
    42
    1.23
    turqoise
    >>> v2 = snap.TIntV()
    >>> N.IntAttrValueEI(0, v2)  # there are also methods for specific types of attributes
    >>> for val in v2:
    ...   print(val)
    42

In addition to being able to retrieve a vector of all attribute names and values
for a given node or edge, it is also possible to retrieve the value of a specific
attribute::

    >>> N.GetIntAttrDatN(1, 'num_apples')
    100
    >>> N.GetFltAttrDatN(2, 'node_weight')
    3.14
    >>> N.GetStrAttrDatN(5, 'color')
    'pink'
    >>> N.GetStrAttrDatE(0, 'color')
    'turqoise'

Finally, it is also possible to delete the value of an attribute for a specific
node/edge or even delete the attribute entirely. Note that :meth:`IsAttrDeletedN()` and
other associated methods only return true if the attribute exists but has been deleted, ie its
value has been set to the default::

    >>> N.IsAttrDeletedN(1, 'num_apples')
    False
    >>> N.DelAttrDatN(1, 'num_apples')  # delete value, ie reset to default value
    0
    >>> N.IsAttrDeletedN(1, 'num_apples')
    True
    >>> N.IsIntAttrDeletedN(1, 'num_apples')  # like IsAttrDeletedN but for int attributes only
    True
    >>> N.DelAttrN('num_apples')  # delete the attribute entirely
    0

Vector Attributes
=================
In addition to the three basic types, SNAP :class:`TNEANet` also supports vector attributes, namely
attributes of type :class:`TIntV` and :class:`TFltV`. :class:`TStrV` attributes are currently unsupported.
Vector attributes can be useful for complex graph-related tasks where it is necessary to have vectors of data associated with nodes
and edges. There is currently limited support for sparse vectors (not to be confused with sparse attributes), ie
vectors which are stored using a sparse representation in memory. Vector attributes can be created similarly to non-vector attributes::

    >>> N.AddIntVAttrN('vec')
    0
    >>> N.AddFltVAttrE('edge_info')
    0
    >>> N.AddIntVAttrN('sparse_vec', snap.TBool(False))  # False means sparse vector representation
    0
    >>> N.AddFltVAttrE('sparse_edge_info', snap.TBool(False))
    0

Like with basic type attributes, we can assign values to vector attributes,

    >>> N.AddIntVAttrDatN(1, snap.TIntV(1), 'vec')  # TIntV(1) is a zero-filled vector of length 1
    0
    >>> N.AddIntVAttrDatN(2, snap.TIntV(2), 'sparse_vec', snap.TBool(False))  # False means sparse vector
    0
    >>> N.AddFltVAttrDatE(0, snap.TFltV(7), 'edge_info')
    0
    >>> N.AddFltVAttrDatE(0, snap.TFltV(10), 'sparse_edge_info', snap.TBool(False))
    0

query vector attribute names and values,

    >>> N.AttrNameEI(0, v)
    >>> for attr in v:
    ...   print(attr)
    num_oranges
    edge_weight
    color
    edge_info
    sparse_edge_info
    >>> checkv = N.GetIntVAttrDatN(1, 'vec')  # this method is not supported for sparse vectors
    >>> for item in checkv:
    ...   print(item)
    0

and delete vector attribute values. :meth:`DelAttrN()` and :meth:`DelAttrE()` are not currently compatible with
vector attributes.

    >>> N.IsFltVAttrDeletedE(0, 'edge_info')
    False
    >>> N.DelAttrDatE(0, 'edge_info')  # this method is not supported for sparse vectors
    0
    >>> N.IsFltVAttrDeletedE(0, 'edge_info')
    True

Additional functionality specific to vector attributes is that values can be appended to vector
attributes. For :class:`TIntV` attributes, values can also be deleted from vector attributes::

    >>> checkv = N.GetIntVAttrDatN(1, 'vec')
    >>> for item in checkv:
    ...   print(item)
    0
    >>> N.AppendIntVAttrDatN(1, 4, 'vec')
    0
    >>> checkv = N.GetIntVAttrDatN(1, 'vec')
    >>> for item in checkv:
    ...   print(item)
    0
    4
    >>> N.AppendFltVAttrDatE(0, 2021, 'edge_info')
    0
    >>> fltv = N.GetFltVAttrDatE(0, 'edge_info')
    >>> fltv[7]
    2021.0
    >>> N.DelFromIntVAttrDatN(1, 0, 'vec')  # delete value 0 from vector
    >>> checkv = N.GetIntVAttrDatN(1, 'vec')
    >>> for item in checkv:
    ...   print(item)
    4

Attribute Iterators
===================
Similar to node and edge iterators, SNAP supports attribute iterators. For example,
an integer node attribute iterator can be used to iterate through all nodes and get
the value of the attribute at each node. Currently, vector attribute iterators are not
supported, SNAP supports integer, float, and string attribute iterators, or :class:`TNEANetAIntI`,
:class:`TNEANetAFltI`, and :class:`TNEANetAStrI`, respectively. Attribute iterators can be
used to obtain attribute values as well as check whether the attribute has been deleted from
a given node/edge. The following example demonstrates how to use basic type attribute iterators::

    >>> EI = N.BegEAIntI('num_oranges')  # integer edge attribute iterator
    >>> while EI < N.EndEAIntI('num_oranges'):
    ...   print(EI.IsDeleted(), EI.GetDat())
    ...   EI.Next()  # move iterator to the next edge in the network
    False 42
    True -2147483648  # default value since not defined for edges 1 and 2
    True -2147483648
    >>> NI = N.BegNAStrI('color')
    >>> while NI < N.EndNAStrI('color'):
    ...   print(NI.IsDeleted(), NI.GetDat())
    ...   NI.Next()
    True  # iterates from nodes 0 through 5 even though we only explicitly defined nodes 1, 2, and 5
    True
    False pink  # only node 2 has 'color' defined
    True
    True
    True

Sparse Attributes
=================
All of the above examples use normal attributes, which are dense by default. Support for
sparse attributes, that is attributes which are not organized as columns but instead are only stored
for the nodes/edges for which they are defined, is in the process of being implemented. Like normal attributes,
sparse attributes can be created, queried, and deleted. Unlike normal attributes, an attribute ID must be
manually specified on creation. Currently, sparse attributes of vector types are not supported::

    >>> N.AddSAttrN('sparse_int', snap.atInt, 0)  # 0 is the attribute ID
    0
    >>> N.AddSAttrE('sparse_flt', snap.atFlt, 1)
    0
    >>> N.AddSAttrE('sparse_str', snap.atStr, 2)
    0
    >>> N.AddSAttrDatN(1, 'sparse_int', 10)
    0
    >>> N.AddSAttrDatE(0, 'sparse_flt', 0.5)
    0
    >>> N.AddSAttrDatE(2, 'sparse_str', 'SNAP is awesome!')
    0
    >>> N.DelSAttrDatN(1, 'sparse_int')
    0
    >>> N.DelSAttrDatE(0, 'sparse_flt')
    0
    >>> N.DelSAttrDatE(2, 'sparse_str')
    0
    >>> N.DelSAttrDatE(1, 'sparse_str')  # fails since 'sparse_str' attribute not defined for edge 1
    -1

Congratulations on completing this tutorial!
