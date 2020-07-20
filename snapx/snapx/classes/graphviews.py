"""View of Graphs as SubGraph, Reverse, Directed, Undirected.
In some algorithms it is convenient to temporarily morph
a graph to exclude some nodes or edges. It should be better
to do that via a view than to remove and then re-add.
In other algorithms it is convenient to temporarily morph
a graph to reverse directed edges, or treat a directed graph
as undirected, etc. This module provides those graph views.
The resulting views are essentially read-only graphs that
report data from the orignal graph object. We provide an
attribute G._graph which points to the underlying graph object.
Note: Since graphviews look like graphs, one can end up with
view-of-view-of-view chains. Be careful with chains because
they become very slow with about 15 nested views.
For the common simple case of node induced subgraphs created
from the graph class, we short-cut the chain by returning a
subgraph of the original graph directly rather than a subgraph
of a subgraph. We are careful not to disrupt any edge filter in
the middle subgraph. In general, determining how to short-cut
the chain is tricky and much harder with restricted_views than
with induced subgraphs.
Often it is easiest to use .copy() to avoid chains.
"""
from snapx.classes.coreviews import (
    # UnionAdjacency,
    # UnionMultiAdjacency,
    FilterAtlas,
    FilterAdjacency,
    FilterMultiAdjacency,
)
from snapx.classes.filters import no_filter

# from snapx.exception import SnapXError
# from snapx.utils import not_implemented_for

import snapx as sx

__all__ = ["subgraph_view"]


def subgraph_view(G, filter_node=no_filter, filter_edge=no_filter):
    """ View of `G` applying a filter on nodes and edges.
    `subgraph_view` provides a read-only view of the input graph that excludes
    nodes and edges based on the outcome of two filter functions `filter_node`
    and `filter_edge`.
    The `filter_node` function takes one argument --- the node --- and returns
    `True` if the node should be included in the subgraph, and `False` if it
    should not be included.
    The `filter_edge` function takes two (or three arguments if `G` is a
    multi-graph) --- the nodes describing an edge, plus the edge-key if
    parallel edges are possible --- and returns `True` if the edge should be
    included in the subgraph, and `False` if it should not be included.
    Both node and edge filter functions are called on graph elements as they
    are queried, meaning there is no up-front cost to creating the view.
    Parameters
    ----------
    G : networkx.Graph
        A directed/undirected graph/multigraph
    filter_node : callable, optional
        A function taking a node as input, which returns `True` if the node
        should appear in the view.
    filter_edge : callable, optional
        A function taking as input the two nodes describing an edge (plus the
        edge-key if `G` is a multi-graph), which returns `True` if the edge
        should appear in the view.
    Returns
    -------
    graph : networkx.Graph
        A read-only graph view of the input graph.
    Examples
    --------
    >>> import networkx as nx
    >>> G = nx.path_graph(6)
    Filter functions operate on the node, and return `True` if the node should
    appear in the view:
    >>> def filter_node(n1):
    ...     return n1 != 5
    ...
    >>> view = nx.subgraph_view(
    ...     G,
    ...     filter_node=filter_node
    ... )
    >>> view.nodes()
    NodeView((0, 1, 2, 3, 4))
    We can use a closure pattern to filter graph elements based on additional
    data --- for example, filtering on edge data attached to the graph:
    >>> G[3][4]['cross_me'] = False
    >>> def filter_edge(n1, n2):
    ...     return G[n1][n2].get('cross_me', True)
    ...
    >>> view = nx.subgraph_view(
    ...     G,
    ...     filter_edge=filter_edge
    ... )
    >>> view.edges()
    EdgeView([(0, 1), (1, 2), (2, 3), (4, 5)])
    >>> view = nx.subgraph_view(
    ...     G,
    ...     filter_node=filter_node,
    ...     filter_edge=filter_edge,
    ... )
    >>> view.nodes()
    NodeView((0, 1, 2, 3, 4))
    >>> view.edges()
    EdgeView([(0, 1), (1, 2), (2, 3)])
    """
    newG = sx.freeze(G.__class__())
    newG._NODE_OK = filter_node
    newG._EDGE_OK = filter_edge

    # create view by assigning attributes from G
    newG._graph = G
    newG.graph = G.graph

    newG._node_extra_attr = FilterAtlas(G._node_extra_attr, filter_node)
    if G.is_multigraph():
        Adj = FilterMultiAdjacency

        def reverse_edge(u, v, k):
            return filter_edge(v, u, k)

    else:
        Adj = FilterAdjacency

        def reverse_edge(u, v):
            return filter_edge(v, u)

    if G.is_directed():
        newG._succ = Adj(G._succ, filter_node, filter_edge)
        newG._pred = Adj(G._pred, filter_node, reverse_edge)
        newG._adj = newG._succ
    else:
        newG.nodes = Adj(G.nodes, filter_node, filter_edge)
    return newG
