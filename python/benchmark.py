import os.path
import sys
import argparse
import random
from socket import gethostname

from datetime import datetime

sys.path.append("../swig")
import snap as Snap
from math import log

PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Graph types:
# 'rand_ungraph' - random undirected
# 'rand_ngraph' - random directed
# 'rmat' - R-MAT
# 'pref' - preferential attachment
# 'sw' - small world

DEFAULT_TYPES = "rmat"      #   Comma separated

# Average is 1, non-average is 0.
DEGREES = [10]  #  List of degrees to loop [10, 100] tries N*10, N*100 edges
SW_REWIRE_PROB = 0.1

# Exponent range (e.g. 10^x to 10^y)
DEFAULT_RANGE = '5-7'
DEFAULT_ITERATIONS = 1

# Hostname for results
HOSTNAME = gethostname()

RESULTS_DIR = 'results'
RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%M%S'))

def benchmark_ngraph(Graph):
  '''
  Perform benchmark tests for Directed Graphs
  '''
  
  results = {}
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

def benchmark_ungraph(Graph):
  '''
  Perform benchmark tests for Undirected Graphs
  '''

  results = {}
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
  
  if Model == 'rand_ungraph':
    # GnRndGnm returns error, so manually generate
    Graph = Snap.GenRndGnm_PUNGraph(NNodes, NEdges, 0)

  elif Model == 'rand_ngraph':
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
  Perform tests with specificed exponent range
  '''

  all_results = []
  
  if verbose:
    print "Running results from %e to %e" % (min_nodes_exponent,
                                           max_nodes_exponent)
  
  for n in range(num_iterations):
    if verbose:
      print "Iteration: %d of %d" % (n+1, num_iterations)
  
    for exp in range(min_nodes_exponent,max_nodes_exponent+1):
      
      for g in graph_types:
        
        # Random number of nodes of degree i
        NNodes = 10**exp;
        
        for avg_deg in DEGREES:
          
          if verbose:
            print "Using average degree of %d" % avg_deg
          NEdges = NNodes*avg_deg
        
          Graph = None
          if g in ['rmat', 'rand_ngraph']:
            Type = "directed"
      
          elif g in ['sw', 'pref', 'rand_ungraph']:
            Type = "undirected"
        
          else:
            print "Unknown graph type: %s" % g
          
          StartTime = datetime.now()
          FName = os.path.join(RESULTS_DIR, "%s_10e%d_deg%d_%d.graph" %
                              (g, exp, NEdges/NNodes, n))
        
          if not generate:
            
            if os.path.exists(FName):
              try:
              
                if verbose:
                  print "Loading '%s' from ...'%s'" % (g, FName)
                
                FIn = Snap.TFIn(Snap.TStr(FName))
                if Type == "directed":
                  Graph = Snap.PNGraph_New()
                else:
                  Graph = Snap.PUNGraph_New()
                Graph = Graph.Load(FIn)
              
                if verbose:
                  print "Re-loaded graph with %d Nodes and %d Edges" % \
                    (Graph.GetNodes(), Graph.GetEdges())
  
              except Exception, e:
                print "Unable to load graph file, '%s': %s" % (FName, str(e))

            else:
              print "File not found: %s" % FName

            
          if not Graph:
            
            try:
            
              # User wants to re-generate graph, or no graph data available.
              if verbose:
                print "Generating %s '%s' graph with %d nodes, %d edges" % \
                        (Type, g, NNodes, NEdges)
              
              Graph = generate_graph(NNodes, NEdges, g, Type)
            
              # Save the graph
              print "Saving '%s' graph to file ... '%s'" % (g, FName)
              if Graph:

                  FOut = Snap.TFOut(Snap.TStr(FName))
                  Graph.__ref__().Save(FOut)   # Save as TUNGraph or TNGraph
                  FOut.Flush()
            
            except Exception, e:
              print "Unable to generate/save graph file, '%s': %s" % \
                    (FName, str(e))
              continue

          TimeGenerate = datetime.now() - StartTime

          print "Running tests..."
          StartTime = datetime.now()

          if Type == 'directed':
            results = benchmark_ngraph(Graph)
          if Type == 'undirected':
            results = benchmark_ungraph(Graph)

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
  
  global results_dir, verbose, generate, graph_types, hostname, num_iterations
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")
  parser.add_argument("-r", "--range", default=DEFAULT_RANGE,
                      help="range (4-6) (10^4 to 10^6 nodes)")
  
  parser.add_argument("-t", "--graph_types", default=DEFAULT_TYPES,
                      help='''
      Graph types, comma separated.
      Available: rand_ungraph, rand_ngraph, rmat, pref, sw''')

  parser.add_argument("-n", "--num_iterations", type=int,
                      default=DEFAULT_ITERATIONS, help="number of iterations")

  parser.add_argument("-g", "--generate", default=False,
                      action="store_true", dest="generate", help="generate new graphs")
  
  args = parser.parse_args()
  
  verbose = args.verbose
  generate = args.generate
  num_iterations = args.num_iterations
  graph_types = args.graph_types.split(",")
  
  if verbose:
    print "Hostname: %s" % HOSTNAME
    print "Range = 10^%s to 10^%s" % (args.range[0], args.range[-1])
  
  if not os.path.exists(RESULTS_DIR):
    print "Creating results directory %s" % RESULTS_DIR
    os.makedirs(RESULTS_DIR)
                        
  all_results = run_tests(num_iterations, int(args.range[0]),
                          int(args.range[-1]))

if __name__ == "__main__":
  main()
                      
                      
