Basic Types
```````````

Basic types in SNAP are :class:`TInt`, :class:`TFlt`, and :class:`TStr`, which
in Snap.py are automatically converted to Python types
:class:`int`, :class:`float`, and :class:`str`, respectively. In general,
there is no need to explicitly work with SNAP types in Snap.py because
of the automatic conversion.


TInt
====

.. class:: TInt()
           TInt(val)

   Returns a new TInt initialized with the value specified by optional parameter
   val. If no value is given, the TInt object is initialized with the default value 0.
   In Snap.py, TInt is automatically converted to Python type :class:`int`.

   Below is a list of public functions supported by the TInt class:

     .. describe:: GetMemUsed()

        Returns the size of the TInt object in bytes.

     .. describe:: GetPrimHashCd()

        Returns the value stored in the TInt.

     .. describe:: GetSecHashCd()

        Returns the value stored in the TInt divided by 0x10.


   Below is a list of static functions supported by the TInt class:

     .. describe::  Abs(val)

        A static method that returns the absolute value of val, an int.

     .. describe:: GetHexStr(val)

        A static method that returns a string with the hexidecimal representation of int val.

     .. describe:: GetInRng(val, min, max)

        A static method that returns int val if it is between min and max. If val is smaller
        than min, it returns min. If val is larger than max, it returns max.

     .. describe:: GetKiloStr(val)

        A static method that returns the int val as a kilo-formatted string. If val is less 
        than 1000, it returns val as a string. If val is greater than or equal to 1000, it
        returns a string in form of 'x.yK', where x is some digit from 1-9 and y from 0-9.

     .. describe:: GetMegaStr(val)

        A static method that returns the int val as a mega-formatted string. If val is less
        than 1000000, it returns the equivalent of GetKiloStr(val). If val is greater than
        or equal to 1000000, it returns a string in the form of 'x.yM', where x is some
        digit from 1-9 and y from 0-9.

     .. describe:: GetMn(val1, val2)
                   GetMn(val1, val2, val3)
                   GetMn(val1, val2, val3)

        A static method that returns the minimum of the ints passed in as parameters.

     .. describe:: GetMx(val1, val2)
                   GetMx(val1, val2, val3)
                   GetMx(val1, val2, val3)

        A static method that returns the maximum of the ints passed in as parameters.

     .. describe:: GetRnd(range=0)

        A static method that returns a random int between 0 and range-1, inclusive. If a range 
        value of 0 is specified, it returns a random int between 0 and INT_MAX. The default
        value of range is 0.

     .. describe:: IsEven(val)

        A static method that returns a bool indicating whether val is even.

     .. describe:: IsOdd(val)

        A static method that returns a bool indicating whether val is odd.

     .. describe:: Sign(val)

        A static method that returns 1 if val > 0, -1 if val < 0, and 0 if val == 0.


   A single public attribute is offered by the TInt class:

     .. describe:: Val

        A member of the TInt object of type int that gives the value the TInt holds. Supports 
        =, +=, -=, *=, and /= operators.


   A few static public attributes are offered by the TInt class:

     .. data:: Mn

        The minimum value of an signed int, equivalent to INT_MIN in C++.

     .. data:: Mx

        The maximum value of an signed int, equivalent to INT_MAX in C++.

     .. data:: Kilo

        Equal to 1024.

     .. data:: Mega

        Equal to 1024*1024.

     .. data:: Giga

        Equal to 1024*1024*1024.

     .. data:: Rnd

        The TRnd object used in methods such as GetRnd.



   Below is some code demonstrating the use of the TInt type:

      >>> i = snap.TInt(10)
      >>> print i.Val
      10
      >>> i.Val = 21
      >>> snap.TInt.IsEven(5)
      False
      >>> snap.TInt.GetMegaStr(1234567)
      '1.2M'

TFlt
====

.. class:: TFlt()
           TFlt(val)

   Returns a new TFlt initialized with the value specified by optional parameter
   val. If no value is given, the TFlt object is initialized with the default value 0.
   In Snap.py, TFlt is automatically converted to Python type :class:`float`.

   Below is a list of public functions supported by the TFlt class:

     .. describe:: GetMemUsed()

        Returns the size of the TFlt object in bytes.

     .. describe:: GetPrimHashCd()

        Returns the primary hash code for the TFlt object.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code for the TFlt object.

     .. describe:: IsNan()

        Returns a bool indicating whether the value stored in the TFlt is NaN - not a number.

     .. describe:: IsNum()

        Returns a bool indicating whether the value stored in the TFlt is a valid number.


   Below is a list of static functions supported by the TFlt class:

     .. describe::  Abs(val)

        A static method that returns the absolute value of val, a float.

     .. describe:: GetInRng(val, min, max)

        A static method that returns float val if it is between min and max. If val is smaller
        than min, it returns min. If val is larger than max, it returns max.

     .. describe:: GetKiloStr(val)

        A static method that returns the float val as a kilo-formatted string. If val is less 
        than 1000, it rounds val to the nearest int, and returns it as a string. If val is 
        greater than or equal to 1000, it returns a string in form of 'x.yK', where x is some 
        digit from 1-9 and y from 0-9.

     .. describe:: GetMegaStr(val)

        A static method that returns the float val as a mega-formatted string. If val is less
        than 1000000, it returns the equivalent of GetKiloStr(val). If val is greater than
        or equal to 1000000, it returns a string in the form of 'x.yM', where x is some
        digit from 1-9 and y from 0-9.

     .. describe:: GetGigaStr(val)

        A static method that returns the float val as a giga-formatted string. If val is less
        than 1000000000, it returns the equivalent of GetMegaStr(val). If val is greater than
        or equal to 1000000000, it returns a string in the form of 'x.yG', where x is some
        digit from 1-9 and y from 0-9.

     .. describe:: GetMn(val1, val2)
                   GetMn(val1, val2, val3)
                   GetMn(val1, val2, val3)

        A static method that returns the minimum of the floats passed in as parameters.

     .. describe:: GetMx(val1, val2)
                   GetMx(val1, val2, val3)
                   GetMx(val1, val2, val3)

        A static method that returns the maximum of the floats passed in as parameters.

     .. describe:: GetRnd()

        A static method that returns a random int between 0 and 1.

     .. describe:: IsNum(val)

        A static method that returns a bool indicating whether val is a valid numner.

     .. describe:: IsNaN(val)

        A static method that returns a bool indicating whether val is NaN, not a number.

     .. describe:: Sign(val)

        A static method that returns 1 if val > 0, -1 if val < 0, and 0 if val == 0.

     .. describe:: Round(val)

        A static method that returns val rounded to the nearest int.

     .. describe:: Eq6(val1, val2)

        A static method that returns whether val1 and val2 are equal to 6 decimal places.


   A single public attribute is offered by the TFlt class:

     .. describe:: Val

        A member of the TFlt object of type int that gives the value the TFlt holds. Supports 
        =, +=, -=, *=, and /= operators.


   A few static public attributes are offered by the TInt class:

     .. data:: Mn

        The minimum value of a TFlt, equivalent to -DBL_MAX in C++.

     .. data:: Mx

        The maximum value of a TFlt, equivalent to DBL_MAX in C++.

     .. data:: NInf

        The value used to represent negative infinity, which is equivalent to Mn.

     .. data:: PInf

        The value used to represent positive infinity, which is equivalent to Mx.

     .. data:: Eps

        The epsilon value for the TFlt, equal to 1e-16.

     .. data:: EpsHalf

        Equal to 1e-7.

     .. data:: Rnd

        The TRnd object used in methods such as GetRnd.


   Below is some code demonstrating the use of the TFlt type:

      >>> f = snap.TInt(9.874)
      >>> print f.Val
      9.874
      >>> f.Val = 2.1
      >>> f.IsNum()
      True
      >>> snap.TFlt.Round(1.234567)
      1

TStr
====

.. class:: TStr()
           TStr(str)

   Returns a new TStr initialized with the value specified by optional parameter
   str. If no value is given, the TStr object is initialized with the empty string.
   In Snap.py, TStr is automatically converted to Python type :class:`str`.

   Below is a list of functions supported by the TStr class:

     .. describe:: GetMemUsed()

        Returns the size of the TStr object in bytes.

     .. describe:: CStr()

        Returns the TStr as a c-string, which is converted to a python str.

     .. describe:: PutCh(ChN, Ch)

        Replaces the character at position ChN with character Ch.

     .. describe:: GetCh(ChN)

        Returns the character at position ChN.

     .. describe:: LastCh()

        Returns the last character in the string.

     .. describe:: Clr()

        Sets the TStr to the empty string.

     .. describe:: Len()

        Returns the length of the string.

     .. describe:: Empty()

        Returns a bool indicating whether the string is empty.

     .. describe:: IsUc()

        Returns a bool indicating whether the string is uppercase.

     .. describe:: ToUc()

        Coverts the contents of the TStr to uppercase and returns the str.

     .. describe:: GetUc()

        Returns a Python str with the contents of the TStr converted to uppercase. The contents
        of the original TStr are left unchanged.

     .. describe:: CmpI(str)

        Compares the TStr to the parameter str, of type TStr, character by character. Returns a 
        positive number if the TStr is greater than str and vice versa.

     .. describe:: Eql(str)

        Returns a bool indicating whether the TStr is equal to the TStr str.

     .. describe:: IsLc()

        Returns a bool indicating whether the string is lowercase.

     .. describe:: ToLc()

        Coverts the contents of the TStr to lowercase and returns the str.

     .. describe:: GetLc()

        Returns a Python str with the contents of the TStr converted to lowercase. The contents
        of the original TStr are left unchanged.

     .. describe:: ToCap()

        Returns a Python str with the first letter of the contents of the TStr capitalized.

     .. describe:: GetCap()

        Capitalizes the first letter of the contents of the TStr and returns the resulting
        Python str.

     .. describe:: ToTrunc()

        Removes the trailing whitespace from the contents of the TStr and returns the resulting
        Python str.

     .. describe:: GetTrunc()

        Returns a Python str with all the whitespace removed from the end of the contents of the
        TStr.

     .. describe:: ToHex()

        Converts the contents of the TStr to hex and returns the resulting value.

     .. describe:: GetHex()

        Returns the contents of the TStr converted to hex as a Python str. The contents of the
        original TStr are left unchanged.

     .. describe:: FromHex()

        Converts the contents of the TStr from hex to the original string and returns the
        resulting value.

     .. describe:: GetFromHex()

        Returns the contents of the TStr converted from hex as a Python str. The contents of the
        original TStr are left unchanged.

     .. describe:: GetSubStr(start)
                   GetSubStr(start, end)

        Returns a substring starting at position start and ending at position end. The substring
        includes the character at position end. If end is not specified, the end position is 
        assumed to be the last character in the string.

     .. describe:: InsStr(pos, str)

        Inserts the contents of the string str (either a Python str or a TStr) into the TStr
        at position pos.

     .. describe:: DelChAll(ch)

        Deletes all instances of the char ch from the TStr.

     .. describe:: DelSubStr(start, end)

        Deletes the substring starting at position start and ending at position end from the TStr.

     .. describe:: DelStr(str)

        Deletes the first instance of str found in the TStr. Returns a bool indicating whether
        anything was deleted.

     .. describe:: LeftOf(ch)

        Returns the substring left of the first instance of char ch in the TStr.

     .. describe:: LeftOfLast(ch)

        Returns the substring left of the last instance of char ch in the TStr.

     .. describe:: RightOf(ch)

        Returns the substring right of the first instance of char ch in the TStr.

     .. describe:: RightOfLast(ch)

        Returns the substring right of the last instance of char ch in the TStr.

     .. describe:: Mid(start)
                   Mid(start, numChars)

        Returns the Python str starting at position start containing at most numChars characters.
        If numChars is not specified, it returns the substring starting at position start to the
        end of the string.

     .. describe:: Left(start)

        Returns the substring starting at position 0 to start-1.

     .. describe:: Right(start)

        Returns the substring starting at position start to the end of the string.

     .. describe:: Slice(start, numChars)

        Returns a substring of the string starting at position start containing numChars 
        characters.

     .. describe:: CountCh(ch, start=0)

        Returns the number of times ch appears in the string, starting at position start.

     .. describe:: SearchCh(ch, start=0)

        Searches the string for the character ch starting at position 0 and returns the index at 
        which ch was found or -1 if it was not found.

     .. describe:: SearchChBack(ch, start=-1)

        Searches the string for the character ch starting at position start and going backward. 
        Returns the index at which the character was found or -1. A start value of -1 indicates 
        that the method should start searching at the end of the string.

     .. describe:: SearchStr(str, start=0)

        Searches the string for the substring str starting at position 0 and returns the index at 
        which str was found or -1 if it was not found.

     .. describe:: IsChIn(ch)

        Returns a bool indicating whether the character ch is in the string.

     .. describe:: IsPrefix(prefix)

        Returns a bool indicating whether prefix is a prefix of the string.

     .. describe:: IsSuffix(suffix)

        Returns a bool indicating whether suffix is a suffix of the string.

     .. describe:: ChangeCh(orig, repl, start)

        Looks for the first instance of the character orig starting at index start and replaces 
        it with the character repl. Returns the index of the character replaced.

     .. describe:: ChangeChAll(orig, repl, start)

        Looks for the all instances of the character orig starting at index start and replaces 
        them with the character repl. Returns the number of character replaced.

     .. describe:: ChangeStr(orig, repl, start)

        Looks for the first instance of the string orig starting at index start and replaces 
        it with the string repl. Returns the starting index of the string replaced.

     .. describe:: ChangeStrAll(orig, repl, start)

        Looks for the all instances of the string orig starting at index start and replaces 
        them with the string repl. Returns the number of replacements done.

     .. describe:: Reverse()

        Returns a Python string with the contents of the TStr reveresed.

     .. describe:: GetPrimHashCd()

        Returns the primary hash code for the TStr.

     .. describe:: GetSecHashCd()

        Returns the secondary hash code for the TStr.

     .. describe:: IsInt()

        Returns a bool indicating whether the string is an int.

     .. describe:: GetInt()

        Returns the contents of the string converted to an int.

     .. describe:: IsUInt()

        Returns a bool indicating whether the string is an unsigned int.

     .. describe:: GetUInt()

        Returns the contents of the string converted to an unsigned int.

     .. describe:: IsInt64()

        Returns a bool indicating whether teh string is a 64-bit int.

     .. describe:: GetInt64()

        Returns the contents of the string converted to a 64-bit int.

     .. describe:: IsUInt64()

        Returns a bool indicating whether the string is an unsigned 64-bit int.

     .. describe:: GetUInt64()

        Returns the contents of the string converted to an unsigned 64-bit int.

     .. describe:: IsHexInt()

        Returns a bool indicating whether the string is a valid hexadecimal int.

     .. describe:: GetHexInt()

        Returns the contents of the string converted to an int, which is in decimal, not 
        hexadecimal format.

     .. describe:: IsHexInt64()

        Returns a bool indicating whether the string is a valid 64-bit hexadecimal int.

     .. describe:: GetHexInt64()

        Returns the contents of the string converted to a 64-bit int, which is in decimal, not 
        hexadecimal format.

     .. describe:: IsFlt()

        Returns a bool indicating whether the contents of string is a valid float.

     .. describe:: GetFlt()

        Returns the contents of the string converted to a float.

     .. describe:: IsWord()

        Returns a bool indicating whether the contents of the string is a single word, which
        is defined as a collection of letters and digits, starting with a letter.

     .. describe:: IsWs()

        Returns a bool indicating whether the content of the string is just whitespace.


   Below is some code demonstrating the use of the TStr type:

      >>> s = snap.TStr('Welcome to Snap.py!')
      >>> print s.CStr()
      'Welcome to Snap.py!'
      >>> s.GetSubStr(0,6)
      'Welcome'

.. note::
 
   Do not use an empty string literal “” in Python, if a Snap.py
   function parameter is of type TStr. SNAP handling of TStr(“”)
   is not compatible with Python, so an empty string literal will cause
   an error.
