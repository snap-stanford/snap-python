#!/usr/bin/python
# convert.py
#
# Author: Nick Shelly, Spring 2013
# Description:
#     - Loads SNAP as a Python module.
#     - Randomly generates a graph of specified size and type and saving,
#         or loading the graph if has already been created.
#     - Converts the graph to the specified file
#           
#  usage: convert.py [-h] [-v]
#
#  optional arguments:
#    -h, --help            show this help message and exit
#
#   Example:
#   $ python benchmark.py -v -n 3 -g -d -r 2-3 -t rmat -o results/results.txt
#

import os.path
import sys
import argparse
from socket import gethostname
from time import clock
from datetime import datetime

sys.path.append("../swig-r")
import snap

PROPERTY_TYPES = [1, 10]  # 1=Triads, 10=BFS

# Comma-separated, graph types:
# 'rmat' - R-MAT
# 'pref' - preferential attachment
# 'sw' - small world
# 'rand_ungraph' - random undirected
# 'rand_ngraph' - random directed
# 'rand_neagraph' - random directed attribute
# 'syn_ngraph' - random directed
# 'syn_negraph' - synthetic multi-edge
# 'syn_neagraph' - synthetic directed multi-edge attribute

GRAPH_TYPES = ['rmat', 'pref', 'sw', \
                'rand_ungraph', 'rand_ngraph', 'rand_neagraph', \
                'syn_ngraph', 'syn_negraph', 'syn_neagraph']
DEFAULT_TYPES = "rmat,rand_ungraph"

DEFAULT_NODES_EXP = 3
DEFAULT_EDGES_EXP = 4

# Average is 1, non-average is 0.
DEFAULT_DEGREES = 1-2  #  Default is 10x and 100x edges/node
DEFAULT_WRITE = False
SW_REWIRE_PROB = 0.1
SYNTHETIC_DELTA = 10

# Exponent range (e.g. 10^x to 10^y)
DEFAULT_RANGE = '5-7'
DEFAULT_ITERATIONS = 1

# Hostname for results
HOSTNAME = gethostname()

RESULTS_DIR = 'results'
DEFAULT_RESULTS_FILE = os.path.join(RESULTS_DIR, 'results%s.txt' % \
                            datetime.now().strftime('%m%d-%H%M%S'))

def generate_graph(NNodes, NEdges, Model, Rnd):
  
  Graph = None
  if Model == 'rand_ungraph':
    # GnRndGnm returns error, so manually generate
    Graph = snap.GenRndGnm_PUNGraph(NNodes, NEdges, 0)

  elif Model == 'rand_ngraph':
    Graph = snap.GenRndGnm_PNGraph(NNodes, NEdges, 1)
      
  elif Model == 'rand_neagraph':
    Graph = snap.GenRndGnm_PNEANet(NNodes, NEdges, 1)

  elif Model == 'syn_neagraph':
    Graph = snap.GenSyntheticGraph_PNEANet(NNodes, NEdges/NNodes,
                                             SYNTHETIC_DELTA)

  elif Model == 'syn_ngraph':
    Graph = snap.GenSyntheticGraph_PNGraph(NNodes, NEdges/NNodes,
                                             SYNTHETIC_DELTA)

  elif Model == 'rmat':
    Graph = snap.GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2, Rnd)

  elif Model == 'sw':
    Graph = snap.GenSmallWorld(NNodes, NNodes/NEdges, 0.1)
  
  elif Model == 'pref':
    Graph = snap.GenPrefAttach(NNodes, NNodes/NEdges)

  else:
    print "Unknown model: %s" % Model
    sys.exit(1)

  return Graph


def convert_graph(Graph, TypeSrc, TypeDst):
  '''
    Converts a GRAPH from type TYPESRC to a TYPEDST and returns the new graph
  '''
  
  print "Converting from '%s' to '%s'..." % (TypeSrc, TypeDst)
  sys.stdout.flush()
  
  
  if TypeSrc == 'ngraph' and TypeDst == 'neagraph':

    GraphOut = snap.ConvertGraph_PNGraphToPNEANet(Graph)
  
  else:
    print "Unable to convert: %s to %s" % (TypeSrc, TypeDst)
    sys.exit(1)
  
  print "done"

  print "GraphIn (%s) has %d nodes, %d edges\n" % \
          (Graph.__class__, Graph.GetNodes(), Graph.GetEdges())
  print "GraphOut (%s) has %d nodes, %d edges" % \
          (GraphOut.__class__, GraphOut.GetNodes(), GraphOut.GetEdges())

def run(nodes_exp, edges_exp, InputModel, OutputType):
  
  '''
  Perform tests with specified exponent range
  '''

  if opt_verbose:
    print "Running results from %e to %e" % (min_nodes_exponent,
                                           max_nodes_exponent)

  Rnd = snap.TRnd()

  # Random number of nodes of degree i
  NNodes = 10**nodes_exp
  NEdges = 10**edges_exp
  
  if opt_deterministic:
    if opt_verbose:
      print "Deterministic mode, putting seed"
  else:
    if opt_verbose:
      print "Non-deterministic mode"
    Rnd.PutSeed(0)

  if opt_verbose: print "Using average degree of 10^%d" % avg_deg
    
  StartTime = clock()
    
  # User wants to re-generate graph, or no graph data available.
  if opt_verbose:
    print "Generating '%s %s' graph with %e nodes, %e edges..." % \
            (Type, g, NNodes, NEdges),
    sys.stdout.flush()
  Graph = generate_graph(NNodes, NEdges, InputModel, Rnd)
  if opt_verbose: print "done"

  if InputModel in ['rmat', 'rand_ngraph', 'syn_ngraph','syn_negraph']:
    TypeSrc = "ngraph"
  
  elif InputModel in ['sw', 'pref', 'rand_ungraph']:
    TypeSrc = "ungraph"
  
  elif InputModel in ['rand_neagraph', 'syn_neagraph']:
    TypeSrc = "neagraph"
  
  else:
    print "Unknown graph type: %s" % g
    sys.exit(1)

  convert_graph(Graph, TypeSrc, OutputType)
  print "-"*75

def main():
    
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", default=False,
                      action="store_true", dest="verbose",
                      help="increase output verbosity")

  parser.add_argument("-n", "--nodes_exp", default=DEFAULT_NODES_EXP,
                      help="number of nodes, exponent (e.g. 4 => 10^4 nodes)")

  parser.add_argument("-e", "--edges_exp", default=DEFAULT_EDGES_EXP,
                      help="number of edges, exponent (e.g. 4 => 10^4 edges)")

  parser.add_argument("-d", "--deterministic", default=False,
                        action="store_true", dest="deterministic",
                        help="deterministic benchmark")

  parser.add_argument("-i", "--input_model", required=True,
                      help='''
          Graph types, comma separated: (rmat, pref, rand_ngraph, syn_ngraph)'''

  parser.add_argument("-o", "--output_type", required=True,
                      help="output type (PNEANet)")

  args = parser.parse_args()

  global opt_verbose, opt_deterministic, opt_nodes_exp, opt_edges_exp

  opt_verbose = args.verbose
  opt_deterministic = args.deterministic
  
  if opt_verbose:
    print "Hostname: %s" % HOSTNAME

  run(args.nodes_exp, args.edges_exp, args.input_model, args.output_type)

if __name__ == "__main__":
  main()
                      
                      
