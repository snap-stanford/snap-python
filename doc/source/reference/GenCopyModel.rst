GenCopyModel
''''''''''''

.. function:: GenCopyModel (Nodes, Beta, Rnd=TInt::Rnd)

Generates a random scale-free network using the Copying Model. The generating 
process operates as follows: Node u is added to a graph, it selects a random 
node v, and with probability Beta it links to v, with 1-Beta links u links to 
neighbor of v. 

Parameters:

- *Nodes*: int (input)
    Number of nodes

- *Beta*: double (input)
    Probability used in the generating process

- *Rnd*: TRnd (input)
    Random number generator

Return value:

- PNGraph

For more info see http://snap.stanford.edu/class/cs224w-readings/kumar00stochastic.pdf

The following example shows how to generate a network using GenCopyModel::

    import snap

    result = snap.GenCopyModel(20, 0.4, snap.TRnd())
    print "resulting graph: Nodes %d, Edges %d" % (result.GetNodes(), result.GetEdges())
