import sys
from socket import gethostname

sys.path.append("../swig")
import snap as Snap

def main():
  
  # Run TNEAGraph demo
  Snap.DefaultConstructor()
  
  Snap.ManipulateNodesEdges()
  
  Snap.ManipulateNodeEdgeAttributes()

if __name__ == "__main__":
  main()