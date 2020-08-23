"""PORTED FROM NETWORKX
Connected components."""
import snapx as sx
from snap import GetSccs, GetMxScc, TCnComV
from snapx.utils.decorators import not_implemented_for

__all__ = [
    "connected_components",
    "max_connected_component",
]


@not_implemented_for("directed")
def connected_components(G):
    """Generate connected components.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph

    Returns
    -------
    comp : generator of sets
       A generator of sets of nodes, one for each component of G.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed.

    Examples
    --------
    Generate a sorted list of connected components, largest first.

    >>> G = nx.path_graph(4)
    >>> nx.add_path(G, [10, 11, 12])
    >>> [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    [4, 3]

    If you only want the largest connected component, it's more
    efficient to use max instead of sort.

    >>> largest_cc = max(nx.connected_components(G), key=len)

    To create the induced subgraph of each component use:

    >>> S = [G.subgraph(c).copy() for c in nx.connected_components(G)]

    See Also
    --------
    strongly_connected_components
    weakly_connected_components

    Notes
    -----
    For undirected graphs only.

    """
    Components = TCnComV()
    Graphs = []
    GetSccs(G._graph, Components)
    for CnCom in Components:
        Graphs.append(sx.Graph(incoming_graph_data=CnCom))
    return Graphs

@not_implemented_for("directed")
def max_connected_component(G):
    return sx.Graph(incoming_graph_data=GetMxScc(G._graph))



# def number_connected_components(G):
#     """Returns the number of connected components.

#     Parameters
#     ----------
#     G : NetworkX graph
#        An undirected graph.

#     Returns
#     -------
#     n : integer
#        Number of connected components

#     See Also
#     --------
#     connected_components
#     number_weakly_connected_components
#     number_strongly_connected_components

#     Notes
#     -----
#     For undirected graphs only.

#     """
#     return sum(1 for cc in connected_components(G))


# @not_implemented_for("directed")
# def is_connected(G):
#     """Returns True if the graph is connected, False otherwise.

#     Parameters
#     ----------
#     G : NetworkX Graph
#        An undirected graph.

#     Returns
#     -------
#     connected : bool
#       True if the graph is connected, false otherwise.

#     Raises
#     ------
#     NetworkXNotImplemented
#         If G is directed.

#     Examples
#     --------
#     >>> G = nx.path_graph(4)
#     >>> print(nx.is_connected(G))
#     True

#     See Also
#     --------
#     is_strongly_connected
#     is_weakly_connected
#     is_semiconnected
#     is_biconnected
#     connected_components

#     Notes
#     -----
#     For undirected graphs only.

#     """
#     if len(G) == 0:
#         raise nx.NetworkXPointlessConcept(
#             "Connectivity is undefined ", "for the null graph."
#         )
#     return sum(1 for node in _plain_bfs(G, arbitrary_element(G))) == len(G)


# @not_implemented_for("directed")
# def node_connected_component(G, n):
#     """Returns the set of nodes in the component of graph containing node n.

#     Parameters
#     ----------
#     G : NetworkX Graph
#        An undirected graph.

#     n : node label
#        A node in G

#     Returns
#     -------
#     comp : set
#        A set of nodes in the component of G containing node n.

#     Raises
#     ------
#     NetworkXNotImplemented
#         If G is directed.

#     See Also
#     --------
#     connected_components

#     Notes
#     -----
#     For undirected graphs only.

#     """
#     return _plain_bfs(G, n)