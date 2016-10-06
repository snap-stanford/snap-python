import os
import sys

import snap

filename = "example.paj"

output = open(filename, "w")
output.write("""*Vertices      9
   1 "1"    0.3034    0.7561
   2 "2"    0.4565    0.6039
   3 "3"    0.4887    0.8188
*Arcs
    1      2       1
    1      3       1
    2      3       1
""")
output.close()

print "Directed graph"
Graph = snap.LoadPajek(snap.PNGraph, filename)

print "Nodes", Graph.GetNodes()
if Graph.GetNodes() != 3:
    print "*** Error11"
for NI in Graph.Nodes():
    print "Node", NI.GetId()

print "Edges", Graph.GetEdges()
if Graph.GetEdges() != 3:
    print "*** Error12"
for EI in Graph.Edges():
    print "Edge", EI.GetSrcNId(), EI.GetDstNId()

print "Undirected graph"
UGraph = snap.LoadPajek(snap.PUNGraph, filename)

print "Nodes", UGraph.GetNodes()
if UGraph.GetNodes() != 3:
    print "*** Error21"
for NI in UGraph.Nodes():
    print "Node", NI.GetId()

print "Edges", UGraph.GetEdges()
if UGraph.GetEdges() != 3:
    print "*** Error22"
for EI in UGraph.Edges():
    print "Edge", EI.GetSrcNId(), EI.GetDstNId()

print "Directed multigraph"
Network = snap.LoadPajek(snap.PNEANet, filename)

print "Nodes", Network.GetNodes()
if Network.GetNodes() != 3:
    print "*** Error31"
for NI in Network.Nodes():
    print "Node", NI.GetId()

print "Edges", Network.GetEdges()
if Network.GetEdges() != 3:
    print "*** Error32"
for EI in Network.Edges():
    print "Edge", EI.GetSrcNId(), EI.GetDstNId()

os.remove(filename)

