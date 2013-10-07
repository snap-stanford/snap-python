GenConfModel
'''''''''''''''

.. function:: GenConfModel(DegSeqV, Rnd)

Generates a random undirect graph with a given degree sequence.

Generates a random undirect graph with a given degree sequence DegSeqV. Configuration model operates as follows. For each node N, of degree DeqSeqV[N] we create DeqSeqV[N] spokes (half-edges). We then pick two spokes at random, and connect the spokes endpoints. We continue this process until no spokes are left. Generally this generates a multigraph (i.e., spokes out of same nodes can be chosen multiple times).We ignore (discard) self-loops and multiple edges. Thus, the generated graph will only approximate follow the given degree sequence. The method is very fast!

Parameters:

- *DegSeqV*: vector of ints of type TIntV (input)
	The degree sequence vector.

- *Rnd*: a TRand type
	Random number generator.

Return value:

- Random undirect graph with degree sequence given by DegSeqV.

The following example generates a random unidirect graph with degree sequence 1, 2, 3. 

from snap import *

DegSeqV = TIntV()
DegSeqV.Add(1)
DegSeqV.Add(2)
DegSeqV.Add(3)
Rnd = TRnd()

GenConfModel(DegSeqV, Rnd)
