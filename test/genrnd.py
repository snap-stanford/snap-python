import random
import sys

sys.path.append("../swig")

import snap as Snap

def GenRndGnm():
    Graph = Snap.GenRndGnm_PNGraph(1000,10000)
    print("Graph", str(type(Graph)), Graph.GetNodes(), Graph.GetEdges())

    # save the graph
    FName = "test2.graph"
    print("Save", FName)

    FOut = Snap.TFOut(Snap.TStr(FName))
    Graph.Save(FOut)
    FOut.Flush()

    # load the graph
    print("Read", FName)
    FIn = Snap.TFIn(Snap.TStr(FName))
    #Graph2 = Snap.TNGraph(FIn)
    #Graph2 = Snap.TNGraph.Load(FIn)
    Graph2 = Snap.PNGraph.New()
    print("Graph2", str(type(Graph2)))
    print(str(dir(Graph2)))
    Graph2.Load(FIn)
    #Graph2 = Snap.Load_PNGraph(FIn)
    #print("Read end", FName)
    #print("Graph2", str(type(Graph2)), Graph2.GetNodes(), Graph2.GetEdges())

if __name__ == '__main__':
    print("----- GenRndGnm -----")
    GenRndGnm()

