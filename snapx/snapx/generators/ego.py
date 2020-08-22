"""
Ego graph.
"""
__all__ = ["ego_graph"]

import snapx as sx
import snap


def ego_graph(G, n, radius=1, center=True, undirected=False, distance=None):
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

    center : bool, optional
      If False, do not include center node in graph

    undirected : bool, optional
      If True use both in- and out-neighbors of directed graphs.

    distance : key, optional
      Use specified edge data key as distance.  For example, setting
      distance='weight' will use the edge weight to measure the
      distance from the node n.

    Notes
    -----
    For directed graphs D this produces the "out" neighborhood
    or successors.  If you want the neighborhood of predecessors
    first reverse the graph with D.reverse().  If you want both
    directions use the keyword argument undirected=True.

    Node, edge, and graph attributes are copied to the returned subgraph.
    """
    if undirected:
        if distance is not None:
            raise NotImplementedError
        else:
            # ret = snap.GetEgonet(H, n)
            H = snap.ConvertGraph(snap.PNGraph, G._graph)
            Nodes = snap.TIntV()
            for N in H.GetNI(n).GetOutEdges():
                Nodes.Add(N)
            I = snap.GetSubGraphRenumber(H, Nodes)
            J = sx.Graph()
            J._graph = snap.ConvertGraph(snap.PNEANet, I)
            return J
    else:
        raise NotImplementedError

