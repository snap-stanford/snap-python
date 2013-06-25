import sys
from socket import gethostname

sys.path.append("../swig-r")
import snap

def main():
  
  # Run TNEAGraph demo
  snap.DefaultConstructor()
  
  snap.ManipulateNodesEdges()
  
  snap.ManipulateNodeEdgeAttributes()

if __name__ == "__main__":
  main()
