Composite Types
````````````````

Composite types in SNAP are :class:`TPair`, :class:`TVec`, :class:`THash`, and 
:class:`TSet`.

TPair
=====

The name TPair refers to a general data structure that consists of two values, which can 
be of different types. All of the following methods are available for objects that are 
classified as TPair objects. 

.. class:: TPair()
           TPair(val1, val2)

   
   Createsa TPair object consisting of the two values, if provided. If *val1* and
   *val2* are not given, the default value for each of their respective types is used.

   The TPair constructor cannot be directly used. To create a TPair object, the correct
   constructor must be chosen, which indicates the types of both the values in the pair.
   The naming convention for the constructor/type is as follows: the `<type_name_1>` of
   the first object in the pair, the `<type_name_2>` for the second object in the pair 
   (without the `T`), and finally a `V`. If `<type_name_1>` and `<type_name_2>` are the 
   same, then the TPair type will be the `<type_name>` and finally a `V`.

   To illustrate, the following examples all return a TPair of two ints (TInts) with both
   values set to 0::

      >>> snap.TIntPr(0, 0)
      >>> snap.TIntPr(snap.TInt(0), snap.TInt(0))
      >>> snap.TIntPr()

   The following public functions are supported by the TPair class:

     .. describe:: GetMemUsed()

        Returns the size of the TPair object in bytes.

     .. describe:: GetVal1()

        Returns the first value in the TPair.

     .. describe:: GetVal2()

        Returns the second value in the TPair.

     .. describe:: GetPrimHashCd()

        Returns an int hash code using the primary hash codes of the two values in the
        pair.

     .. describe:: GetSecHashCd()

        Returns an int hash code using the secondary hash codes of the two values in the
        pair.

   The following public attributes are available:

     .. describe:: Val1

        The first value in the pair. Supports assignment, which requires the use of 
        SNAP.py types rather than Python types.

     .. describe:: Val2

        The second value in the pair. Supports assignment, which requires the use of 
        SNAP.py types rather than Python types.


   Below is some code demonstrating the use of the TPair type:

      >>> pr = snap.TIntPr(10, 15)
      >>> print pr.Val1.Val
      10
      >>> pr.Val1 = snap.TInt(21)
      >>> print pr.Val1.Val
      21
      >>> pr.GetPrimHashCd()
      687

TVec
=====

Vectors are sequences of values of the same type. Existing vector values can be accessed 
or changed by their index in the sequence. New values can be added at the end of a 
vector. All of the following methods are available for objects that are classified as
TVec objects. 

.. class:: TVec()
           TVec(NumVals)
           TVec(MxVals, NumVals)
           TVec(Vec)

   
   Creates a TVec object of size *NumVals*, if specified. It *MxVals* is given, enough
   memory to store *MxVals* will be reserved. MxVals must be larger than *NumVals*. If
   *Vec* - a TVec of the same type - is given, the values from *Vec* are copied into the
   new TVec.

   The TVec constructor cannot be directly used. To create a TVec object, the correct
   constructor must be chosen, which indicates the type stored in the TVec.
   Vector types in Snap.py and SNAP use a naming convention of being named as 
   `<type_name>`, followed by `V`. For example, a vector of integers is named
   :class:`TIntV`. 

   To illustrate, the following examples show how to create a TVec with each of the
   constructors::

      >>> snap.TIntV()
      >>> snap.TIntV(5)
      >>> v1 = snap.TIntV(8, 5)
      >>> v1.Add(1)
      >>> v2 = snap.TIntV(v1)
      >>> for val in v2:
      ...     print val
      ...
      1

   The following public functions are supported by the TVec class:

     .. describe:: v[index]

        Returns the value at index *index* in vector *v*.

     .. describe:: v[index] = value

        Set ``v[index]`` to *value*.

     .. describe:: del v[index]

        Removes the value at index *index* from the vector.

     .. describe:: val in v

        Return ``True`` if *val* is a value stored in vector *v*, else ``False``.

     .. describe:: val not in v

        Equivalent to ``not val in v``.

     .. iter(v)

        Returns an iterator over all the values in the vector.

     .. describe:: GetMemUsed()

        Returns the size of the vector object in bytes.

     .. describe:: GetPrimHashCd()

        Returns the primary hash code for the vector.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code for the vector.

     .. describe:: Gen(NumVals)
                   Gen(MxVals, NumVals)

        Resizes the vector to hold *NumVals* and initializes each position in the vector 
        with the default value for the given type of the vector (i.e. 0 for TInt). If 
        *MxVals* is provided, the function reserves enough memory for *MxVals* values in 
        the vector.

     .. describe:: Reserve(MxVals)
                   Reserve(MxVals, NumVals)

        Reserves enough memory for *MxVals* values in the vector. If *NumVals* is 
        provided, it resizes the vector to hold *NumVals* and initializes each position 
        in the vector with the default value for the given type of the vector.

     .. describe:: Clr()

        Clears the contents of the vector.

     .. describe:: Trunc(NumVals=-1)

        Truncates the vector to length *NumVals*. If *NumVals* is not given, the vector 
        is left unchanged.

     .. describe:: Pack()

        The vector reduces its capacity (frees memory) to match its size. 

     .. describe:: MoveFrom(vec)

        Moves all the data from *vec* into the current vector and changes its capacity to
        match that of *vec*. The contents and capacity of vec are cleared in the process.

     .. describe:: Swap(vec)

        Swaps the contents and the capacity of the current vector with *vec*.

     .. describe:: Empty()

        Returns a bool indicating whether the vector is empty.

     .. describe:: Len()

        Returns the length of the vector.

     .. describe:: Reserved()

        Returns the reserved capacity for the vector.

     .. describe:: Last()

        Returns the last value in the vector.

     .. describe:: LastValN()

        Returns the index of the last value in the vector.

     .. describe:: LastLast()

        Returns the second to last element in the vector.

     .. describe:: Add()
        describe:: Add(val)
        describe:: Add(val, capInc)

        Appends *val* to the end of the vector. If *val* is not specified, it adds an 
        element with the default value for the given type of the vector. Returns the 
        index at which the value was appended. If *capInc* is provided, it increases the 
        capacity of the vector by *capInc*. 

     .. describe:: AddV(vec)

        Appends the contents of the vector *vec* onto the vector. Returns the index of 
        the last element in the vector.

     .. describe:: AddSorted(val, isAsc=True)

        Adds *val* to a sorted vector. If *isAsc* is True, the vector is sorted in 
        ascending order.

     .. describe:: AddBackSorted(val, isAsc)

        Adds *val* to a sorted vector. If *isAsc* is True, the vector is sorted in 
        ascending order.

     .. describe:: AddMerged(val)

        Adds element *val* to a sorted vector only if the element *val* is not already 
        in the vector. Returns the index at which *val* was inserted or -1.

     .. describe:: AddVMerged(vec)

        Adds elements of *vec* to a sorted vector only if a particular element is not 
        already in the vector. Returns the new length of the vector.

     .. describe:: AddUnique(val)

        Adds element *val* to a vector only if the element *val* is not already in the 
        vector. Returns the index at which *val* was inserted or -1.

     .. describe:: GetVal(index)

        Returns the value at index *index*.

     .. describe:: SetVal(index, newVal)

        Sets the value of the element at index *index* to *newVal*.

     .. describe:: GetSubValV(start, end, vec)

        Fills *vec* with the elements at positions *start* to *end*, inclusive, in this 
        vector.

     .. describe:: Ins(index, val)

        Inserts the value *val* into the vector before the element at position *index*.

     .. describe:: Del(index)

        Deletes the value at index *index*.

     .. describe:: Del(start, end)

        Deletes all elements from index *start* to *end*, inclusive.

     .. describe:: DelLast()

        Deletes the last element in the vector.

     .. describe:: DelIfIn(val)

        Deletes the first instance of value *val* from the vector. Returns a boolean 
        indicating whether *val* was found in the vector.

     .. describe:: DelAll(val)

        Deletes all occurrences of *val* from the vector.

     .. describe:: PutAll(val)

        Sets all elements of the vector to value *val*. 

     .. describe:: Swap(index1, index2)

        Swaps elements at positions *index1* and *index2*. 

     .. describe:: NextPerm()

        Generates next permutation of the elements in the vector. Returns a boolean
        indicating whether the previous permutation is different from the original 
        permutation.

     .. describe:: GetPivotValN(index1, index2)

        Picks three random elements at positions *index1*...*index2* and returns the 
        index of the middle one. 

     .. describe:: BSort(mnLValN, mxRValN, isAsc)

        Bubble sorts values in the portion of the vector starting at *mnLVal* and ending 
        at *MxRValN*. If *isAsc* is True, it sorts the vector in ascending order.

     .. describe:: ISort(mnLValN, mxRValN, isAsc)

        Insertion sorts the values in the portion of the vector starting at *mnLVal* and 
        ending at *MxRValN*. If *isAsc* is True, it sorts the vector in ascending order.

     .. describe:: Partition(mnLValN, mxRValN, isAsc)

        Partitions the values in the portion of the vector starting at *mnLVal* and 
        ending at *MxRValN*. If *isAsc* is True, it partitions using ascending order.

     .. describe:: QSort(mnLValN, mxRValN, isAsc)

        Quick sorts the values in the portion of the vector starting at *mnLVal* and 
        ending at *MxRValN*. If *isAsc* is True, it sorts the vector in ascending order.

     .. describe:: Sort(isAsc)

        Sorts the vector. If *isAsc* is True, it sorts it in ascending order.

     .. describe:: IsSorted(isAsc)

        Checks whether the vector is sorted in ascending (if *isAsc*=True) or 
        descending (if *isAsc*=False) order. 

     .. describe:: Shuffle(rnd)

        Shuffles the contents of the vector in random order, using the TRnd object *rnd*.

     .. describe:: Reverse()

        Reverses the contents of the vector.

     .. describe:: Reverse(start, end)

        Reverses the order of elements in the portion of the vector starting at index 
        *start* and ending at *end*.

     .. describe:: Merge()

        Sorts the vector and only keeps a single element of each value. 

     .. describe:: Intrs(vec)

        Updates this vector with the intersection of this vector with *vec*. 

     .. describe:: Union(vec)

        Updates this vector with the union of this vector with *vec*.

     .. describe:: Diff(vec)

        Updates this vector with the difference of this vector with *vec*.

     .. describe:: Intrs(vec, dst)

        *dst* is the intersection of vectors this and *vec*.  

     .. describe:: Union(vec, dst)

        *dst* is the union of vectors this and *vec*. 

     .. describe:: Diff(vec, dst)

        *dst* is the difference of vectors this and *vec*. 

     .. describe:: IntrsLen(vec)

        Returns the lenght of the intersection of this vector with *vec*. 

     .. describe:: UnionLen(vec)

        Returns the length of the union of this vector with *vec*.

     .. describe:: Count(val)

        Returns the number of times *val* appears in the vector.

     .. describe:: SearchBin(val)

        Returns the index of an element with value *val* or -1.

     .. describe:: SearchForw(val, start=0)

        Returns the index of an element with value *val* or -1. Starts looking at
        index *start*.

     .. describe:: SearchBack(val)

        Returns the index of an element wiht value *val* or -1.

     .. describe:: SearchForw(vec, start=0)

        Returns the starting position of vector *vec* or -1. Starts looking at
        index *start*.

     .. describe:: IsIn(val)

        Returns a bool checking whether element *val* is a member of the vector. 

     .. describe:: GetMxValN()

        Returns the position of the largest element in the vector. 

   Below is a list of static functions supported by the TVec class:

     .. describe:: GetV(val1)
                   GetV(val1, val2)
                   GetV(val1, val2, val3)
                   GetV(val1, val2, val3, val4)
                   GetV(val1, val2, val3, val4, val5)
                   GetV(val1, val2, val3, val4, val5, val6)
                   GetV(val1, val2, val3, val4, val5, val6, val7)
                   GetV(val1, val2, val3, val4, val5, val6, val7, val8)
                   GetV(val1, val2, val3, val4, val5, val6, val7, val8, val9)

        Returns a vector with the given values.


   Below is some code demonstrating the use of the TVec type:

      >>> vec1 = snap.TIntV.GetV(1, 2, 3, 4, 5, 6, 7, 8, 9)
      >>> vec1.IsIn(5)
      True
      >>> vec2 = snap.TIntV(vec1)
      >>> vec2.Add(10)
      >>> vec2.Diff(vec1)
      >>> for val in vec2:
      ...     print val
      ...
      10


THash
=====

Hash tables contain values of the same type. Each value has a user provided key associated with it. All the keys are of the same type. Table values can be accessed or changed either their keys. New values can be added as `(key, value)` pairs. All objects classified as THash objects have access to the following methods.

.. class:: THash()
           THash(ExpectVals)
           THash(Hash)

   
   Creates a THash object with a capacity of *ExpectVals*, if specified.  If *Hash* - a
   THash of the same type - is given, the values from *Hash* are copied into the
   new THash.

   The THash constructor cannot be directly used. To create a THash object, the correct
   constructor must be chosen, which indicates the types of the key and value in the THash. Hash table types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name><value_type_name>`, followed by `H`. For example, a hash table 
   with integer key and string values is named :class:`TIntStrH`. If `<key_type_name>` 
   and `<value_type_name>` have the same type, only one type name might be used, such 
   as :class:`TIntH`.


   To illustrate, the following examples show how to create a THash with each of the
   constructors::

      >>> snap.TIntH()
      >>> h1 = snap.TIntH(5)
      >>> h1[5] = 5
      >>> h2 = snap.TIntH(h1)
      >>> for key in h2:
      ...     print key, h2[key]
      ...
      5 5

   The following public functions are supported by the THash class:

     .. describe:: h[key]

        Returns the item of *h* with key *key*.

     .. describe:: h[key] = value

        Set ``h[key]`` to *value*.

     .. describe:: del h[key]

        Removes ``h[key]`` from *h*.

     .. describe:: key in h

        Return ``True`` if *key* is a key in hash table *h*, else ``False``.

     .. describe:: key not in h

        Equivalent to ``not key in h``.

     .. iter(h)

        Returns an iterator over all the keys in the hash table.

     .. describe:: GetMemUsed()

        Returns the size of the hash table in bytes.

     .. describe:: BegI()

        Returns an iterator to the beginning of the hash table.

     .. describe:: EndI()

        Returns an iterator to the end of the hash table.

     .. describe:: GetI(key)

        Returns an iterator starting at the node with key value *key*.


   Below is a list of static functions supported by the THash class:


   Below is some code demonstrating the use of the THash type:
