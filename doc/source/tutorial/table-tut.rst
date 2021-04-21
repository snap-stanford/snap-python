Tables
`````````````````````
The :class:`TTable` in SNAP is a table data structure for storing tabular data, which can easily be converted into the SNAP graph. The :class:`TTable` is much more efficient than other tabular data structures and functions seamlessly inside the SNAP universe. The :class:`TTable` can easily store hundreds of millions of rows and perform complex data manipulation operations. 

:class:`TTable` objects can be easily loaded from CSV and TSV files. :class:`TTable` objects can store integers, strings, and floats in its columns. Each column can store exactly one data type, and each column has its own name, a string. 

This tutorial will cover:

* how to create a TTable,
* how to save and load a TTable,
* how to perform columnwise operations on TTables,
* how to perform rowwise operations on TTables,
* how to join two TTables together,
* and how to extract information from a TTable.

Creating a :class:`TTable`
==========================

To create a :class:`TTable` object in SNAP, you must first define the:

* Context: The Context holds information behind-the-scenes about the mappings between integers and strings (which reduces memory usage). You don’t have to do anything with the Context except create it and use it as a parameter when creating your :class:`TTable`. Many :class:`TTable` objects can share the same Context.
* Schema: The Schema defines the column names in the table and their data types, which, unlike in other Python packages, you must specify up-front. Each column can be either an integer column, a float column, or a string column. Each column can hold values of only that data type.

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

    	>>> context = snap.TTableContext()
    	>>> schema = snap.Schema()
    	>>> schema.Add(snap.TStrTAttrPr("StudentID", snap.atInt))
    	>>> schema.Add(snap.TStrTAttrPr("Midterm1", snap.atInt))
    	>>> schema.Add(snap.TStrTAttrPr("Midterm2", snap.atInt))
    	>>> schema.Add(snap.TStrTAttrPr("Final", snap.atInt))

As you can see, defining the Context simply requires initializing an object of type *TTableContext*. That’s all you have to do for the Context! There is one another important aspect of Context. Context should not be garbage collected by Python, which means that if it is defined within a function which returns TTable or Context, then the variable must be declared as global within the function:
    	>>>     global context

For the Schema, you must first initialize an object of the SNAP Schema type, and then use the :meth:`Add()` method to create column types for the :class:`TTable` you want to build.  The Add() method takes one parameter, a SNAP *TStrTAttrPr*, which is a pair consisting of a string and an attribute. An attribute in SNAP is used to represent different data types using an integer key; you don’t have to worry about this, but just remember that the Schema requires this data type for the columns. There are always 2 components of a *TStrTAttrPr*: the name of the column, which is a string, and the type of data that the column with that name will hold. The options are atInt (integer attribute), atFlt (float attribute), and atStr (string attribute). Since our columns are type integer, we will use atInt for all of them.

We now have the building blocks for a :class:`TTable` with four columns and a context! Next, we’ll show how to create a :class:`TTable` from these components, plus a path to a file that we want to make a :class:`TTable` from. :class:`TTable` objects can be created from comma-separated files (CSV) and tab-separated files (TSV). Here’s an example::

       >>> filename = "/path/to/student_grades.tsv"
       >>> grade_table = snap.TTable.LoadSS(schema, filename, context, "\t", snap.TBool(True))

For the filename, we simply use the path to that file on the local machine. Then, to create a table, we use the function :meth:`TTable.LoadSS()`. This function takes in 5 parameters:

* The Schema that we made before, which should correspond to the number and types of columns in the TSV file
* The name of the path to the file, as a string
* The Context created earlier
* The separator used in the file (“\t” for tab separated, “,” for comma separated, etc.)
* A *snap.TBool* boolean value indicating whether or not the file has a ‘title line,’ that is, a beginning line of column names or other text that is not commented out with a #. Remember that your Schema already has column names, so you don’t want to include them from your CSV or TSV since they’ll throw an error! In our example above, we did have column names in our TSV, so we set this boolean to True.

Now we’ve successfully created a :class:`TTable` in SNAP! Recall that you can accommodate any table by changing the Schema for the number and type of columns that you need. 

Saving and Loading a :class:`TTable` with Binary Format
=======================================================

Next, we’ll demonstrate how to save a :class:`TTable` and load one from binary. :class:`TTable` objects can be saved in binary format because this saves space (in fact, it’s orders of magnitude more efficient than saving it as text). To save a :class:`TTable` to binary format, you use the following:

	>>> outfile = "/path/to/grade_table.bin"
	>>> FOut = snap.TFOut(outfile)
	>>> table.Save(FOut)
	>>> FOut.Flush()

The four steps are:

* Create a path to the file you want to save your :class:`TTable` to.
* Create a TFOut object. A SNAP *TFout* object allows writing the contents of a file to the specified pathname.
* Save the table to your *TFOut* object (here, named FOut) using the :meth:`Save()` function.
* Flush your *TFOut* object. This flushes the write buffer for the stream, meaning that it has been cleared of the contents of our table and it can be used again for further saving operations.

Once we’ve saved a :class:`TTable` object to binary format, we can also load :class:`TTable` objects from their binary format as follows: 

	>>> context = snap.TTableContext()
	>>> outfile = "/path/to/grade_table.bin"
	>>> FIn = snap.TFIn(outfile)
	>>> table = snap.TTable.Load(FIn, context)

Again, the four steps of loading a :class:`TTable` from binary format are:

* Create a Context object for the :class:`TTable`. This is necessary when loading a :class:`TTable` that has been stored in binary format.
* Provide the pathname where the binary file currently resides.
* Create an *TFIn* object with the pathname to the binary file. The SNAP *FIn* object is used to read the contents of a binary file and parse it back into a more complex data structure. It takes the pathname as a parameter.
* Finally, create the :class:`TTable` using the :meth:`.Load()` method, which takes two parameters: the *TFIn* object we just made, and the context that was created in Step 1.

We’ve now covered the basics of how to create, save, and load :class:`TTable` objects!

Columnwise :class:`TTable` Operations
=====================================

Now that we know how to create a :class:`TTable`, let’s investigate different column operations that are supported by :class:`TTable` objects. These column operations allow us to take two or more columns and create a new column via some operation. These include addition, subtraction, multiplication, division, modulo division, maximum, minimum, and concatenation. They are united by their function names, which are all of the form *.ColFunc()*, where Func is the operation name. There is also one more advanced function, :meth:`AggregateCols()`, that allows us to do other operations like count, first, last, mean, and median.

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


Let’s say we wanted to know the total number of points that each student earned across the two midterms. To do this, we want to use the :meth:`ColAdd()` function, which looks like `table.ColAdd(Attr1, Attr2, NewColName`.

In the :meth:`ColAdd()` function, we provide three parameters: the first two are the columns we want to add together, using their string names, and the third is the name of the column we want to create that will hold the sums of the first two columns. This is true for all ColFunc() functions. Since we want to get the sum over the midterm scores, we will add together Midterm1 and Midterm2::

       >>> grade_table.ColAdd("Midterm1", "Midterm2", "MidScoreSum")

Which yields: 


.. table:: Student Grades
   :widths: 15 10 10 10 10

   ========== ========== ========== ========== ==========
   StudentID  Midterm1   Midterm2   Final      MidScoreSum
   ========== ========== ========== ========== ==========
   101        79         86         88         165
   102        84         80         79         164
   103        56         76         80         132
   104        90         92         96         182
   105        92         85         87         177
   106        87         95         92         182
   107        94         90         91         184
   108        76         88         81         164
   ========== ========== ========== ========== ==========

Let’s say now that we wanted a column that gave the average of the midterm scores. In this case, we’d use the :meth:`AggregateCols()` method to create a new column with the mean of the midterm columns, row by row. The :meth:`AggregateCols()` has parameters `table.AggregateCols(AggAttrs, AggOp, NewColName` where *AggAttrs* is the list of columns you’re working with (it can be more than two), and *AggOp* is the operation you want to perform from the options: aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, aaMedian. We’ll choose aaMean for our purposes here. Last, you’ll again provide the string name of the new column you’d like to create!

Here is the code for getting the mean over the midterm scores:: 

	>>> AggAttrs = snap.TStrV()
	>>> AggAttrs.Add("Midterm1")
	>>> AggAttrs.Add("Midterm2")
	>>> grade_table.AggregateCols(AggAttrs, snap.aaMean, "MidtermMean")

With the result:


.. table:: Student Grades
   :widths: 15 10 10 10	10 10

   ========== ========== ========== ========== =========== ==========
   StudentID  Midterm1   Midterm2   Final      MidScoreSum MidtermMean
   ========== ========== ========== ========== =========== ==========
   101        79         86         88         165         82.5
   102        84         80         79         164         82
   103        56         76         80         132         66
   104        90         92         96         182         91
   105        92         85         87         177         88.5
   106        87         95         92         182         91
   107        94         90         91         184         92
   108        76         88         81         164         82
   ========== ========== ========== ========== =========== ==========

A similar methodology can be used for all of the column operation functions for :class:`TTable` objects.

One important feature of this function group is: If the third parameter passed is an empty string, i.e.:: 

	>>> table.ColDiv("Col1", "Col2", "")

then the results will overwrite the values in the column of the first parameter. In this case, the results of dividing *Col1* values by *Col2* values would replace the values in Col1.

Rowwise Table Operations
========================

The operations shown above focused on creating new data from some combination of two pre-existing columns. Now, we’ll look at operations that summarize or elucidate information about the table: namely, the Group(), Aggregate(), AggregateCols(), Select(), and Unique() functions. These methods affect the table in different ways. Here, we will describe the use cases of the most important features. 

First, we will investigate the :meth:`Select()` function family, which consists of :meth:`SelectAtomicIntConst()`, :meth:`SelectAtomicFltConst()`, :meth:`SelectAtomicStrConst()`,  :meth:`SelectAtomic()`, and :meth:`Select()`. You will usually use the first four, as :meth:`Select()` is utilized for complex, layered selecting parameters.

First, let’s look at :meth:`SelectAtomic***Const()` functions, which allows you to select rows based on their value in a single column. For example, perhaps you want to select students who had final scores of 90 or above. Here are the general parameters of :meth:`SelectAtomic***Const()` (insert Int, Flt, or Str depending on the type): `table.SelectAtomicIntConst(Column, Val, Cmp, SelectedTable`.

*Column* is the column we want to select on. This would be final scores in the example above. *Val* is the value we want to compare to, which is 90 in the example above. *Cmp* is the comparator we want to use, with choices of less then (LT), less than or equal to (LTE), equal to (EQ), not equal to (NEQ), greater than or equal to (GTE), greater than (GT), substring of (SUBSTR), or superstring of (SUPERSTR). In the example above, we want to use greater than or equal to (GTE). Finally, we need to provide a *SelectedTable*, the table that we want add the selected rows to. Generally, using a new blank table is the right option.

Here’s the code to select only rows where the final score is greater than or equal to 90. Let’s assume we’ve greater a new blank :class:`TTable` called 'above_90_table'::

       	   >>> grade_table.SelectAtomicIntConst("Final", 90, snap.GTE, above_90_table)

Let’s now look at the :meth:`Group()` and :meth:`Unique()` functions. The :meth:`Group()` function allows us to create a new column to label each column according to shared attributes by using `Group(GroupByAttrs, GroupAttrName, Ordered=True`.
Let’s now look at the :meth:`Group()` and :meth:`Unique()` functions. The :meth:`Group()` function allows us to create a new column to label each column according to shared attributes by using `Group(GroupByAttrs, GroupAttrName, Ordered=True`.

Here, *GroupByAttrs* are the columns we want to group with respect to, where their values are the same. *GroupAttrName* will be the name of the new column with the labels. Let’s say we wanted to group students by their midterm mean score. As we can see above, two students scored an average 91, and two students scored an average 82, so we will see some groups developed. Let’s write the code for this operation:

	   >>> groupAttrs = snap.TStrV()
	   >>> groupAttrs.Add("MidtermMean")
	   >>> table.Group(groupAttrs, "MeanGroups", snap.TBool(True))

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

Another related method is :meth:`Unique()`. Rather than assigning the same labels to rows with similar values, any rows with the same sought-after values will be deleted so there are no remaining duplicates, using the paramaters :meth:`Unique(Attrs, Ordered=True)`.
Here, Attrs is simply the attributes that need to be equal in order for us to consider them duplicates. 

Let’s try this on the original table, and instead of grouping by the midterm mean, we’ll use :meth:`Unique()` to keep only students with a unique midterm mean score::

      	  >>> attrs = snap.TStrV()
	  >>> attrs.Add("MidtermMean", snap.TBool(True))
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

Now, let’s investigate the :meth:`Aggregate()` method, which allows us to aggregate statistics for each row based on values in certain columns. For example, we might want to add a column telling us how many instances of the AuthorID in each row exist in the dataset. :meth:`Aggregate()` is invoked using parameters `Aggregate(GroupByAttrs, AggOp, ValAttr, ResAttr, Ordered=True`.

The Aggregate method takes:

* *GroupByAttrs*: The attributes (columns) that you want to aggregate with respect to. This will need to be a vector of strings that you create in advance.
* *AggOp*: The operation you want to aggregate by: options are aaSum, aaCount, aaMin, aaMax, aaFirst, aaLast, aaMean, or aaMedian.
* *ValAttr*: Which attribute (column) we want to aggregate over.
* *ResAttr*: The name of the column where the result of the aggregation will be stored.
* *Ordered*: Whether to treat grouping keys as ordered or unordered.

To make all this more concrete, let’s say we wanted to find the maximum final score over all students based on a particular mean midterm score. That is, for students with the same midterm score, we will add a value to their row indicating the highest final score achieved by someone with their same score. Here’s how we would use Aggregate() to do so::

   	>>> GroupBy = snap.TStrV()
	>>> GroupBy.Add("MidtermMean")
	>>> PapAuthT.Aggregate(GroupBy, snap.aaMax, "Final", "MaxFinal", snap.TBool(False))

Here, we use a variable *GroupBy* to hold a vector of strings representing the columns we want to group with respect to, that is, the MidtermMean column. We then use :meth:`Aggregate()` with the snap.aaCount function to count the number of times each mean appears in the dataset, and store the count in a new column called MeanCount. Here is what the result will look like:

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

* :meth:`Intersection()`: creates a new table from all rows that appear in both original tables. Returns a new table.
* :meth:`Union()`: creates a new table from all rows that appear in either original table. Returns a new table. *UnionAll* has a similar function, but retains duplicates of rows across the tables.
* :meth:`Minus()`: creates a new table from all rows in the first table not present in the second table. Returns a new table.
* :meth:`Join()`: a more customizable function, Join equi-joins two tables based on one attribute in the first table. Columns from the second table will be added to the first where the value of the desired attribute in the first table matches the value of the desired attribute in the second. Does not return a new table, but rather updates the original table with columns from the second table.
* :meth:`SimJoin()`: a function that performs an equi-join if the distance between two rows is less than the specified threshold.

Let’s go back to our original grade table with four columns: StudentID, Midterm1, Midterm2, and Final. Let’s say we have another table that lists the student IDs of these students, plus a column with their names:

.. table:: Student Names
   :widths: 15 40

   ========= ==========
   ID        Name
   ========= ==========
   101       Will
   102       Amira
   103       Todd
   104       Yang
   105       Cathy
   106       Shubash
   107       Nicolo
   108       Maria
   ========= ==========

Let’s say we want to incorporate the Name column into our original table. We can do this using the :meth:`Join()` function, with parameters `Join(Attr1, PTable, Attr2`.

Here, *Attr1* is the column we want to join on from the first table, *PTable* is the second table we want to join with, and *Attr2* is the column we want to join on from the second table.

To combine our two tables, we would use:: 

   	   >>> combined_table = grade_table.Join("StudentID", name_table, "ID")

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
   105        92         85         87         Cathy
   106        87         95         92         Shubash
   107        94         90         91         Nicolo
   108        76         88         81         Maria
   ========== ========== ========== ========== ==========

Getting Information from Tables
===============================

SNAP has many functions to get information from :class:`TTable` objects, in the form of vectors or basic data types. Some of the most useful get functions include:

* :meth:`GetNumRows()`
* :meth:`GetSchema()`
* :meth:`GetIntVal()`, :meth:`GetFltVal()`, and :meth:`GetStrVal()`
* :meth:`GetIntValAtRowIdx()`, :meth:`GetFltValAtRowIdx()`, and :meth:`GetStrValAtRowIdx()`
* :meth:`ReadIntCol()`, :meth:`ReadFltCol()`, and :meth:`ReadStrCol()`

These functions are relatively straightforward, and will assist with obtaining pieces of information and summary statistics from the :class:`TTable`. The *Val* functions return single values, and the *Col* functions return vectors of entire column values.

