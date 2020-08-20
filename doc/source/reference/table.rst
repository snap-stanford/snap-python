TTable
`````````````````````
The :class:`TTable` in SNAP is a table data structure for storing tabular data, which can easily be converted into the SNAP graph. The :class:`TTable` is much more efficient than other tabular data structures and functions seamlessly inside the SNAP universe. The :class:`TTable` can easily store hundreds of millions of rows and perform complex data manipulation operations. 

:class:`TTable` objects can be easily loaded from CSV and TSV files. :class:`TTable` objects can store integers, strings, and floats in its columns. Each column can store exactly one data type, and each column has its own name, a string. 

This tutorial will cover:
- how to create a TTable, 
- how to save and load a TTable, 
- how to perform columnwise operations on TTables, 
- how to perform rowwise operations on TTables, 
- how to join two TTables together, 
- and how to extract information from a TTable.

Creating a :class:`TTable`
==========================

To create a :class:`TTable` object in SNAP, you must first define the: 
- Context: The Context holds information behind-the-scenes about the mappings between integers and strings (which reduces memory usage). You don’t have to do anything with the Context except create it and use it as a parameter when creating your :class:`TTable`. Many :class:`TTable`s can share the same Context. 
- Schema: The Schema defines the column names in the table and their data types, which, unlike in other Python packages, you must specify up-front. Each column can be either an integer column, a float column, or a string column. Each column can hold values of only that data type.

For this tutorial, let’s assume the table below is a tab-separated file with the following columns and values, called ‘student_grades.tsv’:


.. table:: Student Grades
   :widths: 15 10 10 10
========== ========== ========== ==========
StudentID  Midterm1   Midterm2   Final
========== ========== ========== ==========
101        79         86         88
102        84         80         79
103        56         76         80
104        90         92         96
105        92         85         87
106        87         95         92
107        94         90         91
108        76         88         81
========== ========== ========== ==========

To turn this into a SNAP table, we must create a Context and Schema::

   	>>> import snap
   
	>>> context = snap.:class:`TTable`Context()

	>>> schema = snap.Schema()
	>>> schema.Add(snap.TStrTAttrPr("StudentID", snap.atInt))
	>>> schema.Add(snap.TStrTAttrPr("Midterm1", snap.atInt))
	>>> schema.Add(snap.TStrTAttrPr("Midterm2", snap.atInt))
	>>> schema.Add(snap.TStrTAttrPr("Final", snap.atInt))

As you can see, defining the Context simply requires initializing an object of type :class:`TTable`Context. That’s all you have to do for the Context!

For the Schema, you must first initialize an object of the SNAP Schema type, and then use the Add() method to create column types for the :class:`TTable` you want to build.  The Add() method takes one parameter, a SNAP TStrTAttrPr, which is a pair consisting of a string and an attribute. An attribute in SNAP is used to represent different data types using an integer key; you don’t have to worry about this, but just remember that the Schema requires this data type for the columns. There are always 2 components of a TStrTAttrPr: the name of the column, which is a string, and the type of data that the column with that name will hold. The options are atInt (integer attribute), atFlt (float attribute), and atStr (string attribute). Since our columns are type integer, we will use atInt for all of them. 

We now have the building blocks for a :class:`TTable` with four columns and a context! Next, we’ll show how to create a :class:`TTable` from these components, plus a path to a file that we want to make a :class:`TTable` from. :class:`TTable`s can be created from comma-separated files (CSV) and tab-separated files (TSV). Here’s an example::

       >>> filename = "/path/to/student_grades.tsv"
       >>> grade_table = snap.:class:`TTable`.LoadSS(schema, filename, context, "\t", 
       >>> snap.TBool(True))

For the filename, we simply use the path to that file on the local machine. Then, to create a table, we use the function :class:`TTable`.LoadSS(). This function takes in 5 parameters::

- The Schema that we made before, which should correspond to the number and types of columns in the TSV file
- The name of the path to the file, as a string
- The Context created earlier
- The separator used in the file (“\t” for tab separated, “,” for comma separated, etc.)
- A snap.TBool boolean value indicating whether or not the file has a ‘title line,’ that is, a beginning line of column names or other text that is not commented out with a #. Remember that your Schema already has column names, so you don’t want to include them from your CSV or TSV since they’ll throw an error! In our example above, we did have column names in our TSV, so we set this boolean to True. 

Now we’ve successfully created a :class:`TTable` in SNAP! Recall that you can accommodate any table by changing the Schema for the number and type of columns that you need. 

Saving and Loading a :class:`TTable` with Binary Format
=======================================================

Next, we’ll demonstrate how to save a :class:`TTable` and load one from binary. :class:`TTable`s can be saved in binary format because this saves space (in fact, it’s orders of magnitude more efficient than saving it as text). To save a :class:`TTable` to binary format, you use the following: 

      	    >>> outfile = "/path/to/grade_table.bin"
	    >>> FOut = snap.TFOut(outfile)
	    >>> table.Save(FOut)
	    >>> FOut.Flush()

The four steps are: 
- Create a path to the file you want to save your :class:`TTable` to. 
- Create a TFOut object. A SNAP TFout object allows writing the contents of a file to the specified pathname. 
- Save the table to your TFOut object (here, named FOut) using the Save() function. 
- Flush your TFOut object. This flushes the write buffer for the stream, meaning that it has been cleared of the contents of our table and it can be used again for further saving operations. 

Once we’ve saved a :class:`TTable` object to binary format, we can also load :class:`TTable` objects from their binary format as follows: 

     	   >>> context = snap.:class:`TTable`Context()

	   >>> outfile = "/path/to/grade_table.bin"
	   >>> FIn = snap.TFIn(outfile)
	   >>> table = snap.:class:`TTable`.Load(FIn, context)

Again, the four steps of loading a :class:`TTable` from binary format are: 
- Create a Context object for the :class:`TTable`. This is necessary when loading a :class:`TTable` that has been stored in binary format. 
- Provide the pathname where the binary file currently resides. 
- Create an TFIn object with the pathname to the binary file. The SNAP FIn object is used to read the contents of a binary file and parse it back into a more complex data structure. It takes the pathname as a parameter. 
- Finally, create the :class:`TTable` using the :class:`TTable`.Load() method, which takes two parameters: the TFIn object we just made, and the context that was created in Step 1. 

We’ve now covered the basics of how to create, save, and load :class:`TTable`s!

Columnwise :class:`TTable` Operations
=====================================

Now that we know how to create a :class:`TTable`, let’s investigate different column operations that are supported by :class:`TTable`s. These column operations allow us to take two or more columns and create a new column via some operation. These include addition, subtraction, multiplication, division, modulo division, maximum, minimum, and concatenation. They are united by their function names, which are all of the form .ColFunc(), where Func is the operation name. There is also one more advanced function, AggregateCols(), that allows us to do other operations like count, first, last, mean, and median. 

Let’s do an example by taking our table from above and performing some basic operations. Here is the original for reference:


.. table:: Student Grades
   :widths: 15 10 10 10
========== ========== ========== ==========
StudentID  Midterm1   Midterm2   Final
========== ========== ========== ==========
101        79         86         88
102        84         80         79
103        56         76         80
104        90         92         96
105        92         85         87
106        87         95         92
107        94         90         91
108        76         88         81
========== ========== ========== ==========


Let’s say we wanted to know the total number of points that each student earned across the two midterms. To do this, we want to use the ColAdd() function, which looks like this:: 

      	  >>> table.ColAdd(Attr1, Attr2, NewColName)

In the ColAdd() function, we provide three parameters: the first two are the columns we want to add together, using their string names, and the third is the name of the column we want to create that will hold the sums of the first two columns. This is true for all ColFunc() functions. Since we want to get the sum over the midterm scores, we will add together Midterm1 and Midterm2:: 

       >>> grade_table.ColAdd(“Midterm1”, “Midterm2”, “MidScoreSum”)

Which yields: 


.. table:: Student Grades
   :widths: 15 10 10 10 10
========== ========== ========== ========== ==========
StudentID  Midterm1   Midterm2   Final	    MidScoreSum
========== ========== ========== ========== ==========
101        79         86         88	    165
102        84         80         79	    164
103        56         76         80	    132
104        90         92         96	    182
105        92         85         87	    177
106        87         95         92	    182
107        94         90         91	    184
108        76         88         81	    164
========== ========== ========== ========== ==========

Let’s say now that we wanted a column that gave the average of the midterm scores. In this case, we’d use the AggregateCols() method to create a new column with the mean of the midterm columns, row by row. The AggregateCols() function looks like this:: 

      	  >>> table.AggregateCols(AggAttrs, AggOp, NewColName)

Where AggAttrs is the list of columns you’re working with (it can be more than two), and AggOp is the operation you want to perform from the options: aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, aaMedian. We’ll choose aaMean for our purposes here. Last, you’ll again provide the string name of the new column you’d like to create! 

Here is the code for getting the mean over the midterm scores:: 

     	>>> AggAttrs = snap.TStrV()
	>>> AggAttrs.Add(“Midterm1”)
	>>> AggAttrs.Add(“Midterm2”)
	>>> grade_table.AggregateCols(AggAttrs, snap.aaMean, “MidtermMean”)

With the result:


.. table:: Student Grades
   :widths: 15 10 10 10	10 10
========== ========== ========== ========== =========== ==========
StudentID  Midterm1   Midterm2   Final      MidScoreSum MidtermMean
========== ========== ========== ========== =========== ==========
101        79         86         88         165	        82.5
102        84         80         79         164	        82
103        56         76         80         132	        66
104        90         92         96         182	        91
105        92         85         87         177	        88.5
106        87         95         92         182	        91
107        94         90         91         184	        92
108        76         88         81         164	        82
========== ========== ========== ========== =========== ==========

A similar methodology can be used for all of the column operation functions for :class:`TTable`s. 

One important feature of this function group is: If the third parameter passed is an empty string, i.e.:: 

    	      >>> table.ColDiv(“Col1”, “Col2”, “”)

then the results will overwrite the values in the column of the first parameter. In this case, the results of dividing Col1 values by Col2 values would replace the values in Col1. 

Rowwise Table Operations
========================

The operations shown above focused on creating new data from some combination of two pre-existing columns. Now, we’ll look at operations that summarize or elucidate information about the table: namely, the Group(), Aggregate(), AggregateCols(), Select(), and Unique() functions. These methods affect the table in different ways. Here, we will describe the use cases of the most important features. 

First, we will investigate the Select() function family, which consists of select_const(), select_atomic(), and select(). You will usually use the first two, as select() is utilized for complex, layered selecting parameters. 

First, let’s look at select_const(), which allows you to select rows based on their value in a single column. For example, perhaps you want to select students who had final scores of 90 or above. Here are the general parameters of select_const():

table.select_const(column, val, cmp, selected_table)
Column is the column we want to select on. This would be final scores in the example above. Val is the value we want to compare to, which is 90 in the example above. Cmp is the comparator we want to use, with choices of less then (LT), less than or equal to (LTE), equal to (EQ), not equal to (NEQ), greater than or equal to (GTE), greater than (GT), substring of (SUBSTR), or superstring of (SUPERSTR). In the example above, we want to use greater than or equal to (GTE). Finally, we need to provide a selected_table, the table that we want add the selected rows to. Generally, using a new blank table is the right option. 

Here’s the code to select only rows where the final score is greater than or equal to 90. Let’s assume we’ve greater a new blank :class:`TTable` called above_90_table::

       	   >>> grade_table.select_const(“Final”, 90, snap.GTE, above_90_table)

Let’s now look at the Group() and Unique() functions. The Group() function allows us to create a new column to label each column according to shared attributes: 

      	  >>> Group(GroupByAttrs, GroupAttrName, Ordered=True)

Here, GroupByAttrs are the columns we want to group with respect to, where their values are the same. GroupAttrName will be the name of the new column with the labels. Let’s say we wanted to group students by their midterm mean score. As we can see above, two students scored an average 91, and two students scored an average 82, so we will see some groups developed. Let’s write the code for this operation: 

      		   >>> groupAttrs = snap.TStrV()
		   >>> groupAttrs.Add(“MidtermMean”)
		   >>> table.Group(groupAttrs, ”MeanGroups”, snap.TBool(True))
Which yields: 

.. table:: Student Grades
   :widths: 15 10 10 10 10 10 10
========== ========== ========== ========== =========== =========== ==========
StudentID  Midterm1   Midterm2   Final      MidScoreSum MidtermMean MeanGroups
========== ========== ========== ========== =========== =========== ==========
101        79         86         88         165         82.5        0
102        84         80         79         164         82          1
103        56         76         80         132         66          2
104        90         92         96         182         91          3
105        92         85         87         177         88.5        4
106        87         95         92         182         91          3
107        94         90         91         184         92          5
108        76         88         81         164         82          1
========== ========== ========== ========== =========== =========== ==========

Another related method is Unique(). Rather than assigning the same labels to rows with similar values, any rows with the same sought-after values will be deleted so there are no remaining duplicates:: 

		>>> Unique(Attrs, Ordered=True)
Here, Attrs is simply the attributes that need to be equal in order for us to consider them duplicates. 

Let’s try this on the original table, and instead of grouping by the midterm mean, we’ll use Unique() to keep only students with a unique midterm mean score:: 

      	  >>> attrs = snap.TStrV()
	  >>> attrs.Add(“MidtermMean”, snap.TBool(True))
	  >>> table.Unique(attrs)

Which would instead yield: 

.. table:: Student Grades
   :widths: 15 10 10 10 10 10
========== ========== ========== ========== =========== ==========
StudentID  Midterm1   Midterm2   Final      MidScoreSum MidtermMean
========== ========== ========== ========== =========== ==========
101        79         86         88         165         82.5
102        84         80         79         164         82
103        56         76         80         132         66
104        90         92         96         182         91
105        92         85         87         177         88.5
========== ========== ========== ========== =========== ==========

Students 106 and 108 have been removed because they had the same midterm mean score as students before them. Remember that Unique() goes from top to bottom row, so earlier rows will be preserved. 

Now, let’s investigate the Aggregate method, which allows us to aggregate statistics for each row based on values in certain columns. For example, we might want to add a column telling us how many instances of the AuthorID in each row exist in the dataset. Aggregate() is invoked as follows:: 

     	   >>> Aggregate(GroupByAttrs, AggOp, ValAttr, ResAttr, Ordered=True)

The Aggregate method takes:
- GroupByAttrs: The attributes (columns) that you want to aggregate with respect to. This will need to be a vector of strings that you create in advance. 
- AggOp: The operation you want to aggregate by: options are aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, or aaMedian. 
- ValAttr: Which attribute (column) we want to aggregate over. 
- ResAttr: The name of the column where the result of the aggregation will be stored. 
- Ordered: Whether to treat grouping keys as ordered or unordered. 

To make all this more concrete, let’s say we wanted to find the maximum final score over all students based on a particular mean midterm score. That is, for students with the same midterm score, we will add a value to their row indicating the highest final score achieved by someone with their same score. Here’s how we would use Aggregate() to do so::

   	>>> GroupBy = snap.TStrV()
	>>> GroupBy.Add("MidtermMean")
	>>> PapAuthT.Aggregate(GroupBy, snap.aaMax, "Final", "MaxFinal", snap.TBool(False))

Here, we use a variable GroupBy to hold a vector of strings representing the columns we want to group with respect to, that is, the MidtermMean column. We then use Aggregate with the snap.aaCount function to count the number of times each mean appears in the dataset, and store the count in a new column called MeanCount. Here is what the result will look like:

.. table:: Student Grades
   :widths: 15 10 10 10 10 10 10

========== ========== ========== ========== =========== =========== ===========
StudentID  Midterm1   Midterm2   Final      MidScoreSum MidtermMean	MaxFinal
========== ========== ========== ========== =========== =========== ===========
101        79         86         88         165         82.5	    88
102        84         80         79         164         82		    81
103        56         76         80         132         66		    80
104        90         92         96         182         91		    96
105        92         85         87         177         88.5	    87
106        87         95         92         182         91		    96
107        94         90         91         184         92		    91
108        76         88         81         164         82		    81
========== ========== ========== ========== =========== =========== ===========

As you can see, the MaxFinal values indicate the highest final score value for students with the same midterm mean. Notably, we see that students 102 and 108 have the same value, because they have the same midterm score, and their value is the maximum of either of their final scores (81 being higher than 79). The same occurred for students 104 and 106. 

Two Table Operations
====================

Some SNAP :class:`TTable` operations help us to combine two different tables into a single table according to various rules. These functions include Intersection, Union, Join, and Minus. They work as follows: 
- Intersection: creates a new table from all rows that appear in both original tables. Returns a new table.
- Union: creates a new table from all rows that appear in either original table. Returns a new table. *UnionAll has a similar function, but retains duplicates of rows across the tables. 
- Minus: creates a new table from all rows in the first table not present in the second table. Returns a new table.
- Join: a more customizable function, Join equi-joins two tables based on one attribute in the first table. Columns from the second table will be added to the first where the value of the desired attribute in the first table matches the value of the desired attribute in the second. Does not return a new table, but rather updates the original table with columns from the second table. 
- SimJoin: a function that performs an equi-join if the distance between two rows is less than the specified threshold.

Let’s go back to our original grade table with four columns: StudentID, Midterm1, Midterm2, and Final. Let’s say we have another table that lists the student IDs of these students, plus a column with their names:

.. table:: Student Names
   :widths: 15 10
========= ==========
ID	      Name
========= ==========
101	      Will
102	      Amira
103	      Todd
104	      Yang
105	      Catherine
106	      Shubash
107	      Nicolo
108	      Maria
========= ==========

Let’s say we want to incorporate the Name column into our original table. We can do this using the Join() function. Here is the prototype for it:: 

      	  >>> table.Join(Attr1, PTable, Attr2)

Here, Attr1 is the column we want to join on from the first table, PTable is the second table we want to join with, and Attr2 is the column we want to join on from the second table. 

To combine our two tables, we would use:: 

   	   >>> combined_table = grade_table.Join(“StudentID”, name_table, “ID”)

Which will create a new table called ‘combined_table’ as so:

.. table:: Student Grades
   :widths: 15 10 10 10 10

========== ========== ========== ========== ==========
StudentID  Midterm1   Midterm2   Final      Name
========== ========== ========== ========== ==========
101        79         86         88         Will
102        84         80         79         Amira
103        56         76         80         Todd
104        90         92         96         Yang
105        92         85         87         Catherine
106        87         95         92         Shubash
107        94         90         91         Nicolo
108        76         88         81         Maria
========== ========== ========== ========== ==========

Getting Information from Tables
===============================

SNAP has many functions to get information from :class:`TTable`s, in the form of vectors or basic data types. Some of the most useful get functions include: 
- GetNumRows
- GetSchema
- GetIntVal, GetFltVal, and GetStrVal
- GetIntValAtRowIdx, GetFltValAtRowIdx, and GetStrValAtRowIdx
- ReadIntCol, ReadFltCol, and ReadStrCol

These functions are relatively straightforward, and will assist with obtaining pieces of information and summary statistics from the :class:`TTable`. The Val functions return single values, and the Col functions return vectors of entire column values. 


TTable
======

.. class:: TTable()
           TTable(Context)
           TTable(S, Context)
           TTable(SIn, Context)
           TTable(H, Col1, Col2, Context, IsStrKeys=False)
           TTable(Table, const TIntV& RowIds)
           TTable(Table)

   Returns a new table. If no parameters are provided, an empty table is returned. If
   *S* and *Context* are provided, the table is initialized with the provided Schema and
   TTableContext. If *SIn* is provided, the table is read from the binary stream. If *H*, a
   :class:`THash` with :class:`TInt` keys and either :class:`TInt` or :class:`TFlt` values,
   is given, the TTable is constructed from the hash table. If *IsStrKeys* is True, then 
   the :class:`TInt` keys in *H* refer to strings in the *Context*. *Col1* provides the name
   for the keys in *H* in the schema for the table and *Col2* does the same for the values.
   If *Table* is provided, the contents of *Table* are copied into the current table. If
   *RowIds* is given, then only those particular rows are copied.

   Below is a list of functions supported by the :class:`TTable` class:

      .. describe:: AddDstNodeAttr(Attr)

         Adds column with name *Attr* to be used as the destination node attribute
         of the graph.

      .. describe:: AddDstNodeAttr(Attrs)

         Adds columns with the names specified in *Attrs*, a :class:`TStrV`, to be used as
         destination node attributes of the graph.

      .. describe:: AddEdgeAttr(Attr)

         Adds column with name *Attr* to be used as graph edge attribute.

      .. describe:: AddEdgeAttr(Attrs)

         Adds columns, with names provided in *Attrs*, to be used as graph edge attributes.

      .. describe:: AddNodeAttr(Attr)

         Adds column with name *Attr* to be used as node attribute (both source and destination).

      .. describe:: AddNodeAttr(Attrs)

         Adds columns, with names provided in *Attrs*, to be used as node attribute 
         (both source and destination).

      .. describe:: AddSrcNodeAttr(Attr)

         Adds column with name *Attr* to be used as the source node attribute
         of the graph.

      .. describe:: AddSrcNodeAttr(Attrs)

         Adds columns with the names specified in *Attrs*, a :class:`TStrV`, to be used as
         source node attributes of the graph.

      .. describe:: Aggregate(GroupByAttrs, AggOp, ValAttr, ResAttr, Ordered=True)

         Aggregates values over one attribute, *ValAttr*, after grouping with respect to a
         list of attributes given in *GroupByAttrs*. Results are stored in a new attribute
         with name *ResAttr*. *Ordered* indicates whether to treat grouping key as ordered
         (true) or unordered. *AggOp* gives the aggregation policy. It must be one of
         aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, or aaMedian.

      .. describe:: AggregateCols(AggrAttrs, AggOp, ResAttr)

          For each row in the table, aggregates values over a list of attributes given by *AggrAttrs*. Results are stored in a new attribute *ResAttr*. *AggOp* gives the aggregation policy.
          It must be one of aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, aaMedian

      .. describe:: BegRI()

         Gets an iterator to the first valid row of the table. Returns a :class:`TRowIterator`.

      .. describe:: BegRIWR()

         Gets an iterator to remove the first valid row. Returns a :class:`TRowIteratorWithRemove`.

      .. describe:: Classify(Predicate, LabelAttr, PositiveLabel, NegativeLabel)

         Adds a label attribute, *LabelAttr*, with positive labels, a :class:`TInt` given by
         *PositiveLabel*, on rows selected according to the :class:`TPredicate` *Predicate*,
         and negative labels, a :class:`TInt` given by *NegativeLabel*, on the rest.

      .. describe:: ClassifyAtomic(Attr1, Attr2, Cmp, LabelAttr, PositiveLabel,
                                   NegativeLabel)

         Adds an integer label attribute, *LabelAttr*, with positive labels, given by *PositiveLabel*,
         on selected rows and negative labels, given by *NegativeLabel*, on the rest. Rows are
         selected using the atomic compare operator of type :class:`TPredComp`, *Cmp*, over
         *Attr1* and *Attr2*. *Cmp* must be one of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR.

      .. describe:: ColAdd(Attr1, Attr2, ResAttr=:class:`TStr`(""))
                    ColAdd(Attr1, Table, Attr2, ResAttr=:class:`TStr`(""), AddToFirstTable)
                    ColAdd(Attr1, Value, ResAttr=:class:`TStr`(""), FloatCast)

         Performs the operation *Attr1* + *Attr2*, where *Attr1* and *Attr2* are attributes
         which can belong to the same or different tables. Could also perform *Attr1* + *Value*, 
         depending on the function prototype. The result is stored in a new attribute, *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding to *Attr1*. 
         If *FloatCast*, a :class:`TBool`, is set to true, then values in Int columns are cast to 
         Flt values. *AddToFirstTable* is a flag specifying whether to add *ResAttr* to the table 
         corresponding to the caller (true), or to the table *Table*. **NOTE**: This operation 
         does not work on String columns.

      .. describe:: ColConcat(Attr1, Attr2, Separator, ResAttr=:class:`TStr`(""))
                    ColConcat(Attr1, Table, Attr2, Separator, ResAttr=:class:`TStr`(""), AddToFirstTable)

         Concatenates the two columns given by *Attr1* and *Attr2*, separated by *Separator*.
         *Table* specifies the :class:`TTable` *Attr2* comes from. The result is stored in a
         new column, *ResAttr*. If *ResAttr* = "", the result is stored instead in the column
         corresponding to *Attr1*. *AddToFirstTable* is a flag specifying whether to add *ResAttr* 
         to the table corresponding to the caller (true), or to the table *Table*. **NOTE**: 
         This operation only works on String columns.

      .. describe:: ColConcatConst(Attr, Value, Separator, ResAttr=:class:`TStr`(""))

        Concatenates values for column *Attr* with the given string value *Value*, separated 
        by *Separator*. Result is stored in a new column *ResAttr*. If *ResAttr* = "", the
        result is stored instead in the column corresponding to *Attr1*. **NOTE**: This operation
        only works on String columns.

      .. describe:: ColDiv(Attr1, Attr2, ResAttr=:class:`TStr`(""))
                    ColDiv(Attr1, Table, Attr2, ResAttr, AddToFirstTable)
                    ColDiv(Attr1, Value, ResAttr=:class:`TStr`(""), FloatCast)

         Performs the operation *Attr1* / *Attr2*, where *Attr1* and *Attr2* are attributes
         which can belong to the same or different tables. Could also perform *Attr1* / *Value*, 
         depending on the function prototype. The result is stored in a new attribute, *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding to *Attr1*.
         If *FloatCast*, a :class:`TBool`, is set to true, then values in Int columns are cast to 
         Flt values. *AddToFirstTable* is a flag specifying whether to add *ResAttr* to the table 
         corresponding to the caller (true), or to the table *Table*. **NOTE**: This operation 
         does not work on String columns.

      .. describe:: ColMax(Attr1, Attr2, ResAttr=:class:`TStr`(""))

         Performs the operation MAX (*Attr1*, *Attr2*), where *Attr1* and *Attr2* 
         are attributes in a table. The result is stored in a new column *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding
         to *Attr1*. **NOTE**: This operation does not work on String columns.


      .. describe:: ColMin(Attr1, Attr2, ResAttr=:class:`TStr`(""))

         Performs the operation MIN (*Attr1*, *Attr2*), where *Attr1* and *Attr2* 
         are attributes in a table. The result is stored in a new column *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding
         to *Attr1*. **NOTE**: This operation does not work on String columns.

      .. describe:: ColMod(Attr1, Attr2, ResAttr)
                    ColMod(Attr1, Table, Attr2, ResAttr, AddToFirstTable)
                    ColMod(Attr1, Value, ResAttr, FloatCast)

         Performs the operation *Attr1* % *Attr2*, where *Attr1* and *Attr2* are attributes
         which can belong to the same or different tables. Could also perform *Attr1* % *Value*, 
         depending on the function prototype. The result is stored in a new attribute, *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding to *Attr1*.
         If *FloatCast*, a :class:`TBool`, is set to true, then values in Int columns are cast to 
         Flt values. *AddToFirstTable* is a flag specifying whether to add *ResAttr* to the table 
         corresponding to the caller (true), or to the table *Table*. **NOTE**: This operation 
         does not work on String or float columns.

      .. describe:: ColMul(Attr1, Attr2, ResAttr)
                    ColMul(Attr1, Table, Attr2, ResAttr, AddToFirstTable)
                    ColMul(Attr1, Value, ResAttr, FloatCast)

         Performs the operation *Attr1* * *Attr2*, where *Attr1* and *Attr2* are attributes
         which can belong to the same or different tables. Could also perform *Attr1* * *Value*, 
         depending on the function prototype. The result is stored in a new attribute, *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding to *Attr1*.
         If *FloatCast*, a :class:`TBool`, is set to true, then values in Int columns are cast to 
         Flt values. *AddToFirstTable* is a flag specifying whether to add *ResAttr* to the table 
         corresponding to the caller (true), or to the table *Table*. **NOTE**: This operation 
         does not work on String columns.

      .. describe:: ColSub(Attr1, Attr2, ResAttr)
                    ColSub(Attr1, Table, Attr2, ResAttr, AddToFirstTable)
                    ColSub(Attr1, Value, ResAttr, FloatCast)

         Performs the operation *Attr1* - *Attr2*, where *Attr1* and *Attr2* are attributes
         which can belong to the same or different tables. Could also perform *Attr1* - *Value*, 
         depending on the function prototype. The result is stored in a new attribute, *ResAttr*.
         If *ResAttr* = "", the result is stored instead in the column corresponding to *Attr1*.
         If *FloatCast*, a :class:`TBool`, is set to true, then values in Int columns are cast to 
         Flt values. *AddToFirstTable* is a flag specifying whether to add *ResAttr* to the table 
         corresponding to the caller (true), or to the table *Table*. **NOTE**: This operation 
         does not work on String columns.

      .. describe:: Count(Attr, ResAttr)

         For each row of the table, counts number of rows in the table sharing the same value
         as it for a given attribute *Attr*, a :class:`TStr`. The result is stored in a new
         attribute, *ResAttr*.

      .. describe:: EndRI()

         Gets an iterator to the last valid row of the table. Returns a :class:`TRowIterator`.


      .. describe:: EndRIWR()

         Gets an iterator to remove the last valid row. Returns a :class:`TRowIteratorWithRemove`.


      .. describe:: GetColType(Attr)

         Gets type of an attribute *Attr*. Returns a :class:`TAttrType` object representing 
         attribute type.

      .. describe:: GetDstCol()

         Returns the name, a :class:`TStr`, of the column representing destination nodes
         in the graph.

      .. describe:: GetDstNodeFltAttrV()

         Returns the names of the Flt columns, in a :class:`TStrV`, corresponding to attributes
         of the destination nodes.

      .. describe:: GetDstNodeIntAttrV()

         Returns the names of the Int columns, in a :class:`TStrV`, corresponding to attributes
         of the destination nodes.

      .. describe:: GetDstNodeStrAttrV()

         Returns the names of the Str columns, in a :class:`TStrV`, corresponding to attributes
         of the destination nodes.

      .. describe:: GetEdgeFltAttrV()

         Returns the names of the Flt columns, in a :class:`TStrV`, corresponding to edge 
         attributes.

      .. describe:: GetEdgeIntAttrV()

         Returns the names of the Int columns, in a :class:`TStrV`, corresponding to edge 
         attributes.

      .. describe:: GetEdgeStrAttrV()

         Returns the names of the Str columns, in a :class:`TStrV`, corresponding to edge 
         attributes.

      .. describe:: GetEdgeTable(Network, Context)

         Extracts edge TTable from the :class:`PNEANet` *Network*, using the :class:`TTableContext`
         *Context*. Returns the resulting :class:`PTable`.

      .. describe:: GetEdgeTablePN(Network, Context)

         Extracts edge TTable from the :class:`PNGraphMP` *Network*, using the :class:`TTableContext`
         *Context*. Returns the resulting :class:`PTable`. **NOTE**: Defined only if OpenMP present.

      .. describe:: GetFltNodePropertyTable(Network, Property, NodeAttrName, NodeAttrType, PropertyAttrName, Context)

         Extracts node and and edge property TTables from a THash. *Network* is of type
         :class:`PNEANet`, *Property* is a :class:`TIntFltH`, *NodeAttrName* and
         *PropertyAttrName* are :class:`TStr`s, *NodeAttrType* is a :class:`TAttrType`, and
         *Context* is a :class:`TTableContext`. Returns a :class:`PTable` object.

      .. describe:: GetFltVal(Attr, RowIdx)

         Gets the value of float attribute with name *Attr* at row *RowIdx*.

      .. describe:: GetFltValAtRowIdx(ColIdx, RowIdx)

         Gets the value of the float column at index *ColIdx* at row *RowIdx*.

      .. describe:: GetIntVal(Attr, RowIdx)

         Gets the value of integer attribute with name *Attr* at row *RowIdx*.

      .. describe:: GetIntValAtRowIdx(ColIdx, RowIdx)

         Gets the value of the integer column at index *ColIdx* at row *RowIdx*.

      .. describe:: GetMP()

         Returns the value of the static variable TTable::UseMP, which controls whether
         to use multi-threading. TTable::UseMP is 1 by default (meaning algorithms are
         multi-threaded by default if the OpenMP library is present).

      .. describe:: GetMapHitsIterator(GraphSeq, Context, MaxIter=20)

         Computes a sequence of Hits tables for a graph sequence *GraphSeq*, a
         :class:`TVec<snap.PNEANet>`. A :class:`TTableIterator` is returned.

      .. describe:: GetMapPageRank(GraphSeq, Context, C=0.85, Eps=1e-4, MaxIter=100)

         Computes a sequence of PageRank tables for a graph sequence *GraphSeq*, a
         :class:`TVec<snap.PNEANet>`. A :class:`TTableIterator` is returned.

      .. describe:: GetNodeTable()

         Extracts node TTable from :class:`PNEANet` *Network*, using :class:`TTableContext` *Context*.

      .. describe:: GetNumRows()

         Returns total number of rows in the table. Count could include
         rows which have been deleted previously.

      .. describe:: GetNumValidRows()

         Returns total number of valid rows in the table.

      .. describe:: GetSchema()

         Returns the schema of the table. Return type is :class:`Schema`.

      .. describe:: GetSrcCol()

         Returns the name of the column representing source nodes in the graph.

      .. describe:: GetSrcNodeFltAttrV()

         Returns the names of the Flt columns corresponding to attributes of the 
         source nodes. Return type is :class:`TStrV`.

      .. describe:: GetSrcNodeIntAttrV()

         Returns the names of the Int columns corresponding to attributes of the 
         source nodes. Return type is :class:`TStrV`.

      .. describe:: GetSrcNodeStrAttrV()

         Returns the names of the Str columns corresponding to attributes of the 
         source nodes. Return type is :class:`TStrV`.

      .. describe:: GetStrVal(Attr, RowIdx)

         Gets the value of string attribute with name *Attr* at row *RowIdx*.

      .. describe:: Group(GroupByAttrs, GroupAttrName, Ordered=True)

         Groups rows according to the attributes specified by GroupByAttrs, a :class:`TStrV`.
         Result is stored in a new column of the table with name *GroupAttrName*.

      .. describe:: Intersection(PTable)

         Returns a new table containing rows present in the current table
         that are also present in *PTable*, which is of type :class:`PTable`.

      .. describe:: Join(Attr1, PTable, Attr2)

         Performs an equi-join on the current table and another table, *PTable* over
         attributes *Attr1* in the current table and *Attr2* in *PTable*.

      .. describe:: Load(SIn, Context)

         Loads table from the input stream *SIn* using
         :class:`TTableContext` *Context*. Returns a :class:`PTable`.

      .. describe:: LoadSS(Schema, InFNm, Context, Separator='\\t', HasTitleLine=False)

         Loads table from spread sheet (TSV, CSV, etc). *Schema* is a :class:`Schema` object,
         *InFNm* provides the input file name, *Context is a :class:`TTableContext`, *Separator*
         is the field separator character in the input file, and HasTitleLine indicates whether
         the first line is a title line with the name of the columns (without a # preceding it).
         If *HasTitleLine* is True, then *Schema* is validated against it.

      .. describe:: Minus(PTable)

         Returns a new table containing rows present in the current table which are not
         present in another table given by *PTable*.

      .. describe:: Order(OrderByAttrs, ResAttr, ResetRankFlag=False, Asc=True)

         Orders the rows according to the values in *OrderByAttrs* (a :class:`TStrV`).
         Results are stored in new column with name *ResAttr*. If *Asc* is True, rows
         are ordered in ascending lexicographic order.

      .. describe:: Project(ProjectAttrs)

         Returns a table with only the attributes in *ProjectAttrs*, a :class:`TStrV`.

      .. describe:: ProjectInPlace(ProjectAttrs)

         Modifies the current table to keep only the attributes specified 
         in *ProjectAttrs*.

      .. describe:: ReadFltCol(Attr, Result)

         Reads values of an entire float column given by *Attr* into the :class:`TFltV`
         *Result*.

      .. describe:: ReadIntCol(Attr, Result)

         Reads values of an entire int column given by *Attr* into the :class:`TFltV`
         *Result*.

      .. describe:: ReadStrCol(Attr, Result)

         Reads values of an entire string column given by *Attr* into the :class:`TFltV`
         *Result*.

      .. describe:: Rename(Attr, NewAttr)

         Renames an attribute with name *Attr* to new name *NewAttr* in a table. 


      .. describe:: SaveBin(OutFNm)

         Saves table schema and content into a binary file with name *OutFNm*.

      .. describe:: SaveSS(OutFNm)

         Saves table schema and content into a TSV file with name *OutFNm*.

      .. describe:: Select(Predicate, SelectedRows, Remove=True)

         Selects rows that satisfy a given Predicate, of type :class:`TPredicate`.
         The selected row indices are stored in *SelectedRows*, a :class:`TIntV`. If
         *Remove* is True, rows that do not match the predicate are removed.

      .. describe:: SelectAtomic(Attr1, Attr2, Cmp, SelectedRows, Remove=True)

         Selects rows which satisfy an atomic compare operation, *Cmp*, of type
         :class:`TPredComp`. *Cmp* must be one of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, 
         or SUPERSTR. The selected row indices are stored in *SelectedRows*,
         a :class:`TIntV`. If *Remove* is True, rows that do not match the predicate
         are removed.

      .. describe:: SelectAtomicFltConst(Attr, Val, Cmp, SelectedTable)

         Selects rows where the value of a float attribute, *Attr*, satisfies an atomic
         comparison, *Cmp*, with a primitive type *Val*. *Cmp* must be one of LT, LTE,
         EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR. The selected rows are added to the
         :class:`PTable` *SelectedTable*.

      .. describe:: SelectAtomicIntConst(Attr, Val, Cmp, SelectedTable)

         Selects rows where the value of a int attribute, *Attr*, satisfies an atomic
         comparison, *Cmp*, with a primitive type *Val*. *Cmp* must be one of LT, LTE,
         EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR. The selected rows are added to the
         :class:`PTable` *SelectedTable*.

      .. describe:: SelectAtomicStrConst(Attr, Val, Cmp, SelectedTable)

         Selects rows where the value of a string attribute, *Attr*, satisfies an atomic
         comparison, *Cmp*, with a primitive type *Val*. *Cmp* must be one of LT, LTE, EQ,
         NEQ, GTE, GT, SUBSTR, or SUPERSTR. The selected rows are added to the :class:`PTable`
         *SelectedTable*.

      .. describe:: SelectFirstNRows(N)

         Modifies table in place so that it only its first *N* rows are retained.

      .. describe:: SelfJoin(Attr)

         Performs a self-join on the table on the attribute *Attr*. Returns a new table.

      .. describe:: SelfSimJoin(Attrs, DistColAttr, SimType, Threshold)

         Performs a self sim-join on a table. Performs join if the distance between two rows is
         less than the specified float threshold *Threshold*. *SimType* should be one of L1Norm,
         L2Norm, Jaccard, and Haversine. *Attrs* gives the list of attributes for computing the
         distance between rows. *DistColAttr* is the name of the attribute representing the
         distance between rows in the new table. A new :class:`PTable` is returned.

      .. describe:: SetCommonNodeAttrs(SrcAttr, DstAttr, CommonAttr)

         Sets the columns to be used as both source and destination node 
         attributes. All input parameters should be strings.

      .. describe:: SetDstCol(Attr)

         Sets the column representing destination nodes in the graph.

      .. describe:: SetMP(Value)

         Sets the value of the static variable TTable::UseMP to *Value*, an integer.

      .. describe:: SetSrcCol(Attr)

         Sets the column representing source nodes in the graph.

      .. describe:: SimJoin(Attr1, Table, Attr2, DistColAttr, SimType, Threshold)

         Performs SimJoin on the current table and *Table*. Performs join if the distance between
         two rows is less than the specified float threshold *Threshold*. *SimType* should be one
         of L1Norm, L2Norm, Jaccard, and Haversine. *Attrs* gives the list of attributes for computing
         the distance between rows. *DistColAttr* is the name of the attribute representing the
         distance between rows in the new table. A new :class:`PTable` is returned.

      .. describe:: SpliceByGroup(GroupByAttrs, Ordered)

         Splices table into subtables according to the result of a grouping statement. *GroupByAttrs*
         is a :class:`TStrV`, an attribute vector grouping should be performed with respect to.
         *Ordered* is a flag specifying whether to treat the grouping key as ordered or unordered.

      .. describe:: StoreFltCol(ColName, ColVals)

         Adds entire float column to the table. *ColName* gives the column name and *ColVals* is
         :class:`TFltV` giving the vector of column values.

      .. describe:: StoreIntCol(ColName, ColVals)

         Adds entire int column to the table. *ColName* gives the column name and *ColVals* is
         :class:`TIntV` giving the vector of column values.

      .. describe:: StoreStrCol(ColName, ColVals)

         Adds entire string column to the table. *ColName* gives the column name and *ColVals* is
         :class:`TStrV` giving the vector of column values.

      .. describe:: TableFromHashMap(HashMap, Attr1, Attr2, Context)

         Returns a table constructed from the given hash map *HashMap* of type :class:`TIntH`
         or :class:`TIntFltH`. *Attr1* is the name of the attribute corresponding to the first
         column and *Attr2* for the second column.

      .. describe:: ToGraphSequence(SplitAttr, AggrPolicy, WindowSize, JumpSize, StartVal, EndVal)

         Returns a sequence of graphs created from the table, where partitioning is based on
         values of column with name *SplitAttr* and windows are specified by *JumpSize* and
         *WindowSize*. *AggrPolicy* is a  :class:`TAttrAggr` indicating the policy for
         aggregating node attribute values when a node appears in multiple rows of the table.
         It must be one of aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, or aaMedian.
         *WindowSize* gives the partition size, and *JumpSize* gives the spacing of the
         partitions. Only values of *SplitAttr* between *StartVal* and *EndVal*, inclusive,
         are considered.

      .. describe:: ToVarGraphSequence(SplitAttr, AggrPolicy, SplitIntervals)

         Returns a sequence of graphs created from the table, where partitioning is based on values of column *SplitAttr* and intervals specified by *SplitIntervals*. *SplitIntervals* is a
         :class:`TIntPrV` that gives the start and end *SplitAttr* attribute values for each
         partition of the table. *AggrPolicy* is a  :class:`TAttrAggr` indicating the policy for
         aggregating node attribute values when a node appears in multiple rows of the table.

      .. describe:: ToGraphPerGroup(GroupAttr, AggrPolicy)

         Returns a sequence of graphs created from the table, where partitioning is based on
         the group mappings specified by values of attribute *GroupAttr*. *AggrPolicy* is the
         policy for aggregating node attribute values. It must be one of aaSum, aaCount, aaMin, aaMax,
         aaFirst, aaLast, aaMean, aaMedian

      .. describe:: ToGraphSequenceIterator(SplitAttr, AggrPolicy, WindowSize, JumpSize, StartVal, EndVal)

         Similar to ToGraphSequence, but instead of returning the sequence of graphs,
         returns the first graph in the sequence. To iterate over the sequence, use
         TTable::NextGraphIterator and TTable::IsLastGraphOfSequence.

         Calls to TTable::NextGraphIterator() will generate graphs one at a time. This is
         beneficial when the entire graph sequence cannot fit in memory.

      .. describe:: ToVarGraphSequenceIterator(SplitAttr, AggrPolicy, SplitIntervals)

         Similar to ToVarGraphSequence, but instead of returning the sequence of graphs,
         returns the first graph in the sequence. To iterate over the sequence, use
         TTable::NextGraphIterator and TTable::IsLastGraphOfSequence.

         Calls to TTable::NextGraphIterator() will generate graphs one at a time. This is
         beneficial when the entire graph sequence cannot fit in memory.

      .. describe:: ToGraphPerGroupIterator(GroupAttr, AggrPolicy)

         Similar to ToGraphPerGroupSequence, but instead of returning the entire sequence
         of graphs, returns the first graph in the sequence. To iterate over the sequence,
         use :class:`TTable`::NextGraphIterator and :class:`TTable`::IsLastGraphOfSequence.

         Calls to :class:`TTable`::NextGraphIterator() will generate graphs one at a time. This
         is beneficial when the entire graph sequence cannot fit in memory.

      .. describe:: NextGraphIterator()

         Returns the next graph, a :class:`PNEANet` object, in the sequence defined
         by one of the TTable::ToGraph*Iterator functions. Calls to this function must
         be preceded by a single call to one of the above TTable::ToGraph*Iterator functions.

      .. describe:: IsLastGraphOfSequence()

        Checks if the graph sequence defined by one of the TTable::ToGraph* Iterator
        functions has been completely iterated over. Calls to this function must be
        preceded by a single call to one of the above TTable::ToGraph*Iterator functions.

      .. describe:: Union(PTable)

         Returns a new table containing rows present in either one of the current
         table and the passed table. Duplicate rows across tables may not be preserved.

      .. describe:: UnionAll(PTable)

         Returns a new table containing rows present in either one of the
         current table and the passed table, *PTable*. Duplicate rows across tables
         are preserved.

      .. describe:: Unique(Attrs, Ordered=True)

         Removes rows with duplicate values across the given attributes in *Attrs*.
         If *Ordered* is True, values across attributes are treated as an ordered pair.


      .. describe:: GetIntRowIdxByVal(const TStr& ColName, const TInt& Val)

         Gets a vector containing the indices of rows containing Val in int column ColName.
         Uses an index if it has been requested explicitly; else, it loops over all the rows.
         Be sure to request an index using :meth:`RequestIndexInt` first if you will call this multiple times.

      .. describe:: GetStrRowIdxByMap(const TStr& ColName, const TInt& Map)

         Gets a vector containing the indices of rows containing the integer Map (which maps to a string) in str column ColName.
         Uses an index if it has been requested explicitly; else, it loops over all the rows.
         Be sure to request an index using :meth:`RequestIndexStrMap` first if you will call this multiple times.

      .. describe:: GetFltRowIdxByVal(const TStr& ColName, const TFlt& Val)

         Gets a vector containing the indices of rows containing Val in flt column ColName.
         Uses an index if it has been requested explicitly; else, it loops over all the rows.
         Be sure to request an index using :meth:`RequestIndexFlt` first if you will call this multiple times.

      .. describe:: RequestIndexInt(const TStr& ColName)
        
         Creates a hash-based index for int column ColName, so that the rows containing a particular
         value can be retrieved efficiently. Used by :meth:`GetIntRowIdxByVal`

      .. describe:: RequestIndexFlt(const TStr& ColName)
        
         Creates a hash-based index for float column ColName, so that the rows containing a particular
         value can be retrieved efficiently. Used by :meth:`GetFltRowIdxByVal`

      .. describe:: RequestIndexStrMap(const TStr& ColName)
        
         Creates a hash-based index for string column ColName, using the integer mappings,
         so that the rows containing a particular value can be retrieved efficiently. 
         Used by :meth:`GetStrRowIdxByMap`

TAtomicPredicate
=================

.. class:: TAtomicPredicate()
           TAtomicPredicate(Typ, IsCnst, Cmp, L, R)
           TAtomicPredicate(Typ, IsCnst, Cmp, L, R, ICnst, FCnst, SCnst)

   Returns a new atomic predicate, for encapsulating common operations. *Typ* provides the type
   of the predicate variables, *IsCnst* is a flag indicating if this atomic node represents
   a constant value, *Cmp* is one of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR, *L* and *R*
   are strings giving the left and right variable of the comparison op, and *ICnst*, *FCnst*, and
   *SCnst* give the int, float, and str constant value to use if the object is a constant of the
   respective type,

TPredicateNode
==============

.. class:: TPredicateNode()
           TPredicateNode(A)
           TPredicateNode(Opr)
           TPredicateNode(P)

   Returns a new predicate node, which represents a binary predicate operation on 
   two predicate nodes. Specify *A*, a :class:`TAtomicPredicate`, if this is a leaf node,
   *Opr*, one of AND, NOT, NOP, or OR, for logical operation predicate internal nodes, or
   *P*, another :class:`TPredicateNode`, for the copy constructor.

   Below is a list of functions supported by the :class:`TPredicateNode` class:

      .. describe:: AddLeftChild(TPredicateNode* Child)

         Adds *Child* as the left child of the given node. *Child* is a pointer to a
         :class:`TPredicateNode`.

      .. describe:: AddRightChild(TPredicateNode* Child)

         Adds *Child* as the right child of the given node. *Child* is a pointer to a
         :class:`TPredicateNode`.

      .. describe:: GetVariables(Variables)

         Adds variables to *Variables* in the predicate tree rooted at this node. *Variables*
         is a :class:`TStrV`.

TPredicate
==========

.. class:: TPredicate()
           TPredicate(R)
           TPredicate(Pred)

   Returns a new predicate, for encapsulating comparison operations. If *R*, a pointer to a
   :class:`TPredicateNode`, is provided, it constructs a predicate with the given root node.
   If *Pred*, another :class:`TPredicate`, is supplied, the copy constructor is called.

   Below is a list of functions supported by the :class:`TPredicate` class:

      .. describe:: SetIntVal(VarName, VarVal)

         Sets int variable with name *VarName* to value *VarVal*.

      .. describe:: SetFltVal(VarName, VarVal)

         Sets float variable with name *VarName* to value *VarVal*.

      .. describe:: SetStrVal(VarName, VarVal)

         Sets string variable with name *VarName* to value *VarVal*.

      .. describe:: Eval()

         Return the result of evaluating the current predicate.

      .. describe:: EvalAtomicPredicate(Atom)

         Evaluate the give atomic predicate *Atom*.

      .. describe:: GetVariables(Variables)

         Adds variables to *Variables* in the given predicate. *Variables* is a :class:`TStrV`.

TTableContext
=============

.. class:: TTableContext()
           TTableContext(SIn)

   Returns an context object. A :class:`TTableContext` provides the execution context for a
   :class:`TTable`. The context is loaded in binary from *SIn*, if it is provided.

   The Context is primarily used to handle strings. It maps strings in the table to a unique integer.
   To support fast operations, the :class:`TTable` objects store only the corresponding integer for all strings.
   When a program needs to retrive the string value, it does so by using the provided method's in the table's
   :class:`TTableContext`.


   Below is a list of functions supported by the :class:`TTableContext` class:

      .. describe:: Load(SIn)

         Loads context in binary from *SIn*.

      .. describe:: Save(SOut)

         Saves context in binary to *SOut*.

      .. describe:: AddStr(Key)

         Adds string *Key* to the context and returns its *KeyId*.

      .. describe:: GetStr(KeyId)

         Returns the string key for the given *KeyId*.

TPrimitive
==========

.. class:: TPrimitive()
           TPrimitive(Val)
           TPrimitive(Prim)

   Returns a new primitive, a wrapper around primitive types. If provided, initialized with
   primitive type *Val*, which can be an int, float, or string. Providing *Prim*, another
   :class:`TPrimitive`, copies the contents.

   Below is a list of functions supported by the :class:`TPrimitive` class:

      .. describe:: GetInt()

         Returns the int value of the primitive. If the primitive does not represent an int,
         returns -1.

      .. describe:: GetFlt()

         Returns the float value of the primitive. If the primitive does not represent an float,
         returns -1.

      .. describe:: GetStr()

         Returns the string value of the primitive. If the primitive does not represent an 
         string, returns the empty string.

      .. describe:: GetType()

         Returns the type of this primitive.

TTableRow
==========

.. class:: TTableRow()

   Returns a row object for a :class:`TTable`.

   Below is a list of functions supported by the :class:`TTable` class:

      .. describe:: AddInt(Val)

         Adds int attribute to this row.

      .. describe:: AddInt(Val)

         Adds float attribute to this row.

      .. describe:: AddInt(Val)

         Adds string attribute to this row.

      .. describe:: GetIntVals()

         Gets a vector of all the int attributes of this row.

      .. describe:: GetFltVals()

         Gets a vector of all the float attributes of this row.

      .. describe:: GetStrVals()

         Gets a vector of all the string attributes of this row.

TRowIterator
============

.. class:: TRowIterator()

   Returns a new row iterator for :class:`TTable`. Normally, these objects are
   not created directly, but obtained via a call to the table class :class:`TTable`
   method, such as :meth:`BegRI()`, that returns a row iterator.

   Below is a list of functions supported by the :class:`TRowIterator` class:

      .. describe:: Next()

         Increments the iterator.

      .. describe:: GetRowIdx()

         Gets the id of the row pointed by this iterator.

      .. describe:: GetIntAttr(ColIdx)

         Returns the value of integer attribute specified by the integer column index for 
         the current row.

      .. describe:: GetFltAttr(ColIdx)

         Returns the value of float attribute specified by the integer column index for 
         the current row.

      .. describe:: GetStrAttr(ColIdx)

         Returns the value of string attribute specified by the integer column index for 
         the current row.

      .. describe:: GetStrMapById(ColIdx)

         Returns the integer mapping of a string attribute value specified by the string 
         column index for the current row.

      .. describe:: GetIntAttr(Col)

         Returns value of the integer attribute specified by attribute name for the
         current row.

      .. describe:: GetFltAttr(Col)

         Returns value of the float attribute specified by attribute name for the
         current row.

      .. describe:: GetStrAttr(Col)

         Returns value of the string attribute specified by attribute name for the
         current row.

      .. describe:: GetStrMapByName(Col)

         Returns the integer mapping of string attribute specified by attribute name 
         for the current row.

      .. describe:: CompareAtomicConst(ColIdx, Val, Cmp)

         Compares value in column *ColIdx* with given primitive *Val*. *Cmp* must be one 
         of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR.

      .. describe:: CompareAtomicConstTStr(ColIdx, Val, Cmp)

         Compares value in column *ColIdx* with given :class:`TStr` *Val*. *Cmp* must be
         one of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR.

TRowIteratorWithRemove
======================

.. class:: TRowIteratorWithRemove()

   Returns a new row iterator that allows for logical row removal while iterating 
   for :class:`TTable`. Normally, these objects are not created directly, but obtained
   via a call to the table class :class:`TTable` method, such as :meth:`BegRIWR()`, that
   returns a row iterator.

   Below is a list of functions supported by the :class:`TRowIteratorWithRemove` class:

      .. describe:: Next()

         Increments the iterator.

      .. describe:: GetRowIdx()

         Gets the id of the row pointed by this iterator.

      .. describe:: GetNextRowIdx()

         Gets the id of the next row.

      .. describe:: GetNextIntAttr(ColIdx)

         Returns the value of integer attribute specified by the integer column index for 
         the next row.

      .. describe:: GetNextFltAttr(ColIdx)

         Returns the value of float attribute specified by the integer column index for 
         the next row.

      .. describe:: GetNextStrAttr(ColIdx)

         Returns the value of string attribute specified by the integer column index for 
         the next row.

      .. describe:: GetNextIntAttr(Col)

         Returns value of the integer attribute specified by attribute name for the
         next row.

      .. describe:: GetNextFltAttr(Col)

         Returns value of the float attribute specified by attribute name for the
         next row.

      .. describe:: GetNextStrAttr(Col)

         Returns value of the string attribute specified by attribute name for the
         next row.

      .. describe:: IsFirst()

         Checks whether iterator points to first valid row of the table.

      .. describe:: RemoveNext()

         Removes the next row.

      .. describe:: CompareAtomicConst(ColIdx, Val, Cmp)

         Compares value in column *ColIdx* with given primitive *Val*. *Cmp* must be one 
         of LT, LTE, EQ, NEQ, GTE, GT, SUBSTR, or SUPERSTR.

TTableIterator
==============

.. class:: TTableIterator()

   Returns a new iterator over vector of :class:`PTable`. Normally, these objects are
   not created directly, but obtained via a call to the table class :class:`TTable` 
   method, such as :meth:`GetMapPageRank()`, that returns a node iterator.

   Below is a list of functions supported by the :class:`TTable` class:

      .. describe:: Next()

         Returns next table in the sequence and update iterator.

      .. describe:: HasNext()

         Checks if iterator has reached end of the sequence.
