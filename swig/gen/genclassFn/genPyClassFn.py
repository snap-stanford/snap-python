# This script generates wrappers to enable Python class functions
# Command line input: file name containing the list of class functions to be added, one per line

import sys

graphTypes = ['PUNGraph', 'PNGraph', 'PNEANet']
with open(sys.argv[1], 'r') as f:
    for line in f:
        funcName = line.strip()
        print ("def " + funcName + "_classFn" + "(self, *args):")
        print ("\t" + "return " + funcName + "(self, *args)")
        for graphType in graphTypes:
            print (graphType + "." + funcName + " = " + funcName + "_classFn")
        print()
