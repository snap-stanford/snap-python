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
           TPair(Val1, Val2)

   
   Creates a TPair object consisting of the two values, if provided. If *Val1* and
   *Val2* are not given, the default value for each of their respective types is used.

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

     .. describe:: V[Index]

        Returns the value at index *Index* in vector *v*.

     .. describe:: V[Index] = Value

        Set ``V[Index]`` to *Value*.

     .. describe:: del V[Index]

        Removes the value at index *index* from the vector.

     .. describe:: Val in V

        Return ``True`` if *Val* is a value stored in vector *V*, else ``False``.

     .. describe:: Val not in V

        Equivalent to ``not Val in V``.

     .. iter(V)

        Returns an iterator over all the values in the vector.

     .. describe:: GetMemUsed()

        Returns the size of the vector object in bytes.

     .. describe:: GetPrimHashCd()

        Returns the primary hash code for the vector.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code for the vector.

     .. describe:: Gen(Vals)
                   Gen(MxVals, Vals)

        Resizes the vector to hold *Vals* and initializes each position in the vector 
        with the default value for the given type of the vector (i.e. 0 for TInt). If 
        *MxVals* is provided, the function reserves enough memory for *MxVals* values in 
        the vector.

     .. describe:: Reserve(MxVals)
                   Reserve(MxVals, Vals)

        Reserves enough memory for *MxVals* values in the vector. If *Vals* is 
        provided, it resizes the vector to hold *NumVals* and initializes each position 
        in the vector with the default value for the given type of the vector.

     .. describe:: Clr()

        Clears the contents of the vector.

     .. describe:: Trunc(Vals=-1)

        Truncates the vector to length *NumVals*. If *Vals* is not given, the vector 
        is left unchanged.

     .. describe:: Pack()

        The vector reduces its capacity (frees memory) to match its size. 

     .. describe:: MoveFrom(Vec)

        Moves all the data from *Vec* into the current vector and changes its capacity to
        match that of *Vec*. The contents and capacity of vec are cleared in the process.

     .. describe:: Swap(Vec)

        Swaps the contents and the capacity of the current vector with *Vec*.

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
        describe:: Add(Val)
        describe:: Add(Val, ResizeLen)

        Appends *Val* to the end of the vector. If *val* is not specified, it adds an 
        element with the default value for the given type of the vector. Returns the 
        index at which the value was appended. If *ResizeLen* is given, it increases the 
        capacity of the vector by *ResizeLen*. 

     .. describe:: AddV(ValV)

        Appends the contents of the vector *ValV* onto the vector. Returns the index of 
        the last element in the vector.

     .. describe:: AddSorted(Val, Asc=True)

        Adds *Val* to a sorted vector. If *Asc* is True, the vector is sorted in 
        ascending order.

     .. describe:: AddBackSorted(Val, Asc)

        Adds *Val* to a sorted vector. If *Asc* is True, the vector is sorted in 
        ascending order.

     .. describe:: AddMerged(Val)

        Adds element *Val* to a sorted vector only if the element *val* is not already 
        in the vector. Returns the index at which *val* was inserted or -1.

     .. describe:: AddVMerged(ValV)

        Adds elements of *ValV* to a sorted vector only if a particular element is not 
        already in the vector. Returns the new length of the vector.

     .. describe:: AddUnique(Val)

        Adds element *Val* to a vector only if the element *val* is not already in the 
        vector. Returns the index at which *val* was inserted or -1.

     .. describe:: GetVal(ValN)

        Returns the value at index *ValN*.

     .. describe:: SetVal(ValN, Val)

        Sets the value of the element at index *ValN* to *Val*.

     .. describe:: GetSubValV(BValN, EValN, vec)

        Fills *ValV* with the elements at positions *BValN* to *EValN*, inclusive, in this 
        vector.

     .. describe:: Ins(ValN, Val)

        Inserts the value *Val* into the vector before the element at position *ValN*.

     .. describe:: Del(ValN)

        Deletes the value at index *ValN*.

     .. describe:: Del(MnValN, MxValN)

        Deletes all elements from index *MnValN* to *MxValN*, inclusive.

     .. describe:: DelLast()

        Deletes the last element in the vector.

     .. describe:: DelIfIn(Val)

        Deletes the first instance of value *val* from the vector. Returns a boolean 
        indicating whether *Val* was found in the vector.

     .. describe:: DelAll(Val)

        Deletes all occurrences of *Val* from the vector.

     .. describe:: PutAll(Val)

        Sets all elements of the vector to value *Val*. 

     .. describe:: Swap(ValN1, ValN2)

        Swaps elements at positions *ValN1* and *ValN2*. 

     .. describe:: NextPerm()

        Generates next permutation of the elements in the vector. Returns a boolean
        indicating whether the previous permutation is different from the original 
        permutation.

     .. describe:: GetPivotValN(LValN, RValN)

        Picks three random elements at positions *LValN*...*RValN* and returns the 
        index of the middle one. 

     .. describe:: BSort(MnLValN, MxRValN, Asc)

        Bubble sorts values in the portion of the vector starting at *MnLVal* and ending 
        at *MxRValN*. If *Asc* is True, it sorts the vector in ascending order.

     .. describe:: ISort(MnLValN, MxRValN, Asc)

        Insertion sorts the values in the portion of the vector starting at *MnLVal* and 
        ending at *MxRValN*. If *Asc* is True, it sorts the vector in ascending order.

     .. describe:: Partition(MnLValN, MxRValN, Asc)

        Partitions the values in the portion of the vector starting at *MnLVal* and 
        ending at *MxRValN*. If *Asc* is True, it partitions using ascending order.

     .. describe:: QSort(MnLValN, MxRValN, Asc)

        Quick sorts the values in the portion of the vector starting at *MnLVal* and 
        ending at *MxRValN*. If *Asc* is True, it sorts the vector in ascending order.

     .. describe:: Sort(Asc)

        Sorts the vector. If *Asc* is True, it sorts it in ascending order.

     .. describe:: IsSorted(Asc)

        Checks whether the vector is sorted in ascending (if *Asc* == True) or 
        descending (if *Asc* == False) order. 

     .. describe:: Shuffle(Rnd)

        Shuffles the contents of the vector in random order, using the TRnd object *Rnd*.

     .. describe:: Reverse()

        Reverses the contents of the vector.

     .. describe:: Reverse(LValN, RValN)

        Reverses the order of elements in the portion of the vector starting at index 
        *LValN* and ending at *RValN*.

     .. describe:: Merge()

        Sorts the vector and only keeps a single element of each value. 

     .. describe:: Intrs(ValV)

        Updates this vector with the intersection of this vector with *ValV*. 

     .. describe:: Union(ValV)

        Updates this vector with the union of this vector with *ValV*.

     .. describe:: Diff(ValV)

        Updates this vector with the difference of this vector with *ValV*.

     .. describe:: Intrs(ValV, DstValV)

        *DstValV* is the intersection of vectors this and *ValV*.  

     .. describe:: Union(ValV, DstValV)

        *DstValV* is the union of vectors this and *ValV*. 

     .. describe:: Diff(ValV, DstValV)

        *DstValV* is the difference of vectors this and *ValV*. 

     .. describe:: IntrsLen(ValV)

        Returns the length of the intersection of this vector with *ValV*. 

     .. describe:: UnionLen(ValV)

        Returns the length of the union of this vector with *ValV*.

     .. describe:: Count(Val)

        Returns the number of times *Val* appears in the vector.

     .. describe:: SearchBin(Val)

        Returns the index of an element with value *Val* or -1.

     .. describe:: SearchForw(Val, BValN=0)

        Returns the index of an element with value *Val* or -1. Starts looking at
        index *BValN*.

     .. describe:: SearchBack(Val)

        Returns the index of an element wiht value *Val* or -1.

     .. describe:: SearchVForw(ValV, BValN=0)

        Returns the starting position of vector *ValV* or -1. Starts looking at
        index *BValN*.

     .. describe:: IsIn(Val)

        Returns a bool checking whether element *Val* is a member of the vector. 

     .. describe:: GetMxValN()

        Returns the position of the largest element in the vector. 

   Below is a list of static functions supported by the TVec class:

     .. describe:: GetV(Val1)
                   GetV(Val1, Val2)
                   GetV(Val1, Val2, Val3)
                   GetV(Val1, Val2, Val3, Val4)
                   GetV(Val1, Val2, Val3, Val4, Val5)
                   GetV(Val1, Val2, Val3, Val4, Val5, Val6)
                   GetV(Val1, Val2, Val3, Val4, Val5, Val6, Val7)
                   GetV(Val1, Val2, Val3, Val4, Val5, Val6, Val7, Val8)
                   GetV(Val1, Val2, Val3, Val4, Val5, Val6, Val7, Val8, Val9)

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

Hash tables contain values of the same type. Each value has a user provided key associated with it. All the keys are of the same type. Table values can be accessed or changed through their keys. New values can be added as `(key, value)` pairs. All objects classified as THash objects have access to the following methods.

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

     .. describe:: H[Key]

        Returns the item of *H* with key *Key*.

     .. describe:: H[Key] = Value

        Set ``H[Key]`` to *Value*.

     .. describe:: del H[Key]

        Removes ``H[Key]`` from *H*.

     .. describe:: Key in H

        Return ``True`` if *Key* is a key in hash table *H*, else ``False``.

     .. describe:: Key not in H

        Equivalent to ``not Key in H``.

     .. iter(H)

        Returns an iterator over all the keys in the hash table.

     .. describe:: GetMemUsed()

        Returns the size of the hash table in bytes.

     .. describe:: BegI()

        Returns an iterator to the beginning of the hash table.

     .. describe:: EndI()

        Returns an iterator to the end of the hash table.

     .. describe:: GetI(Key)

        Returns an iterator starting at the node with key value *Key*.

     .. describe:: Clr(DoDel=True, NoDelLim=-1, ResetDat=True)

        Clears the contents of the hash table.

     .. describe:: Empty()

        Returns a boolean indicating whether the hash table is empty.

     .. describe:: Len()

        Returns the the number of key-value pairs in the hash table.

     .. describe:: GetPorts()

        Returns the number of ports.

     .. describe:: IsAutoSize()

        Returns whether it is auto-size?

     .. describe:: GetMxKeyIds()

        Returns the first key id that is larger than all those currently stored in the 
        hash table.

     .. describe:: GetReservedKeyIds()

        Returns the size of the allocated storage capacity for the hash table.

     .. describe:: IsKeyIdEqKeyN()

        Returns a boolean whether there have been any gaps in the key ids, which can occur if a key is deleted and the hash table has not been defraged.

     .. describe:: AddKey(Key)

        Adds key *Key* to the hash table and returns the key id.

     .. describe:: AddDatId(Key)

        Adds a key-value mapping to the hash table, using *Key* as the key and the key id of *Key* as the value. The value is then returned.

     .. describe:: AddDat(Key)

        Adds a key-value mapping to the hash table, using *Key* as the key and the default value for the datatype as the value (i.e. for TInt values, the default value would be 0) if *Key* was not already in the hash table. If *Key* was already in the hash table, the value remains unchaned. The value is then returned.

     .. describe:: AddDat(Key, Dat)

        Adds a key-value mapping to the hash table, using *Key* as the key and *Dat* as the value. The value, *Dat*, is then returned.

     .. describe:: DelKey(Key)

        Removes the mapping using *Key* as the key from the hash table. Raises an exception if *Key* is not a key in the hash table.

     .. describe:: DelIfKey(Key)

        Removes the mapping using *Key* as the key from the hash table if it exists. Returns a boolean indicating whether *Key* was a key in the hash table.

     .. describe:: DelKeyId(KeyId)

        Removes the mapping using the key with id *KeyId* from the hash table. Raises an exception if *KeyId* is not a valid id for a key in the hash table.

     .. describe:: DelKeyIdV(KeyIdV)

        Removes all the mappings that use a key with an id in *KeyIdV* from the hash table. Raises an exception if one of the key ids in *KeyIdV* is not a valid id for a key in the hash table.

     .. describe:: GetKey(KeyId)

        Returns the key with id *KeyId*.

     .. describe:: GetKeyId(Key)

        Returns the key id for key *Key*.

     .. describe:: GetRndKeyId(Rnd)

        Get an index of a random element. If the hash table has many deleted keys, this may take a long time. 

     .. describe:: GetRndKeyId (Rnd, EmptyFrac)

        Get an index of a random element. If the hash table has many deleted keys, defrag the hash table first. 

     .. describe:: IsKey(Key)

        Returns a bool indicating whether *Key* is a key in the hash table.

     .. describe:: IsKey(Key, KeyId)

        Returns a bool indicating whether *Key* is a key in the hash table with id *KeyId*.

     .. describe:: IsKeyId(KeyId)

        Returns a bool indicating whether there is a key in the hash table with id *KeyId*.

     .. describe:: GetDat(Key)

        Returns the value in the hash table that *Key* maps to.

     .. describe:: FFirstKeyId()

        Returns -1, which is 1 less than the smallest possible key id, 0.

     .. describe:: GetKeyV(KeyV)

        Adds all the keys in the hash table to the vector *KeyV*.

     .. describe:: GetDatV(DatV)

        Adds all the values/data in the hash table to the vector *DatV*.

     .. describe:: GetKeyDatPrV(KeyDatPrV)

        Adds all the key-value pairs (as TPair objects) to the vector *KeyDatPrV*.

     .. describe:: GetDatKeyPrV(DatKeyPrV)

        Adds all the value-key pairs (as TPair objects) to the vector *DatKeyPrV*.

     .. describe:: Swap(Hash)

        Swaps the contents of this hash table with those of *Hash*.

     .. describe:: Defrag()

        Defrags the hash table.

     .. describe:: Pack()

        Reduces the capacity of the memory used to hold the hash table to match its size.

     .. describe:: Sort(CmpKey, Asc)

        Sorts the hash table. If *CmpKey* is True, it sorts based on keys rather than values.

     .. describe:: SortKey(Asc)

        Sorts the hash table based on keys.

     .. describe:: SortDat(Asc)

        Sorts the hash table based on the values.

   Below is some code demonstrating the use of the THash type:

      >>> h1 = snap.TIntH()
      >>> for i in range(10):
      ...     h1[i] = i + 1
      ...
      >>> h2 = snap.TIntH(h1)
      >>> del h2[0]
      >>> h1.Swap(h2)
      >>> h1.IsKey(0)
      False
