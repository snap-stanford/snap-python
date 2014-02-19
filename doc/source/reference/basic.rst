Basic Types
````````````

Basic types in SNAP are :class:`TInt`, :class:`TFlt`, and :class:`TStr`.
In Snap.py, these types are converted to Python types
:class:`int`, :class:`float`, and :class:`str`, respectively. In general,
there is no need to explicitly work with SNAP types in Snap.py, since
Snap.py automatically converts these basic types to Python types.

.. note::
 
   Do not use an empty string literal “” in Python, if a Snap.py
   function parameter is of type TStr. SNAP handling of TStr(“”)
   is not compatible with Python, so an empty string literal will cause
   an error.

Below is some code demonstrating the use of the basic types:

  >>> i = snap.TInt(10)
  >>> print i.Val
  10
