Tables (SWIG)
`````````````

Tables in SNAP are represented by the class :class:`TTable`.

:class:`TTable` is designed to provide fast performance at scale, and to effortlessly handle datasets containing hundreds of millions of rows. They can be saved and loaded to disk in a binary format using the provided methods; loading from and saving to binary is orders of magnitude faster than using a text representation of the table.

A :class:`TTable` can store integers, floats and strings in its entries. For performance reasons, strings are mapped to a unique integer, and the :class:`TTable` stores only the integer which maps to the string. Each :class:`TTable` object has an associated :class:`TTableContext` which stores the mapping from integers to strings and back, and can be used when the string corresponding to an integer needs to be retrieved. (Note: many :class:`TTable` objects can share the same context; this is often useful, for example, to ensure that equivalent strings in different tables are treated as equivalent in SNAP.)

A :class:`TTable` object consists of multiple columns, each column being an integer, string or float. This is defined by the table's Schema. A schema is simply a vector of pairs of TStr and TAttrType. (Note: TAttrType represents the type of the column. Currently supported values are snap.atInt, snap.atFlt and snap.atStr.) Each entry in the schema has the name of the column, and the attribute type.

After the schema and the colums are defined, the data can be stored in rows, with each row containing an entry for each column. It is possible to iterate over the data by row, using the :class:`TRowIterator` class (see documentation below for details).

:class:`TTable` also provides functionality for doing joins (using the :meth:`Join` method), groupings (using the :meth:`Aggregate` method), selection and projection (using the :meth:`Select` and :meth:`Project` methods), as well as sorting (using the :meth:`Order` method).

In order to quickly retrieve elements by value, :class:`TTable` allows the user to construct indexes on a column (using :meth:`RequestIndexInt`, :meth:`RequestIndexFlt` and :meth:`RequestIndexStrMap`. Note that unless these functions are explicitly called, the default is to not create any indexes.)

:class:`TTable` can be loaded from a text-file in spreadsheet (tab-separated or comma-separated) format using the static :meth:`LoadSS` method.

Tables can be converted to SNAP graph classes using the provided :func:`ToNetwork` functions.

The tutorial provides extensive documentation on the use of table methods and functions in the section about :doc:`../tutorial/table-tut`. The code snippets below additionally highlight some of the common operations using :class:`TTable` objects. The reference descriptions of methods and functions used are documented in more detail below.

The following code snippet shows how to load a :class:`TTable` object from a tab-separated file containing one integer, one float and two string columns, and then save the object to disk in binary format::

    import snap

    context = snap.TTableContext()
    filename = "/path/to/input.tsv"

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("Col1", snap.atInt))
    schema.Add(snap.TStrTAttrPr("Col2", snap.atFlt))
    schema.Add(snap.TStrTAttrPr("Col3", snap.atStr))
    schema.Add(snap.TStrTAttrPr("Col4", snap.atStr))

    table = snap.TTable.LoadSS(schema, filename, context, "\t", snap.TBool(False))

    outfile = "/path/to/output.bin"
    FOut = snap.TFOut(outfile)
    table.Save(FOut)
    FOut.Flush()

The saved table can now be loaded from binary using::

    import snap
    context = snap.TTableContext()

    outfile = "/path/to/output.bin"
    FIn = snap.TFIn(outfile)
    table = snap.TTable.Load(FIn, context)

Note that loading and saving from binary is over ten times faster than loading the raw text file.

Next, we present a slightly more involved example. Let's say we have an authorship table for academic papers, *PapAuthT* where each row has a PaperID and an AuthorID. (Thus, if paper P1 was written by A1, A2 and A3, and paper P2 by authors A2, we would have four rows in our :class:`TTable`, with data (P1, A1), (P1, A2) and (P1, A3), and (P2, A2).) Further, let's say we have the citation count of each paper in a separate table, *PapCitT*, which has columns PaperID and CitCount. Assuming that these tables have already been loaded into :class:`TTable` objects with appropriate schema, the following code shows how to perform various useful operations on these tables::

    # Assuming that PapAuthT and PapCitT are already loaded into TTable objects with columns as described above.

    # First, let's say we want to count the number of papers written by an author. We use Aggregate
    # with the operation, snap.aaCount.

    # This counts the number of elements with a particular value of the attributes in GroupBy
    # (namely, AuthorID), and puts the count in a new column called "CountAuthPapers".
    # Note that for the aggregation operation snap.aaCount, the third argument is irrelevant.
    GroupBy = snap.TStrV()
    GroupBy.Add("AuthorID")
    PapAuthT.Aggregate(GroupBy, snap.aaCount, "AuthorID", "CountAuthPapers", snap.TBool(False))

    # To keep only one row for each author, we can use the TTable.Unique() method as PapAuthT.Unique("AuthorID")
    # which will remove all rows with duplicate values of AuthorID.

    # Next, let's say we want to compute the total number of citations each author has.
    # This is the sum of the citations of all the papers the author wrote.
    # However, the citation info is in PapCitT. Hence, we must join it to this table now.

    # Joins these two tables, merging rows which have the same PaperID in both.
    # Now, each row has a PaperID, AuthorID and a CitCount
    PapAuthCitJoinT = PapAuthT.Join("PaperID", PapCitT, "PaperID")

    # We now aggregate the citation counts by author, summing them all up to get the
    # total number of citations.
    GroupBy = snap.TStrV()
    GroupBy.Add("AuthorID")
    PapAuthCitJoinT.Aggregate(GroupBy, snap.aaSum, "CitCount", "TotalAuthCits", snap.TBool(False))

    # Now, we have the total number of citations by each author in a new column
    # TotalAuthCits. We can now keep just the relevant columns, and drop duplicate rows
    # with the same author ID.

    ProjectCols = snap.TStrV()
    ProjectCols.Add("AuthorID")
    ProjectCols.Add("TotalAuthCits")
    AuthCitT = PapAuthCitJoinT.Project(ProjectCols)
    AuthCitT.Unique("AuthorID")

    # We can also sort the authors in decreasing order of total citations.
    OrderBy = snap.TStrV() # The TTable.Order method sorts using the values of
                           # the columns in OrderBy, in lexicographic order.
    OrderBy.Add("TotalAuthCits")
    AuthCitT.Order(OrderBy, "", snap.TBool(False), snap.TBool(False))

TTable
======

.. class:: TTable()
           TTable(Context)
           TTable(S, Context)
           TTable(SIn, Context)
           TTable(H, Col1, Col2, Context, IsStrKeys=False)
           TTable(Table, const TIntV& RowIds)
           TTable(Table)
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

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
   :noindex:

   Returns a new iterator over vector of :class:`PTable`. Normally, these objects are
   not created directly, but obtained via a call to the table class :class:`TTable` 
   method, such as :meth:`GetMapPageRank()`, that returns a node iterator.

   Below is a list of functions supported by the :class:`TTable` class:

      .. describe:: Next()

         Returns next table in the sequence and update iterator.

      .. describe:: HasNext()

         Checks if iterator has reached end of the sequence.
