"""
Ego graph.
"""
__all__ = ["ego_graph"]

import snapx as sx
import snap


def ego_graph(G, n, radius=1, sample=-1.0, traversal='in', copy_attr=True):
    """PORTED FROM NETWORKX
    Returns induced subgraph of neighbors centered at node n within
    a given radius.

    Parameters
    ----------
    G : graph
      A NetworkX Graph or DiGraph

    n : node
      A single node

    radius : number, optional
      Include all neighbors of distance<=radius from n.

    center : bool, optional - NOT ADDED
      If False, do not include center node in graph

    undirected : bool, optional - NOT ADDED
      If True use both in- and out-neighbors of directed graphs.

    distance : key, optional - NOT ADDED
      Use specified edge data key as distance.  For example, setting
      distance='weight' will use the edge weight to measure the
      distance from the node n.
    
    sample : int/float, optional
      Number of nodes to sample as neighbors. Either positive int or float
      between 0.0 and 1.0.

    traversal : str, optional, either 'in', 'out', 'all'
      Get in, out or both ego neighborhoods

    copy_attr : bool, optional
      Copy node and edge attributes to ego graph
    """
    if traversal == 'in':
        if copy_attr:
            if sample != -1.0:
                if type(sample) is int:
                    if 0 > sample:
                        raise RuntimeError
                    else:
                        snapGraph = snap.GetInEgonetSubAttr(G._graph, n, radius, sample, -1.0)
                        return sx.Graph(incoming_graph_data=snapGraph)
                else:
                    if not 0.0 <= sample <= 1.0:
                        raise RuntimeError
                    else:
                        snapGraph = snap.GetInEgonetSubAttr(G._graph, n, radius, 0, sample)
                        return sx.Graph(incoming_graph_data=snapGraph)
            else:
                snapGraph = snap.GetInEgonetAttr(G._graph, n, radius)
                return sx.Graph(incoming_graph_data=snapGraph)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError

