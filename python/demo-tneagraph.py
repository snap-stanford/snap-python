import os.path
import sys
import argparse
import random
from socket import gethostname


sys.path.append("../swig")
import snap as Snap

def main():

  # Run TNEAGraph demo
  Snap.DefaultConstructor()
  
  Snap.ManipulateNodesEdges()


if __name__ == "__main__":
  main()


