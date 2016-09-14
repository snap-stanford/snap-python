Sparse Attributes
``````````````````

SNAP offers the following classes for handling sparse attributes: :class:`TAttr` for
when keys are integers and :class:`TAttrPair` for when keys are a pair of integers.
These classes use hash tables to organize and store integer, float, and string
attributes.

**NOTE:** Sparse attributes are still under development in python. 


TAttr
=========

.. class:: TAttr()
           TAttr(SIn)
           TAttr(Attrs)

   Returns a data structure for tracking sparse attributes, where the keys are integers.
   If *SIn* is specified, the data structure is loaded from the binary stream. If *Attrs*
   is specified, the contents of *Attrs* are copied into the new sparse attribute data
   structure.

   All the attribute related functions return an integer indicating whether there were 
   any errors during execution. Below is a list of functions supported by the 
   :class:`TAttr` class:

     .. describe:: Save()

        Saves the attributes to a (binary) stream SOut.

     .. describe:: Clr()

        Clears the contents of the attribute map. 

     .. describe:: AddSAttrDat(Id, AttrName, Val)
                   AddSAttrDat(Id, AttrId, Val)

        Adds attribute with name *AttrName* or attribtue id *AttrId* for the given 
        integer id *Id*. *Val* can be an int, float, or string.

     .. describe:: GetSAttrDat(Id, AttrName, Val)
                   GetSAttrDat(Id, AttrId, Val)

        Gets attribute with name *AttrName* or attribute id *AttrId* for the given 
        integer id *Id*. Resulting value is stored in *Val*.

     .. describe:: DelSAttrDat(Id, AttrId)

        Delete attribute with name *AttrName* or attribute id *AttrId* for the given
        integer id *Id*.

     .. describe:: DelSAttrId(Id)

        Delete all attributes for the given integer id *Id*.

     .. describe:: GetSAttrV(Id, AttrType, AttrV)

        Get a list of all attributes of type *AttrType* for the given integer id *Id*.
        *AttrType* should be one of IntType, FltType, or StrType.

     .. describe:: GetIdVSAttr(AttrName, IdV)
                   GetIdVSAttr(AttrId, IdV)

        Get a list of all ids that have an attribute with name *AttrName* or id 
        *AttrId*.

     .. describe:: AddSAttr(Name, AttrType, AttrId)

        Adds a mapping for an attribute with name *Name* and type *AttrType*. *AttrId*
        is updated with the assigned attribute integer id.

     .. describe:: GetSAttrId(Name, AttrId, AttrType)

        Given the attribute name *Name*, get the attribute id.

     .. describe:: GetSAttrName(AttrId, Name, AttrType)

        Given the attribute id *AttrId*, get the attribute name.


TAttrPair
=========

.. class:: TAttrPair()
           TAttrPair(SIn)
           TAttrPair(Attrs)

   Returns a data structure for tracking sparse attributes, where the keys are integer pairs.
   If *SIn* is specified, the data structure is loaded from the binary stream. If *Attrs*
   is specified, the contents of *Attrs* are copied into the new sparse attribute data
   structure.

   All the attribute related functions return an integer indicating whether there were 
   any errors during execution. Below is a list of functions supported by the 
   :class:`TAttrPair` class:

     .. describe:: Save()

        Saves the attributes to a (binary) stream SOut.

     .. describe:: Clr()

        Clears the contents of the attribute map. 

     .. describe:: AddSAttrDat(Id, AttrName, Val)
                   AddSAttrDat(Id, AttrId, Val)

        Adds attribute with name *AttrName* or attribtue id *AttrId* for the given 
        integer pair id *Id*. *Val* can be an int, float, or string.

     .. describe:: GetSAttrDat(Id, AttrName, Val)
                   GetSAttrDat(Id, AttrId, Val)

        Gets attribute with name *AttrName* or attribute id *AttrId* for the given 
        integer pair id *Id*. Resulting value is stored in *Val*.

     .. describe:: DelSAttrDat(Id, AttrId)

        Delete attribute with name *AttrName* or attribute id *AttrId* for the given
        integer pair id *Id*.

     .. describe:: DelSAttrId(Id)

        Delete all attributes for the given integer pair id *Id*.

     .. describe:: GetSAttrV(Id, AttrType, AttrV)

        Get a list of all attributes of type *AttrType* for the given integer pair 
        id *Id*. *AttrType* should be one of IntType, FltType, or StrType.

     .. describe:: GetIdVSAttr(AttrName, IdV)
                   GetIdVSAttr(AttrId, IdV)

        Get a list of all ids that have an attribute with name *AttrName* or id 
        *AttrId*.

     .. describe:: AddSAttr(Name, AttrType, AttrId)

        Adds a mapping for an attribute with name *Name* and type *AttrType*. *AttrId*
        is updated with the assigned attribute integer id.

     .. describe:: GetSAttrId(Name, AttrId, AttrType)

        Given the attribute name *Name*, get the attribute id.

     .. describe:: GetSAttrName(AttrId, Name, AttrType)

        Given the attribute id *AttrId*, get the attribute name.