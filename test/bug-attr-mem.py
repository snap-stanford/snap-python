#!/usr/bin/python

#
#   the memory keeps growing while traversing the graph
#   find out why this is happening
#

import os, sys
sys.path.append('/home/user/snap-python/swig')
import snap as sn
import numpy as np
import memory_profiler
import gc

def writeLoop(graph):
    nID = graph.BegNI()
    while nID < graph.EndNI():
        #write attribute            
        graph.AddFltAttrDatN(nID,np.random.random(1),'attr')
        nID.Next()
    return graph
            
def readLoop(graph):
    NI = graph.BegNAFltI('attr')
    while NI < graph.EndNAFltI('attr'):
        NI.GetDat()
        NI.Next()       
    return graph
   
@profile
def repeatChangeAttr(graph):
    for i in range(1,10):
        writeLoop(graph)
        #graph = writeLoop(graph)
    for i in range(1,10):
        readLoop(graph)
        #graph = readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)
    readLoop(graph)

graph = sn.TNEANet()
#graph.AddFltAttrN("attr", 1.)
for i in range(1000):
    graph.AddNode(i)
repeatChangeAttr(graph)

