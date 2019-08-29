GetTreeSig
''''''''''

.. note::

    This page is a draft and under revision.

.. function:: GetTreeSig(Graph, RootNId, Sig)

.. note::

    This function is not yet supported.

Fills Sig, a TIntV object, with the tree signature of the input graph starting at node RootNId. The tree signature is the id of the nodes in descending level sorted within each level.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *RootNId*: int (input)
    Id of the starting node

- *Sig*: TIntV (input)
    A vector of integers that holds the signature.

GetTreeSig currently has a bug. The following code shows an example of the bug. When executed, the program runs out of memory and causes an error.::

    import snap

    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(2)
    G1.AddEdge(1,2)
    v1 = snap.TIntV()
    snap.GetTreeSig(G1, 1, v1)

    for item in v1:
        print(item)

