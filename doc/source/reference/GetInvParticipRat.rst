GetInvParticipRat
'''''''''''''''''

.. function:: GetInvParticipRat(Graph, MaxEigVecs, TimeLimit, EigValIprV)

Computes Inverse participation ratio of a given graph. See Spectra of
"real-world" graphs: Beyond the semicircle law by Farkas, Derenyi, Barabasi
and Vicsek  URL: http://arxiv.org/abs/cond-mat/0102335

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *EigVecs*: int (input)
    Maximum number of eigenvectors to return

- *TimeLimit*: int (input)
    Maximum number seconds to search

- *EigValIprV*: TFltPrV, a vector of (float, float) pairs (output)
    The output inverse participation ratios
    
Return value:

- None

The following example computes the inverse participation ratio for :class:`TNGraph`::

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

