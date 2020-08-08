GetInvParticipRat (SWIG)
''''''''''''''''''''''''

.. function:: GetInvParticipRat(Graph, MaxEigVecs, TimeLimit, EigValIprV)

Computes Inverse participation ratio of a given graph.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EigVecs*: int (input)
    Maximum number of eigenvectors to return.

- *TimeLimit*: int (input)
    Maximum number seconds to search.

- *EigValIprV*: :class:`TFltPrV`, a vector of (float, float) pairs (output)
    The output inverse participation ratios.
    
Return value:

- None

See Spectra of "real-world" graphs: Beyond the semicircle law by Farkas, Derenyi, Barabasi and Vicsek  URL: http://arxiv.org/abs/cond-mat/0102335


The following example computes the inverse participation ratio for :class:`TNGraph`::

 import snap
 
 UGraph = snap.TUNGraph.New()
 UGraph.AddNode(1)
 UGraph.AddNode(2)
 UGraph.AddNode(3)
 UGraph.AddNode(4)
 UGraph.AddNode(5)
 UGraph.AddNode(6)
 UGraph.AddEdge(1, 2)
 UGraph.AddEdge(2, 3)
 UGraph.AddEdge(3, 5)
 UGraph.AddEdge(4, 6)
 UGraph.AddEdge(4, 1)

 EigValIprV = snap.TFltPrV()
 snap.GetInvParticipRat(UGraph, 20, 1000, EigValIprV)
 for item in EigValIprV:
     print('%f, %f' % (item.GetVal1(), item.GetVal2()))

