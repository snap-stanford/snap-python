GetTreeSig
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetTreeSig (Graph, RootNId, Sig, NodeMap)

.. note::

    This function is not yet supported.

Returns the tree signature of the graph, for each level we sort the node in-degrees and concatenate them into a vector.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *RootNId*: int (input)
    Root of the tree

- *Sig*: a vector of ints (output)
    The tree signature

- *NodeMap*: a vector of pairs of ints (output)
    The mapping of nodes in-degrees as a vector

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Tree_%28graph_theory%29

The following example shows how to compute the tree signature for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Sig = snap.TIntV()
    NodeMap = snap.TIntPrV()
    for NI in Graph.Nodes():
      # Without if statement, we receive "error *** Error: Execution stopped: Node.GetInDeg()==0 || Node.GetOutDeg()==0, file /home/rok/include/snap/alg.h, line 513" (see source here: https://github.com/snap-stanford/snap/blob/master/snap-core/alg.h)
      # With if statement, no tree signatures are computed
      #if (NI.GetInDeg() == 0 or NI.GetOutDeg() == 0):
      snap.GetTreeSig(Graph, NI.GetId(), Sig, NodeMap)
      for item in Sig:
        print(item)
      for item in NodeMap:
        print(item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Sig = snap.TIntV()
    NodeMap = snap.TIntPrV()
    for NI in Graph.Nodes():
      # Without if statement, we receive "error *** Error: Execution stopped: Node.GetInDeg()==0 || Node.GetOutDeg()==0, file /home/rok/include/snap/alg.h, line 513" (see source here: https://github.com/snap-stanford/snap/blob/master/snap-core/alg.h)
      # With if statement, no tree signatures are computed
      #if (NI.GetInDeg() == 0 or NI.GetOutDeg() == 0):
      snap.GetTreeSig(Graph, NI.GetId(), Sig, NodeMap)
      for item in Sig:
        print(item)
      for item in NodeMap:
        print(item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Sig = snap.TIntV()
    NodeMap = snap.TIntPrV()
    for NI in Graph.Nodes():
      # Without if statement, we receive "error *** Error: Execution stopped: Node.GetInDeg()==0 || Node.GetOutDeg()==0, file /home/rok/include/snap/alg.h, line 513" (see source here: https://github.com/snap-stanford/snap/blob/master/snap-core/alg.h)
      # With if statement, no tree signatures are computed
      #if (NI.GetInDeg() == 0 or NI.GetOutDeg() == 0):
      snap.GetTreeSig(Graph, NI.GetId(), Sig, NodeMap)
      for item in Sig:
        print(item)
      for item in NodeMap:
        print(item.GetVal1(), item.GetVal2())

