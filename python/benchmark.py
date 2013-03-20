import os.path
import sys
import argparse
import random
from socket import gethostname

from datetime import datetime

sys.path.append("../swig")
import snap as Snap
from math import log

NUM_ITERATIONS = 1
PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Random, Small World, Pref, R-MAT
#GRAPH_TYPES = ['rmat', 'rnd_ngraph','rnd_ungraph', 'pref', 'sw']
GRAPH_TYPES = ['rnd_ungraph', 'rnd_ngraph', 'rmat', 'pref', 'sw']

# Average is 1, non-average is 0.
DEGREE_TYPES = [0, 1]
AVG_DEG = 3
AVG_DEGREE_RANGE = range(2, 10)
SW_REWIRE_PROB = 0.1

# Exponent range (e.g. 10^x to 10^y)
DEFAULT_RANGE = '5-7'

# Hostname for results
HOSTNAME = gethostname()

RESULTS_DIR = 'results'
RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%m'))

def benchmark_ngraph(results, Graph):
  '''
  Perform benchmark tests for Directed Graphs
  '''
    
  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0, 11):
    num = Snap.NodesGTEDegree_PNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg

  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PNGraph(Graph)

  num = Snap.NodesGTEDegree_PNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  
  results['max_wcc_percent'] = Snap.MxWccSz_PNGraph(Graph) \
    / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PNGraph(Graph).GetNodes() \
    / results['num_nodes']

  return results

def benchmark_ungraph(results, Graph):
  '''
  Perform benchmark tests for Undirected Graphs
  '''

  results['num_nodes'] = Graph.GetNodes()
  results['num_edges'] = Graph.GetEdges()
  
  for degree in range(0,11):
    num = Snap.NodesGTEDegree_PUNGraph(Graph, degree)
    percent_deg = float(num) / results['num_nodes']
    results['deg_gte_%d' % degree] = num
    results['deg_gte_%d_percent' % degree] = percent_deg
  
  # Check for over-weighted nodes
  results['max_degree'] = Snap.MxDegree_PUNGraph(Graph)
  
  num = Snap.NodesGTEDegree_PUNGraph(Graph, results['max_degree'])
  results['max_degree_num'] = num
  results['max_wcc_percent'] = Snap.MxWccSz_PUNGraph(Graph) \
                                / results['num_nodes']
  results['max_scc_percent'] = Snap.MxSccSz_PUNGraph(Graph).GetNodes() \
                                / results['num_nodes']

  # Calculate graph skew

  return results

def generate_graph(NNodes, NEdges, Model, Type):
  
  if verbose:
    print "Generating '%s' '%s' graph with %e nodes, %e edges" % \
          (Model, Type, NNodes, NEdges)

  if Model == 'rnd_ungraph':
    # GnRndGnm returns error, so manually generate
    Graph = Snap.GenRndGnm_PUNGraph(NNodes, NEdges, 0)

  elif Model == 'rnd_ngraph':
    Graph = Snap.GenRndGnm_PNGraph(NNodes, NEdges, 1)

  elif Model == 'rmat':
    Graph = Snap.GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2)

  elif Model == 'sw':
    Graph = Snap.GenSmallWorld(NNodes, NNodes/NEdges, 0.1)
  
  elif Model == 'pref':
    Graph = Snap.GenPrefAttach(NNodes, NNodes/NEdges)
        
  return Graph

def run_tests(num_iterations=3, min_nodes_exponent=3, max_nodes_exponent=4):
  '''
  Performtests with specificed exponent range
  '''

  all_results = []
  
  if verbose:
    print "Running results from %e to %e" % (min_nodes_exponent,
                                           max_nodes_exponent)
  
  for n in range(num_iterations):
    if verbose:
      print "Iteration: %d of %d" % (n+1, num_iterations)
  
    for exp in range(min_nodes_exponent,max_nodes_exponent+1):
      
      for g in GRAPH_TYPES:
        
        # Random number of nodes of degree i
        NNodes = 10**exp;
        
        for avg_deg in [10, 100]:
          
          NEdges = NNodes*avg_deg
          
          if NEdges > NNodes ** 2:
            print "Unable to assign %d edges to graph with %d nnodes" % \
                  (NEdges, NNodes)
            continue
          
          # Use SNAP to read from file FIn and FOut don't work
          Graph = None
                    
          results = {}
          
          if g in ['rmat', 'rnd_ngraph']:
            Type = "directed"
      
          elif g in ['sw', 'pref', 'rnd_ungraph']:
            Type = "undirected"
        
          else:
            print "Unknown graph type: %s" % g
          
          StartTime = datetime.now()
        
          FName = os.path.join(RESULTS_DIR, "%s_%de%d_deg%d_%d.graph" %
                               (g, NNodes, exp, NEdges/NNodes, n))
        
          if not generate:
            
            if os.path.exists(FName):
              try:
              
                print "Loading '%s' from ...'%s'" % (g, FName)
                FIn = Snap.TFIn(Snap.TStr(FName))
                if Type == "directed":
                  Graph = Snap.TNGraph(FIn)
                else:
                  Graph = Snap.TUNGraph(FIn)
  
              except Exception, e:
                print "Unable to load graph file, '%s': %s" % (FName, str(e))

        
            else:
              print "File not found: %s" % FName

            
          if not Graph:
            
            # User wants to re-generate graph, or no graph data available.
            Graph = generate_graph(NNodes, NEdges, g, Type)
            
            # Save the graph
            print "Saving '%s' graph to file ... '%s'" % (g, FName)

            if Graph:
#              try:
                FOut = Snap.TFOut(Snap.TStr(FName))
                Graph.Save(FOut)
                FOut.Flush()

            
#              except Exception, e:
#                print "Unable to save graph file, '%s': %s" % (FName, str(e))


          TimeGenerate = datetime.now() - StartTime

          print "Running tests..."
          StartTime = datetime.now()

          if Type == 'directed':
            results = benchmark_ngraph(results, Graph)
          if Type == 'undirected':
            results = benchmark_ungraph(results, Graph)

          TimeElapsed = datetime.now() - StartTime
          
          print "Elapsed Time = %.4f sec" % TimeElapsed.total_seconds()

          row_header = ["Hostname", "Model", "Type", "Nodes", "Edges",
                        "StartTime", "Generation Time", "Run Time"]

          print "Header: %s" % " ".join(row_header)

          import csv
          with open(RESULTS_FILE, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            print "Writing to '%s'..." % RESULTS_FILE
            row = [HOSTNAME, g, Type, NNodes, NEdges,
                   StartTime.strftime("%d/%b/%Y:%H:%M:%S"),
                   TimeGenerate.total_seconds(), TimeElapsed.total_seconds()]
            print "Time Data: %s" % repr(row)
            writer.writerow(row)
              
          print "-"*75

def main():
  
  global results_dir, verbose, generate, hostname, max_nodes_exponent
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")
  parser.add_argument("-r", "--range", default=DEFAULT_RANGE,
                      help="range (4-5) (10^4 to 10^5")
  parser.add_argument("-n", "--num_iterations", type=int,
                      default=NUM_ITERATIONS, help="number of iterations")
  
  parser.add_argument("-g", "--generate", default=False,
                      action="store_true", dest="generate", help="generate new graphs")
  
  args = parser.parse_args()
  
  verbose = args.verbose
  generate = args.generate
  
  print "Hostname: %s" % HOSTNAME
  print "Range = 10^%s to 10^%s" % (args.range[0], args.range[-1])
  
  if not os.path.exists(RESULTS_DIR):
    print "Creating results directory %s" % RESULTS_DIR
    os.makedirs(RESULTS_DIR)
                        
  all_results = run_tests(args.num_iterations, int(args.range[0]),
                          int(args.range[-1]))

if __name__ == "__main__":
  main()
                      
                      
