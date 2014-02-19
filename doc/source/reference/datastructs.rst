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
  >>> h[6] = "six"
  >>> h[1] = "one"

- get the number of values in the table:

  >>> print h.Len()
  5

- get a value for a specific key

  >>> print "h[3] =", h.GetDat(3)
  h[3] = three
  >>> print "h[3] =", h[3]
  h[3] = three

- change a value at a specific key

  >>> h.AddDat(3,"four")
  >>> print "h[3] =", h.GetDat(3)
  h[3] = four
  >>> h[3] = "three"
  >>> print "h[3] =", h[3]
  h[3] = three

- print all values in a table using an iterator

  >>> for key in h:
  >>>     print key, h[key]
  5 five
  3 three
  9 nine
  6 six
  1 one

.. seealso::

  SNAP C++ documentation has a complete list of hash table methods. Search for :class:`THash` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.

Pair Types
``````````
Pairs contain two values. Each value has its own type.

Pair types in Snap.py and SNAP use a naming convention of being named as `<type1><type2>`, followed by `Pr`. For example, a pair of (integer, string) is named :class:`TIntStrPr`. If `<type1>` and `<type2>` have the same type, only one type name might be used, such as :class:`TIntPr`.

Below are the most commonly used pair operations:

- create a pair of an integer and a string:

  >>> p = snap.TIntStrPr(1, "one")

- print the first value:

  >>> print p.GetVal1()
  1

- print the second value:

  >>> print p.GetVal2()
  one

.. seealso::

  SNAP C++ documentation has a complete list of pair methods. Search for :class:`TPair` in: http://snap.stanford.edu/snap/doc/snapdev-ref/.
