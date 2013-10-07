GenRMatEpinions
'''''''''''

.. function:: GenRMatEpinions()

Generates a R-Mat graph, with a synthetic copy of the Epinions social network.

Parameters:

- None

Return value:

- *Graph*: graph
    A Snap.py directed graph which is a synthetic copy of the Epinions social network.

R-Mat generator with parameters set so that it generates a synthetic copy of the Epinions social network. The original Epinions social network can be downloaded at http://snap.stanford.edu/data/soc-Epinions1.html . This function is equivalent to GenRMat(75888, 508837, 0.550, 0.228, 0.212).

The following example shows how to generate a synthetic R-Mat with the same parameters as the Epinions social network::

    import snap

    Graph = snap.GenRMatEpinions()

