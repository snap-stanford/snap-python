GenRewire
'''''''''''

.. function:: GenRewire (Graph, NSwitch=100, Rnd)

Rewires a *graph* by randomly rewiring its edges while keeping the degrees the same.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph

- *NSwitch*: 

- *Rnd*: seed for randomization


Return value:

- PUNGraph 

The following example shows how to use this function for nodes in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    GenRewire(Graph, 100, <TRnd>)
