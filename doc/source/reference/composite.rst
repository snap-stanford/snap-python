Composite Types
````````````````

Composite types in SNAP are :class:`TPair`, :class:`TVec`, :class:`THash`, and 
:class:`THashSet`.

TPair
=====

The name :class:`TPair` refers to a general data structure that consists of two values, which can be of different types. All of the following methods are available for objects that are classified as :class:`TPair` objects. 

.. class:: TPair()
           TPair(Val1, Val2)
           TPair(SIn)

   
   Creates a :class:`TPair` object consisting of the two values, if provided. If *Val1* and
   *Val2* are not given, the default value for each of their respective types is used.
   If *SIn* is provided, the pair of values are loaded from the binary stream *SIn*.

   The :class:`TPair` constructor cannot be directly called. To create a :class:`TPair` object, the correct
   constructor must be chosen, which indicates the types of both the values in the pair.
   The naming convention is as follows: `<type_name_1>` of
   the first object in the pair, `<type_name_2>` for the second object in the pair 
   (without the `T`), and finally a `Pr`. If `<type_name_1>` and `<type_name_2>` are the 
   same, then the name may be condensed to `<type_name>` followed by `Pr`.

   The following :class:`TPair` types are supported: :class:`TIntPr`, :class:`TFltPr`, 
   :class:`TIntStrPr`, :class:`TBoolFltPr`, :class:`TIntBoolPr`, :class:`TIntUInt64Pr`, 
   :class:`TIntIntPrPr`, :class:`TIntIntVPr`, :class:`TIntFltPr`, :class:`TIntStrVPr`, 
   :class:`TIntPrIntPr`, :class:`TUIntUIntPr`, :class:`TUIntIntPr`, :class:`TUInt64IntPr`, 
   :class:`TUInt64Pr`, :class:`TUint64FltPr`, :class:`TUInt64StrPr`, :class:`TFltIntPr`, 
   :class:`TFltUInt64Pr`, :class:`TFltStrPr`, :class:`TAscFltIntPr`, :class:`TAscFltPr`, 
   :class:`TAscFltStrPr`, :class:`TStrIntPr`, :class:`TStrFltPr`, :class:`TStrPr`, 
   :class:`TStrStrVPr`, :class:`TStrVIntPr`, :class:`TIntStrPrPr`, and :class:`TFltStrPrPr`.

   To illustrate, the following examples all return a :class:`TIntPr` with both values set to 0::

      >>> snap.TIntPr(0, 0)
      >>> snap.TIntPr(snap.TInt(0), snap.TInt(0))
      >>> snap.TIntPr()

   The following public functions are supported by the :class:`TPair` class:

     .. describe:: Load(SIn)

        Loads the pair from a binary stream *SIn*. 

     .. describe:: Save(SOut)

        Saves the pair to a binary stream *SOut*. 

     .. describe:: GetMemUsed()

        Returns the size of the :class:`TPair` object in bytes.

     .. describe:: GetVal1()

        Returns the first value in the :class:`TPair`.

     .. describe:: GetVal2()

        Returns the second value in the :class:`TPair`.

     .. describe:: GetPrimHashCd()

        Returns the primary hash code, which is computed using the primary hash codes of the two values in the pair.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code, which is computed using the secondary hash codes of the two values in the pair.

   The following public attributes are available:

     .. describe:: Val1

        The first value in the pair. Supports assignment, which requires the use of Snap.py types rather than Python types.

     .. describe:: Val2

        The second value in the pair. Supports assignment, which requires the use of Snap.py types rather than Python types.


   Below is some code demonstrating the use of the :class:`TPair` type:

      >>> pr = snap.TIntPr(10, 15)
      >>> print(pr.Val1.Val)
      10
      >>> pr.Val1 = snap.TInt(21)
      >>> print(pr.GetVal1())
      21
      >>> pr.GetPrimHashCd()
      687

TVec
=====

Vectors are sequences of values of the same type. Existing vector values can be accessed 
or changed by their index in the sequence. New values can be added at the end of a 
vector. All of the following methods are available for objects that are classified as
:class:`TVec` objects. 

.. class:: TVec()
           TVec(NumVals)
           TVec(MxVals, NumVals)
           TVec(Vec)
           TVec(SIn)

   
   Creates a :class:`TVec` object of size *NumVals*, if specified. It *MxVals* is given, enough
   memory to store *MxVals* will be reserved. MxVals must be larger than *NumVals*. If
   *Vec* - a :class:`TVec` of the same type - is given, the values from *Vec* are copied into the
   new :class:`TVec`. It *SIn* is provided, the contents of the vector are loaded from the binary stream *SIn*.

   The :class:`TVec` constructor cannot be directly called. To create a :class:`TVec` object, the correct
   constructor must be chosen, which indicates the type stored in the :class:`TVec`.
   Vector types in Snap.py and SNAP use a naming convention of being named as 
   `<type_name>`, followed by `V`. For example, a vector of integers is named
   :class:`TIntV`.

   The following :class:`TVec` types are supported: :class:`TIntV`, :class:`TFltV`, :class:`TIntPrV`, :class:`TFltPrV`, :class:`TIntTrV`, :class:`TIntFltKdV`, :class:`TBoolV`, :class:`TChV`, :class:`TUChV`, :class:`TUIntV`, :class:`TUInt64V`, :class:`TSFltV`, :class:`TAscFltV`, :class:`TStrV`, :class:`TChAV`, :class:`TIntQuV`, :class:`TFltTrV`, :class:`TUChIntPrV`, :class:`TUChUInt64PrV`, :class:`TIntUInt64PrV`, :class:`TIntUInt64KdV`, :class:`TIntFltPrV`, :class:`TIntFltPrKdV`, :class:`TFltIntPrV`, :class:`TFltUInt64PrV`, :class:`TFltStrPrV`, :class:`TAscFltStrPrV`, :class:`TIntStrPrV`, :class:`TIntIntStrTrV`, :class:`TIntIntFltTrV`, :class:`TIntFltIntTrV`, :class:`TIntStrIntTrV`, :class:`TIntKdV`, :class:`TUIntIntKdV`, :class:`TIntPrFltKdV`, :class:`TIntStrKdV`, :class:`TIntStrPrPrV`, :class:`TIntStrVPrV`, :class:`TIntIntVIntTrV`, :class:`TUInt64IntPrV`, :class:`TUInt64FltPrV`, :class:`TUInt64StrPrV`, :class:`TUInt64IntKdV`, :class:`TUInt64FltKdV`, :class:`TUInt64StrKdV`, :class:`TFltBoolKdV`, :class:`TFltIntKdV`, :class:`TFltUInt64KdV`, :class:`TFltIntPrKdV`, :class:`TFltKdV`, :class:`TFltStrKdV`, :class:`TFltStrPrPrV`, :class:`TFltIntIntTrV`, :class:`TFltFltStrTrV`, :class:`TAscFltIntPrV`, :class:`TAscFltIntKdV`, :class:`TStrPrV`, :class:`TStrIntPrV`, :class:`TStrIntKdV`, :class:`TStrFltKdV`, :class:`TStrAscFltKdV`, :class:`TStrTrV`, :class:`TStrQuV`, :class:`TStrFltFltTrV`, :class:`TStrStrIntTrV`, :class:`TStrKdV`, :class:`TStrStrVPrV`, :class:`TStrVIntPrV`, :class:`TFltIntIntIntQuV`, :class:`TIntStrIntIntQuV`, and :class:`TIntIntPrPrV`.

   To illustrate, the following examples show how to create a :class:`TVec`::

      >>> snap.TIntV()
      >>> snap.TIntV(5)
      >>> v1 = snap.TIntV(8, 5)
      >>> v1.append(1)
      >>> v2 = snap.TIntV(v1)
      >>> for val in v2:
      ...     print(val)
      ...
      1

   :class:`TVec` offers iterators of type :class:`TInt` for fast access through the vector.
   The :class:`TInt` returned by any iterator method represents the value at a given index in the vector.

   The following public functions are Python list functions that are also supported by the :class:`TVec` class:
     .. describe:: V[Index]

        Returns the value at index *Index* in vector *v*.

     .. describe:: V[Index] = Value

        Set ``V[Index]`` to *Value*.

     .. describe:: del V[Index]

        Removes the value at index *index* from the vector.

     .. describe:: Val in V

        Returns ``True`` if *Val* is a value stored in vector *V*, else ``False``.

     .. describe:: Val not in V

        Equivalent to ``not Val in V``.

     .. describe:: append(Val)
     	
	Appends *Val* to the end of the vector.

     .. describe:: len()
     
	Returns the length of the vector.

     .. describe:: delitem(Index)
     
	Deletes the value at index *Index* from the vector.

     .. describe:: extend(Vec)
     
          Appends the contents of another vector, *Vec*, to the end of the vector.

     .. describe:: clear()
     
	Clears the contents of the vector.
	
     .. describe:: insert(Index, Val)

        Inserts *Val* into the vector at index *Index*.

     .. describe:: remove(Val)

        Deletes the first instance of *Val* from the vector. If the value is not found, an error is thrown.

     .. describe:: index(Val)

        Returns the index of the first instance of *Val* in the vector. If the value is not found, an error is thrown.

     .. describe:: count(Val)

          Returns a count of the number of instances of *Val* in the vector.

     .. describe:: pop(Index)

        Deletes the contents of the vector at index *Index* and returns the value from that index.

     .. describe:: reverse() 

        Reverses the contents of the vector.

     .. describe:: sort(asc=False)

          Sorts the vector. If *Asc* is true, sorts in ascending order; otherwise in descending order.

     .. describe:: copy()

        Returns a copy of the vector.


   The following public functions are additional, SNAP-specific functions supported by the :class:`TVec` class:

     .. iter(V)

        Returns an iterator over all the values in the vector.

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

     .. describe:: Load(SIn)

        Loads a graph from a binary stream *SIn* and returns a pointer to it. 

     .. describe:: Save(SOut)

        Saves the graph to a binary stream *SOut*. 

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

        Truncates the vector to length *Vals*. If *Vals* is not given, the vector 
        is left unchanged.

     .. describe:: Pack()

        The vector reduces its capacity (frees memory) to match its size. 

     .. describe:: MoveFrom(Vec)

        Moves all the data from *Vec* into the current vector and changes its capacity to
        match that of *Vec*. The contents and capacity of *Vec* are cleared in the process.

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

     .. describe:: BegI()

        Returns an iterator pointing to the first element in the vector. 

     .. describe:: EndI()

        Returns an iterator referring to the past-the-end element in the vector. 

     .. describe:: GetI(ValN)

        Returns an iterator an element at position *ValN*. 

     .. describe:: Add()
                   Add(Val)
                   Add(Val, ResizeLen)

        Appends *Val* to the end of the vector. If *Val* is not specified, it adds an 
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

        Picks three random elements at positions *LValN* ... *RValN* and returns the 
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

        Shuffles the contents of the vector in random order, using the :class:`TRnd` object *Rnd*.

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



   Below is some code demonstrating the use of the :class:`TVec` type:

      >>> vec1 = snap.TIntV.GetV(1, 2, 3, 4, 5, 6, 7, 8, 9)
      >>> vec1.IsIn(5)
      True
      >>> vec2 = snap.TIntV(vec1)
      >>> vec2.Add(10)
      >>> vec2.Diff(vec1)
      >>> for val in vec2:
      ...     print(val)
      ...
      10


THash
=====

Hash tables contain values of the same type. Each value has a user provided key associated with it. All the keys are of the same type. Table values can be accessed or changed through their keys. New values can be added as `(key, value)` pairs. All objects classified as :class:`THash` objects have access to the following methods.

.. class:: THash()
           THash(ExpectVals, AutoSizeP=False)
           THash(Hash)
           THash(SIn)

   
   Creates a :class:`THash` object with a capacity of *ExpectVals*, if specified.  If *Hash* - a
   :class:`THash` of the same type - is given, the values from *Hash* are copied into the
   new :class:`THash`. If *SIn* is provided, the contents of the hash table are loaded from the binary stream *SIn*.

   The :class:`THash` constructor cannot be directly called. To create a :class:`THash` object, the correct
   constructor must be chosen, which indicates the types of the key and value in the :class:`THash`. Hash table types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name><value_type_name>`, followed by `H`. For example, a hash table 
   with integer key and string values is named :class:`TIntStrH`. If `<key_type_name>` 
   and `<value_type_name>` have the same type, only one type name might be used, such 
   as :class:`TIntH`.

   The following :class:`THash` types are supported: :class:`TIntH`, :class:`TIntIntH`, :class:`TIntFltH`, :class:`TIntStrH`, :class:`TIntPrFltH`, :class:`TUInt64H`, :class:`TIntBoolH`, :class:`TIntUInt64H`, :class:`TIntIntVH`, :class:`TIntIntHH`, :class:`TIntFltPrH`, :class:`TIntFltTrH`, :class:`TIntFltVH`, :class:`TIntStrVH`, :class:`TIntIntPrH`, :class:`TIntIntPrVH`, :class:`TUInt64StrVH`, :class:`TIntPrIntH`, :class:`TIntPrIntPrVH`, :class:`TIntTrIntH`, :class:`TIntVIntH`, :class:`TUIntH`, :class:`TIntPrIntVH`, :class:`TIntTrFltH`, :class:`TIntPrStrH`, :class:`TIntPrStrVH`, :class:`TIntStrPrIntH`, :class:`TFltFltH`, :class:`TStrH`, :class:`TStrBoolH`, :class:`TStrIntH`, :class:`TStrIntPrH`, :class:`TStrIntVH`, :class:`TStrUInt64H`, :class:`TStrUInt64VH`, :class:`TStrIntPrVH`, :class:`TStrFltH`, :class:`TStrFltVH`, :class:`TStrStrH`, :class:`TStrStrPrH`, :class:`TStrStrVH`, :class:`TStrStrPrVH`, :class:`TStrStrKdVH`, :class:`TStrIntFltPrH`, :class:`TStrStrIntPrVH`, :class:`TStrStrIntKdVH`, :class:`TStrPrBoolH`, :class:`TStrPrIntH`, :class:`TStrPrFltH`, :class:`TStrPrStrH`, :class:`TStrPrStrVH`, :class:`TStrTrIntH`, :class:`TStrIntPrIntH`, :class:`TStrVH`, :class:`TStrVIntVH`, :class:`TStrVStrH`, and :class:`TStrVStrVH`.


   To illustrate, the following examples show how to create a :class:`THash` with each of the
   constructors::

      >>> snap.TIntH()
      >>> h1 = snap.TIntH(5)
      >>> h1[5] = 5
      >>> h2 = snap.TIntH(h1)
      >>> for key in h2:
      ...     print(key, h2[key])
      ...
      5 5

   :class:`THash` offers iterators of type :class:`THashKeyDatI` for fast access through
   the hash table.

   The following public functions are supported by the :class:`THash` class:

     .. describe:: H[Key]

        Returns the item of *H* with key *Key*.

     .. describe:: H[Key] = Value

        Set ``H[Key]`` to *Value*.

     .. describe:: del H[Key]

        Removes ``H[Key]`` from *H*.

     .. describe:: Key in H

        Returns ``True`` if *Key* is a key in hash table *H*, else ``False``.

     .. describe:: Key not in H

        Equivalent to ``not Key in H``.

     .. iter(H)

        Returns an iterator over all the keys in the hash table.

     .. describe:: Load(SIn)

        Loads the hash table from a binary stream *SIn*. 

     .. describe:: Save(SOut)

        Saves the hash table to a binary stream *SOut*. 

     .. describe:: GetMemUsed()

        Returns the size of the hash table in bytes.

     .. describe:: BegI()

        Returns an iterator to the beginning of the hash table.

     .. describe:: EndI()

        Returns an iterator to the past-the-end element of the hash table.

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

        Returns whether it is auto-size, meaning the hash table can be resized.

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

        Adds a key-value mapping to the hash table, using *Key* as the key and the default value for the datatype as the value (i.e. for :class:`TInt` values, the default value would be 0) if *Key* was not already in the hash table. If *Key* was already in the hash table, the value remains unchanged. The value is then returned.

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

        Get the index of a random key. If the hash table has many deleted keys, this may take a long time. 

     .. describe:: GetRndKeyId (Rnd, EmptyFrac)

        Get the index of a random key. If the hash table has many deleted keys, defrag the hash table first. 

     .. describe:: IsKey(Key)

        Returns a bool indicating whether *Key* is a key in the hash table.

     .. describe:: IsKeyId(KeyId)

        Returns a bool indicating whether there is a key in the hash table with id *KeyId*.

     .. describe:: GetDat(Key)

        Returns the value in the hash table that *Key* maps to.

     .. describe:: FFirstKeyId()

        Returns 1 less than the smallest key id.

     .. describe:: GetKeyV(KeyV)

        Adds all the keys in the hash table to the vector *KeyV*.

     .. describe:: GetDatV(DatV)

        Adds all the values/data in the hash table to the vector *DatV*.

     .. describe:: GetKeyDatPrV(KeyDatPrV)

        Adds all the key-value pairs (as :class:`TPair` objects) to the vector *KeyDatPrV*.

     .. describe:: GetDatKeyPrV(DatKeyPrV)

        Adds all the value-key pairs (as :class:`TPair` objects) to the vector *DatKeyPrV*.

     .. describe:: GetKeyDatKdV(KeyDatKdV)

        Adds all the key-value pairs (as :class:`TKeyDat` objects) to the vector *KeyDatKdV*.

     .. describe:: GetDatKeyKdV(DatKeyKdV)

        Adds all the value-key pairs (as :class:`TKeyDat` objects) to the vector *DatKeyKdV*.

     .. describe:: Swap(Hash)

        Swaps the contents of this hash table with those of *Hash*.

     .. describe:: Defrag()

        Defrags the hash table.

     .. describe:: Pack()

        Reduces the capacity of the memory used to hold the hash table to match its size.

     .. describe:: Sort(CmpKey, Asc)

        Sorts the hash table. If *CmpKey* is True, it sorts based on keys rather than values.

     .. describe:: SortByKey(Asc)

        Sorts the hash table based on keys.

     .. describe:: SortByDat(Asc)

        Sorts the hash table based on the values.

   Below is some code demonstrating the use of the :class:`THash` type:

      >>> h1 = snap.TIntH()
      >>> for i in range(10):
      ...     h1[i] = i + 1
      ...
      >>> h2 = snap.TIntH(h1)
      >>> del h2[0]
      >>> h1.Swap(h2)
      >>> h1.IsKey(0)
      False

TKeyDat
=======

Object used to represent the key-value pairs in a :class:`THash` object.

.. class:: TKeyDat()
           TKeyDat (KeyDat)
           TKeyDat (Key)
           TKeyDat(Key, Dat)
           TKeyDat(SIn)


   Creates a :class:`TKeyDat` object. If *KeyDat* is provided, which is of type :class:`TKeyDat`, its contents will be copied into the newly created object. If *Key* and/or *Dat* are provided, the key for :class:`TKeyDat` will be set to *Key* and the value will be set to *Dat*. If *SIn* is provided, the contents of the :class:`TKeyDat` will be read from the stream.


   The :class:`TKeyDat` constructor cannot be directly called. To create a :class:`TKeyDat` object, the correct
   constructor must be chosen, which indicates the types of the key and value in the :class:`TKeyDat`. Key-value pair types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name><value_type_name>`, followed by `Kd`. For example, a hash table 
   with integer key and string values is named :class:`TIntStrKd`. If `<key_type_name>` 
   and `<value_type_name>` have the same type, only one type name might be used, such 
   as :class:`TIntKd`.

   The following :class:`TKeyDat` types are supported: :class:`TIntKd`, :class:`TIntUInt64Kd`, :class:`TIntPrFltKdKd`, :class:`TIntFltPrKd`, :class:`TIntSFltKd`, :class:`TIntStrKd`, :class:`TUIntIntKd`, :class:`TUIntKd`, :class:`TUInt64IntKd`, :class:`TUInt64FltKd`, :class:`TUInt64StrKd`, :class:`TFltBoolKd`, :class:`TFltIntKd`, :class:`TFltUInt64Kd`, :class:`TFltIntPrKd`, :class:`TFltUIntKd`, :class:`TFltKd`, :class:`TFltStrKd`, :class:`TFltBoolKd`, :class:`TFloatIntBoolPrKd`, :class:`TAscFltIntKd`, :class:`TStrBoolKd`, :class:`TStrIntKd`, :class:`TStrFltKd`, :class:`TStrAscFltKd`, :class:`TStrKd`, and :class:`TIntFltKd`.

   The following public functions are supported by the :class:`TKeyDat` class:

     .. describe:: Save(SOut)

        Saves the contents to the binary stream *SOut*

     .. describe:: GetPrimHashCd()

        Returns the primary hash code.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code.

   The following public attributes are available:

     .. describe:: Key

        The key in the key-value pair. Currently does not support assignment.

     .. describe:: Dat

        The value in the key-value pair. Currently does not support assignment.



THashKeyDatI
============

An iterator over the values in a :class:`THash` object. Normally, these objects are not created directly, but via a call to the hash table class :class:`THash` method, such as :func:`BegI`.

.. class:: THashKeyDatI()
           THashKeyDatI(HashKeyDatI)

   Creates a :class:`THashKeyDatI` iterator object. The contents of *HashKeyDatI*, if provided,
   will be copied into the iterator.

   The :class:`THashKeyDatI` constructor cannot be directly called. To create a :class:`THashKeyDatI` object,
   the correct constructor must be chosen, which indicates the types of the key and value. Hash table
   iterator types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name><value_type_name>`, followed by `HI`. For example, a hash table iterator
   with integer key and string values is named :class:`TIntStrHI`. If `<key_type_name>` 
   and `<value_type_name>` have the same type, only one type name might be used, such 
   as :class:`TIntHI`.

   The following iterator types are currently supported: :class:`TIntHI`, :class:`TIntIntHI`, :class:`TIntFltHI`, :class:`TIntStrHI`, :class:`TIntPrFltHI`, :class:`TUInt64HI`, :class:`TIntBoolHI`, :class:`TIntUint64HI`, :class:`TIntIntVHI`, :class:`TIntIntHHI`, :class:`TIntFltPrHI`, :class:`TIntFltTrHI`, :class:`TIntFltVHI`, :class:`TIntStrVHI`, :class:`TIntIntPrHI`, :class:`TIntIntPrVHI`, :class:`TUInt64StrVHI`, :class:`TIntPrIntPrVHI`, :class:`TIntTrIntHI`, :class:`TIntVIntHI`, :class:`TUIntHI`, :class:`TIntPrIntHI`, :class:`TIntPrIntVHI`, :class:`TIntTrFltHI`, :class:`TIntPrStrHI`, :class:`TIntPrStrVHI`, :class:`TIntStrPrIntHI`, :class:`TFltFltHI`, :class:`TStrHI`, :class:`TStrBoolHI`, :class:`TStrIntHI`, :class:`TStrIntPrHI`, :class:`TStrIntVHI`, :class:`TStrUInt64HI`, :class:`TStrUInt64VHI`, :class:`TStrIntPrVHI`, :class:`TStrFltHI`, :class:`TStrFltVHI`, :class:`TStrStrHI`, :class:`TStrStrPrHI`, :class:`TStrStrVHI`, :class:`TStrStrPrVHI`, :class:`TStrStrKdVHI`, :class:`TStrIntFltPrHI`, :class:`TStrStrIntPrVHI`, :class:`TStrStrIntKdVHI`, :class:`TStrPrBoolHI`, :class:`TStrPrIntHI`, :class:`TStrPrFltHI`, :class:`TStrPrStrHI`, :class:`TStrPrStrVHI`, :class:`TStrTrIntHI`, :class:`TStrIntPrIntHI`, :class:`TStrVHI`, :class:`TStrVStrHI`, and :class:`TStrVStrVHI`.

   The following public functions are supported by the :class:`THashKeyDatI` class:

     .. describe:: Next()

        Updates the iterator to point to the next key-value pair in the :class:`THash`.

     .. describe:: IsEmpty()

        Returns a bool indicating whether the iterator is empty.

     .. describe:: IsEnd()

        Returns a bool indicating whether the end of the iterator has been reached.

     .. describe:: GetKey()

        Get the key for the key-value pair at the current position in the iterator.

     .. describe:: GetDat()

        Get the value for the key-value pair at the current position in the iterator.

   Below is some code demonstrating the use of the :class:`THashKeyDatI` type:

      >>> h1 = snap.TIntH()
      >>> for i in range(5):
      ...     h1[i] = i + 1
      ...
      >>> it = h1.BegI()
      >>> while not it.IsEnd():
      >>>     print(it.GetKey(), it.GetDat())
      >>>     it.Next()
      0 1
      1 2
      2 3
      3 4
      4 5

THashSet
========

Hash sets contain keys are of the same type. Specific keys can be accessed through their key ids. New values can be added to the hash set only if they are unique. All objects classified as :class:`THashSet` objects have access to the following methods.

.. class:: THashSet()
           THashSet(ExpectVals, AutoSizeP=False)
           THashSet(KeyV)
           THashSet(SIn)

   
   Creates a :class:`THashSet` object with a capacity of *ExpectVals*, if specified.  If *KeyV* is provided, which should hold the same type of object the hash set holds, a hash set with the unique values in the vector is created. If *SIn* is provided, the contents of the hash set are loaded from the binary stream *SIn*.

   The :class:`THashSet` constructor cannot be directly called. To create a :class:`THashSet` object, the correct constructor must be chosen, which indicates the type of the key in the hash set. Hash set types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name>`, followed by `Set`. For example, a hash set 
   with integer key is named :class:`TIntSet`.

   The only :class:`THashSet` currently supported is :class:`TIntSet`.


   To illustrate, the following examples show how to create a :class:`THashSet` with each of the
   constructors::

      >>> snap.TIntSet()
      >>> snap.TIntSet(5)
      >>> v = snap.TIntV()
      >>> for i in range(5):
      ...     v.Add(i)
      ...     v.Add(i)
      ...
      >>> hs = snap.TIntSet(v)
      >>> for key in hs:
      ...     print(key)
      ...
      0
      1
      2
      3
      4

   For fast access through the hashset, iterators of type :class:`THashSetKeyI` are provided.

   The following public functions are supported by the :class:`THashSet` class:

     .. describe:: Key in HS

        Returns ``True`` if *Key* is a key in hash set *HS*, else ``False``.

     .. describe:: Key not in HS

        Equivalent to ``not Key in HS``.

     .. iter(H)

        Returns an iterator over all the keys in the hash set.

     .. describe:: GetSet(Key1)
                   GetSet(Key1, Key2)
                   GetSet(Key1, Key2, Key3)
                   GetSet(Key1, Key2, Key3, Key4)
                   GetSet(Key1, Key2, Key3, Key4, Key5)
                   GetSet(Key1, Key2, Key3, Key4, Key5, Key6)
                   GetSet(Key1, Key2, Key3, Key4, Key5, Key6, Key7)
                   GetSet(Key1, Key2, Key3, Key4, Key5, Key6, Key7, Key8)
                   GetSet(Key1, Key2, Key3, Key4, Key5, Key6, Key7, Key8, Key9)

        Returns a hash set with the given keys.

     .. describe:: Load(SIn)

        Loads the hash set from a binary stream *SIn*. 

     .. describe:: Save(SOut)

        Saves the hash set to a binary stream *SOut*. 

     .. describe:: GetMemUsed()

        Returns the size of the hash set in bytes.

     .. describe:: BegI()

        Returns an iterator pointing to the first element in the hash set. 

     .. describe:: EndI()

        Returns an iterator referring to the past-the-end element in the hash set. 

     .. describe:: Gen(ExpVals)

        Clears the hash set and resizes it with a capacity of at least *ExpVals*.

     .. describe:: Clr()

        Clears the contents of the hash set.

     .. describe:: Empty()

        Returns a bool indicating whether the hash set is empty.

     .. describe:: Len()

        Returns the number of keys in the hash set.

     .. describe:: GetPorts()

        Returns the number of ports.

     .. describe:: IsAutoSize()

        Returns a bool indicating whether it is auto-size, meaning the hash set can be resized.

     .. describe:: GetMxKeyIds()

        Returns the first key id that is larger than all those currently stored in the 
        hash set.

     .. describe:: GetReservedKeyIds()

        Returns the size of the allocated storage capacity for the hash set.

     .. describe:: IsKeyIdEqKeyN()

        Returns a boolean whether there have been any gaps in the key ids, which can occur if a key is deleted and the hash set has not been defraged.

     .. describe:: AddKey(Key)

        Adds key *Key* to the hash set, if it not already in the hash set, and returns the key id.

     .. describe:: AddKeyV(KeyV)

        Adds each key in *KeyV* not already in the hash set to the hash set.

     .. describe:: DelKey(Key)

        Removes *Key* from the hash set. Raises an exception if *Key* is not a key in the hash set.

     .. describe:: DelIfKey(Key)

        Removes *Key* from the hash set. Returns a boolean indicating whether *Key* was a key in the hash set.

     .. describe:: DelKeyId(KeyId)

        Removes the key with id *KeyId* from the hash set. Raises an exception if *KeyId* is not a valid id for a key in the hash set.

     .. describe:: DelKeyIdV(KeyIdV)

        Removes all the keys with an id in *KeyIdV* from the hash set. Raises an exception if one of the key ids in *KeyIdV* is not a valid id for a key in the hash set.

     .. describe:: GetKey(KeyId)

        Returns the key with id *KeyId*.

     .. describe:: GetKeyId(Key)

        Returns the key id for key *Key*.

     .. describe:: GetRndKeyId(Rnd)

        Get an index of a random key. If the hash set has many deleted keys, this may take a long time. 

     .. describe:: IsKey(Key)

        Returns a bool indicating whether *Key* is a key in the hash set.

     .. describe:: IsKeyId(KeyId)

        Returns a bool indicating whether there is a key in the hash table with id *KeyId*.

     .. describe:: GetDat(Key)

        Returns the value in the hash table that *Key* maps to.

     .. describe:: FFirstKeyId()

        Returns 1 less than the smallest key id.

     .. describe:: GetKeyV(KeyV)

        Adds all the keys in the hash table to the vector *KeyV*.

     .. describe:: Swap(Set)

        Swaps the contents of this hash set with those of *Set*.

     .. describe:: Defrag()

        Defrags the hash set.

     .. describe:: Pack()

        Reduces the capacity of the memory used to hold the hash set to match its size.


   Below is some code demonstrating the use of the :class:`THashSet` type:

      >>> hs = snap.TIntSet()
      >>> for i in range(30):
      ...     hs.AddKey(i)
      ...
      >>> hs.IsKey(0)
      True
      >>> v = snap.TIntV()
      >>> hs.GetKeyV(v)


THashSetKeyI
============

An iterator over the values in a :class:`THashSet` object. Normally, these objects are not created directly, but via a call to the hash table class :class:`THashSet` method, such as :func:`BegI`.

.. class:: THashSetKeyI()
           THashSetKeyI(SetKeyI)

   Creates a :class:`THashSetKeyI` iterator object. The contents of *SetKeyI*, if provided,
   will be copied into the iterator.

   The :class:`THashSetKeyI` constructor cannot be directly called. To create a :class:`THashSetKeyI` object,
   the correct constructor must be chosen, which indicates the type of the key in the hash set iterator. Hash set iterator types in Snap.py and SNAP use a naming convention of being named
   as `<key_type_name>`, followed by `HSI`. For example, a hash set iterator
   with integer key is named :class:`TIntHSI`.

   The following iterator types are currently supported: :class:`TIntHSI`.

   The following public functions are supported by the :class:`THashSetKeyI` class:

     .. describe:: Next()

        Updates the iterator to point to the next key-value pair in the :class:`THashSet`.

     .. describe:: IsEmpty()

        Returns ``True``, if the iterator is empty, else ``False``.

     .. describe:: IsEnd()

        Returns ``True``, if the end of the iterator has been reached, else ``False``.
        
     .. describe:: GetKey()

        Returns the key at the current position in the iterator.

   Below is some code demonstrating the use of the :class:`THashSetKeyI` type:

      >>> hs1 = snap.TIntSet()
      >>> hs1.AddKey(0)
      >>> it = hs1.BegI()
      >>> print(it.GetKey())
      0



