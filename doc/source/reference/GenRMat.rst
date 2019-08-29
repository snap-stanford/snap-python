GenRMat
'''''''

.. function:: GenRMat(Nodes, Edges, A, B, C, Rnd=TRnd)

Generates an R-MAT directed graph using recursive descent into a 2x2 matrix [A,B; C, 1-(A+B+C)].

Parameters:

- *Nodes*: int (input)
    The number of nodes used to generate the graph.

- *Edges*: int (input)
    The number of edges used to generate the graph.

- *A*: float (input)
    Probability of an edge falling into the A partition in the R-MAT model.

- *B*: float (input)
    Probability of an edge falling into the B partition in the R-MAT model.

- *C*: float (input)
    Probability of an edge falling into the C partition in the R-MAT model.

- *Rnd*: :class:`TRnd` (input)
    Random number generator .

Return value:

- directed graph
    A Snap.py directed R-MAT graph.

For more info see: "R-MAT Generator: A Recursive Model for Graph Mining." D. Chakrabarti, Y. Zhan and C. Faloutsos, in SIAM Data Mining 2004. URL: http://www.cs.cmu.edu/~deepay/mywww/papers/siam04.pdf


The following example shows how to generate an R-MAT graph::

    import snap

    Rnd = snap.TRnd()
    Graph = snap.GenRMat(1000, 2000, .6, .1, .15, Rnd)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
