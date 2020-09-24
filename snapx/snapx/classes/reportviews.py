from .attrdict import AttributeDict
from collections.abc import Mapping, Set

# NodeViews
class NodeView(Mapping, Set):
    __slots__ = ("_graph",)

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __init__(self, graph):
        self._graph = graph

    # Mapping methods
    def __len__(self):
        return len(self._graph)

    def __iter__(self):
        return iter(self._graph)

    def __getitem__(self, n):
        if n not in self._graph:
            raise KeyError(str(n))
        return AttributeDict(self._graph, n)

    # Set methods
    def __contains__(self, n):
        return n in self._graph

    @classmethod
    def _from_iterable(cls, it):
        return set(it)

    # DataView method
    def __call__(self, data=False, default=None):
        if data is False:
            return self
        return NodeDataView(self._graph, data, default)

    def data(self, data=True, default=None):
        if data is False:
            return self
        return NodeDataView(self._graph, data, default)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, tuple(self))


class NodeDataView(Set):
    __slots__ = ("_graph", "_data", "_default")

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __init__(self, graph, data=False, default=None):
        self._graph = graph
        self._data = data
        self._default = default

    @classmethod
    def _from_iterable(cls, it):
        try:
            return set(it)
        except TypeError as err:
            if "unhashable" in str(err):
                msg = " : Could be b/c data=True or your values are unhashable"
                raise TypeError(str(err) + msg)
            raise

    def __len__(self):
        return len(self._graph)

    def __iter__(self):
        for n in self._graph:
            if isinstance(self._data, bool):
                if self._data:
                    yield (n, AttributeDict(self._graph, n))
                else:
                    yield n
            else:
                val = AttributeDict(self._graph, n)[self._data]
                val = val if val else (self._default if self._default else None)
                yield (n, val)

    def __contains__(self, n):
        try:
            node_in = n in self._graph
        except TypeError:
            n, d = n
            return n in self._graph and self[n] == d
        if node_in is True:
            return node_in
        try:
            n, d = n
        except (TypeError, ValueError):
            return False
        return n in self._graph and self[n] == d

    def __getitem__(self, n):
        ddict = self._graph.nodes[n]
        data = self._data
        if data is False or data is True:
            return ddict
        return ddict[data] if data in ddict else self._default

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        name = self.__class__.__name__
        if self._data is False:
            return "{}({})".format(name, tuple(self))
        if self._data is True:
            return "{}({})".format(name, dict(self))
        return "{}({}, data={})".format(name, dict(self), self._data.__repr__())


class OutEdgeDataView:
    """EdgeDataView for outward edges of DiGraph; See EdgeDataView"""

    __slots__ = (
        "_viewer",
        "_nbunch",
        "_data",
        "_default",
        "_graph",
        "_nodes_nbrs",
        "_report",
    )

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    def __init__(self, viewer, nbunch=None, data=False, default=None):
        self._viewer = viewer
        graph = self._graph = viewer._graph  # FIXME: Better way to pass graph?

        if nbunch is None:
            self._nodes_nbrs = graph.adj.items
        else:
            nbunch = list(graph.nbunch_iter(nbunch))
            self._nodes_nbrs = lambda: [(n, graph.adj[n]) for n in nbunch]

        self._nbunch = nbunch
        self._data = data
        self._default = default

        # Set _report based on data and default
        if data is True:
            self._report = lambda n, nbr, dd: (n, nbr, dd)
        elif data is False:
            self._report = lambda n, nbr, dd: (n, nbr)
        else:  # data is attribute name
            self._report = (
                lambda n, nbr, dd: (n, nbr, dd[data])
                if data in dd
                else (n, nbr, default)
            )

    def __len__(self):
        # TODO: Support nbunch and returning # of their neighbors
        return self._graph.number_of_edges()

    def __iter__(self):
        return (
            self._report(n, nbr, dd)
            for n, nbrs in self._nodes_nbrs()
            for nbr, dd in nbrs.items()
        )

    def __contains__(self, e):
        try:
            u, v = e[:2]
            ddict = AttributeDict(self._graph, (u, v))
        except KeyError:
            return False
        return e == self._report(u, v, ddict)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, list(self))


class EdgeDataView(OutEdgeDataView):
    __slots__ = ()

    def __len__(self):
        return sum(1 for e in self)

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr, dd in nbrs.items():
                if nbr not in seen:
                    yield self._report(n, nbr, dd)
            seen[n] = 1
        del seen


# EdgeViews    have set operations and no data reported
class OutEdgeView(Set, Mapping):
    """A EdgeView class for outward edges of a DiGraph"""

    __slots__ = ("_graph", "_nodes_nbrs")

    dataview = OutEdgeDataView

    def __getstate__(self):
        raise NotImplementedError("TODO")

    def __setstate__(self, state):
        raise NotImplementedError("TODO")

    @classmethod
    def _from_iterable(cls, it):
        return set(it)

    def __init__(self, G):
        self._graph = G
        self._nodes_nbrs = G.adj.items

    # Set methods
    def __len__(self):
        return sum(len(nbrs) for n, nbrs in self._nodes_nbrs())

    def __iter__(self):
        for n, nbrs in self._nodes_nbrs():
            for nbr in nbrs:
                yield (n, nbr)

    def __contains__(self, e):
        return self._graph.has_edge(*e)

    # Mapping Methods
    def __getitem__(self, e):
        return AttributeDict(self._graph, e)

    # EdgeDataView methods
    def __call__(self, nbunch=None, data=False, default=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    def data(self, data=True, default=None, nbunch=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    # String Methods
    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, list(self))


class EdgeView(OutEdgeView):
    __slots__ = ()
    dataview = EdgeDataView

    def __len__(self):
        num_nbrs = (len(nbrs) + (n in nbrs) for n, nbrs in self._nodes_nbrs())
        return sum(num_nbrs) // 2

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr in list(nbrs):
                if nbr not in seen:
                    yield (n, nbr)
            seen[n] = 1
        del seen

