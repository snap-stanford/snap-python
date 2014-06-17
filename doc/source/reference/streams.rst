File Streams
````````````

The file streams offered by SNAP.py are :class:`TFOut`, which is used for file writing, and :class:`TFIn`, which is used for file reading.

TFOut
=====

.. class:: TFOut(FNm)

   Creates a :class:`TFOut` object that can be used to write the contents of the file specified by the path *FNm*. If a file with name *FNm* does not already exist, it creates a new file. If a file with name *FNm* exists, its contents will be overwritten.

   Below is a list of functions supported by the :class:`TFOut` class:

     .. describe:: PutCh(Ch)

        Writes the character *Ch* to the curret file stream position.

     .. describe:: Flush()

        Flushes the write buffer for the stream.

     .. describe:: New(FNm)

        Returns a new :class:`TFOut` object for the file with name *FNm*.

   Below is some code demonstrating the use of the :class:`TFOut` type, which creates a file with name 'test.graph' in the working directory:

      >>> Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
      >>> FOut = snap.TFOut("test.graph")
      >>> Graph.Save(FOut)
      >>> FOut.Flush()

TFIn
====

.. class:: TFIn(FNm)

   Creates a :class:`TFIn` object that can be used to read the contents of the file specified by the path *FNm*. Raises the exception :class:`RuntimeError` if a file with name *FNm* cannot be found.

   Below is a list of functions supported by the :class:`TFIn` class:

     .. describe:: Eof()

        Returns a boolean indicating whether the end of the file has been reached.

     .. describe:: Len()

        Returns the length of the remainder of the file starting at the current file stream position.

     .. describe:: GetCh()

        Returns the next character in the file and updates the file stream position to the next character in the file.

     .. describe:: PeekCh()

        Returns the next character in the file without updating the file stream position.

     .. describe:: Reset()

        Resets the file stream to the beginning of the file.

     .. describe:: New(FNm)

        Returns a new :class:`TFIn` object for the file with name *FNm*.

   Below is some code demonstrating the use of the :class:`TFIn` type, which assumes a file with name 'test.graph' exists in the working directory:

      >>> FIn = snap.TFIn("test.graph")
      >>> Graph = snap.TNGraph.Load(FIn)
      >>> FIn.Len()
      11445