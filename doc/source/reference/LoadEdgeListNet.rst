LoadEdgeListNet
'''''''''''''''

.. function:: LoadEdgeListNet(InFNm, Separator)

Loads a graph of type `TNEANet` from a text file *InFNm*, which contains nodes and edges, along with their attributes.

*InFNm* is a whitespace separated file of several columns: 

 The file consists of columns separated by *Separator*. There should be a node section, which begins with a schema line, and ends with the (optional) sentinel. The node schema line should begin with the term '#NODES', followed by a list of attribute names and type. The keyword 'NId' should be used to designate the column containing the node ids. The schema would look like: #NODES ... NId ... <attribute_1>:<type_1> ..., where the ... represents the *Separator*. Types should be either 'Int', 'Flt', or 'Str'. If a node has no value for a given attribute, the term '__null__' should be used instead. The sentinel term should follow, on a separate line, after all nodes and their attributes have been specified. The sentinel is '#END'. 

 The edge section is similar to the nodes section, begining with a schema line and ending with an optional sentinel, '#END'. The edge schema line begins with '#EDGES', followed by a list of attribute names and types. The keywords 'SrcNId' and 'DstNId' should be used to designate the columns containing the source and destination node ids for the given edge. An example schema would look like: #EDGES ... SrcNId ... DstNId ... <attribute_1>:<type_1> .... Like with nodes, if an edge does not have a value for a given attribute, use the term '__null__' instead.

Parameters:

- *InFNm*: string (input)
    Filename with the description of the graph edges.

- *Separator*: char (input)
    Column separator.

Return value:

- graph
    A Snap.py network represented by the *InFNm*.


The following example shows how to load a small file representing a graph::

    import snap

    Graph = snap.LoadEdgeList("toy_graph", '\t')


An example file is given below (toy_graph) ::

    #NODES  NId Attr1:Int   Attr2:Str   Attr3:Flt
    0   1   '1'    1.0
    1   2   '2' 2.0
    2   __null__   '3' 3.0
    3   4   '4' __null__
    4   5   __null__ 5.0
    #END
    #EDGES  SrcNId  DstNId  Attr4:Flt
    0   1   3.0
    1   2   4.0
    2   3   5.0
    3   4   6.0
    4   0   7.0



