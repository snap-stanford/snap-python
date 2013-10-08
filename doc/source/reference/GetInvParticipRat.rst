GetInvParticipRat
'''''''''''''''''

.. function:: GetInvParticipRat(Graph, MaxEigVecs, TimeLimit, EigValIprV)

Computes Inverse participation ratio of a given graph. See Spectra of
"real-world" graphs: Beyond the semicircle law by Farkas, Derenyi, Barabasi
and Vicsek [#]_.

.. [#] http://arxiv.org/abs/cond-mat/0102335

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *EigVecs*: integer (input)
    Maximum number of eigenvectors to return

- *TimeLimit*: integer (input)
    Maximum number seconds to search

- *EigValIprV*: vector of float pairs (output)
    The output inverse participation ratios

- *EigVecV*: vector of vector of floats (output)
    The top eigenvectors
    
Return value:

- None

The following example computes the top eigenvectors and prints them::

 import snap
 Graph = snap.TUNGraph.New()
 Graph.AddNode(1)
 Graph.AddNode(2)
 Graph.AddNode(3)
 Graph.AddNode(4)
 Graph.AddNode(5)
 Graph.AddNode(6)
 Graph.AddEdge(1, 2)
 Graph.AddEdge(2, 3)
 Graph.AddEdge(3, 5)
 Graph.AddEdge(4, 6)
 Graph.AddEdge(4, 1)

 EigValIprV = snap.TFltPrV()
 snap.GetInvParticipRat(Graph, 20, 1000, EigValIprV)
 for x in EigValIprV:
    print '%f, %f' % (x.GetVal1(), x.GetVal2())

