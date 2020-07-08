from collections.abc import Mapping

from .attrdict import AttributeDict

class AtlasView(Mapping):
    """This is a view into a dict-of-dict-like structure.

    Note that unlike NetworkX's AltasView, we need both the
    underlying graph and the ID for the node of interest in
    order to accomplish the same effect, hence the difference
    in the API."""
    __slots__ = ('_graph', '_node')

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __init__(self, g, n):
        '''Initialize with the input node and graph'''
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
            strs.append(str(k) + ': ' + str(self[k]))
        return "{" + ", ".join(strs) + "}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'


class AdjacencyView(Mapping):
    """This is a view into a dict-of-dict-of-dict-like structure."""
    __slots__ = '_graph',

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
            strs.append(str(n) + ': ' + str(self[n]))
        return "{" + ", ".join(strs) + "}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def copy(self):
        raise NotImplementedError("TODO")

