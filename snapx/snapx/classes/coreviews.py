from collections.abc import Mapping

from .attrdict import AttributeDict


class AtlasView(Mapping):
    """This is a view into a dict-of-dict-like structure.
    This view shows a certain node's neighbors and their edge attributes.

    Note that unlike NetworkX's AltasView, we need both the
    underlying graph and the ID for the node of interest in
    order to accomplish the same effect, hence the difference
    in the API."""

    __slots__ = ("_graph", "_node")

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __init__(self, g, n):
        """Initialize with the input node and graph"""
        self._graph = g
        self._node = n

        if not isinstance(n, int):
            raise TypeError("Node ID must be int.")
        if n not in g:
            raise KeyError("Node must be present in graph.")

    def __len__(self):
        return sum(1 for d in self)

    def __iter__(self):
        ni = self._graph.snap_graph.GetNI(self._node)
        for dst in ni.GetOutEdges():
            yield dst

    def __getitem__(self, key):
        return AttributeDict(self._graph, (self._node, key))

    def copy(self):
        raise NotImplementedError("TODO")

    def __str__(self):
        strs = []
        for k in iter(self):
            strs.append(str(k) + ": " + str(self[k]))
        return "{" + ", ".join(strs) + "}"

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__str__())

class AdjacencyView(Mapping):
    """This is a view into a dict-of-dict-of-dict-like data structure.
    This view shows all nodes' neighbors and their edge attributes.
    """

    __slots__ = ("_graph",)

    def __init__(self, g):
        self._graph = g

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __getitem__(self, node):
        return AtlasView(self._graph, node)

    def __len__(self):
        return sum(1 for n in self)

    def __iter__(self):
        for n in self._graph:
            yield n

    def __str__(self):
        strs = []
        for n in iter(self):
            strs.append(str(n) + ": " + str(self[n]))
        return "{" + ", ".join(strs) + "}"

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__str__())

    def copy(self):
        raise NotImplementedError("TODO")


class FilterAtlas(Mapping):  # nodedict, nbrdict, keydict
    def __init__(self, d, NODE_OK):
        self._atlas = d
        self.NODE_OK = NODE_OK

    def __len__(self):
        return sum(1 for n in self)

    def __iter__(self):
        try:  # check that NODE_OK has attr 'nodes'
            node_ok_shorter = 2 * len(self.NODE_OK.nodes) < len(self._atlas)
        except AttributeError:
            node_ok_shorter = False
        if node_ok_shorter:
            return (n for n in self.NODE_OK.nodes if n in self._atlas)
        return (n for n in self._atlas if self.NODE_OK(n))

    def __getitem__(self, key):
        if key in self._atlas and self.NODE_OK(key):
            return self._atlas[key]
        raise KeyError("Key {} not found".format(key))

    def copy(self):
        try:  # check that NODE_OK has attr 'nodes'
            node_ok_shorter = 2 * len(self.NODE_OK.nodes) < len(self._atlas)
        except AttributeError:
            node_ok_shorter = False
        if node_ok_shorter:
            return {u: self._atlas[u] for u in self.NODE_OK.nodes if u in self._atlas}
        return {u: d for u, d in self._atlas.items() if self.NODE_OK(u)}

    def __str__(self):
        return str({nbr: self[nbr] for nbr in self})

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self._atlas.__repr__(), self.NODE_OK._repr__())

class FilterAdjacency(Mapping):  # edgedict
    def __init__(self, d, NODE_OK, EDGE_OK):
        self._atlas = d
        self.NODE_OK = NODE_OK
        self.EDGE_OK = EDGE_OK

    def __len__(self):
        return sum(1 for n in self)

    def __iter__(self):
        try:  # check that NODE_OK has attr 'nodes'
            node_ok_shorter = 2 * len(self.NODE_OK.nodes) < len(self._atlas)
        except AttributeError:
            node_ok_shorter = False
        if node_ok_shorter:
            return (n for n in self.NODE_OK.nodes if n in self._atlas)
        return (n for n in self._atlas if self.NODE_OK(n))

    def __getitem__(self, node):
        if node in self._atlas and self.NODE_OK(node):

            def new_node_ok(nbr):
                return self.NODE_OK(nbr) and self.EDGE_OK(node, nbr)

            return FilterAtlas(self._atlas[node], new_node_ok)
        raise KeyError("Key {} not found".format(key))

    def copy(self):
        try:  # check that NODE_OK has attr 'nodes'
            node_ok_shorter = 2 * len(self.NODE_OK.nodes) < len(self._atlas)
        except AttributeError:
            node_ok_shorter = False
        if node_ok_shorter:
            return {
                u: {
                    v: d
                    for v, d in self._atlas[u].items()
                    if self.NODE_OK(v)
                    if self.EDGE_OK(u, v)
                }
                for u in self.NODE_OK.nodes
                if u in self._atlas
            }
        return {
            u: {v: d for v, d in nbrs.items() if self.NODE_OK(v) if self.EDGE_OK(u, v)}
            for u, nbrs in self._atlas.items()
            if self.NODE_OK(u)
        }

    def __str__(self):
        return str({nbr: self[nbr] for nbr in self})

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self._atlas.__repr__(), self.NODE_OK__repr__(), self.EDGE_OK.__repr__())


class FilterMultiAdjacency(FilterAdjacency):  # multiedgedict
    def __getitem__(self, node):
        if node in self._atlas and self.NODE_OK(node):

            def edge_ok(nbr, key):
                return self.NODE_OK(nbr) and self.EDGE_OK(node, nbr, key)

            return FilterMultiInner(self._atlas[node], self.NODE_OK, edge_ok)
        raise KeyError("Key {} not found".format(node))

    def copy(self):
        try:  # check that NODE_OK has attr 'nodes'
            node_ok_shorter = 2 * len(self.NODE_OK.nodes) < len(self._atlas)
        except AttributeError:
            node_ok_shorter = False
        if node_ok_shorter:
            my_nodes = self.NODE_OK.nodes
            return {
                u: {
                    v: {k: d for k, d in kd.items() if self.EDGE_OK(u, v, k)}
                    for v, kd in self._atlas[u].items()
                    if v in my_nodes
                }
                for u in my_nodes
                if u in self._atlas
            }
        return {
            u: {
                v: {k: d for k, d in kd.items() if self.EDGE_OK(u, v, k)}
                for v, kd in nbrs.items()
                if self.NODE_OK(v)
            }
            for u, nbrs in self._atlas.items()
            if self.NODE_OK(u)
        }
