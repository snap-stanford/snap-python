from collections.abc import MutableMapping

from snap import TStrV
from snapx.exception import SnapXKeyError, SnapXTypeError

class AttributeDict(MutableMapping):
    """Wraps snap's attributes representations and presents them
    like a Python built-in dict.

    For attribute types not supported by Snap, it emulates the behavior by
    storing these in the extra attribute dictionaries.

    This layer should work for both node and edge attributes.

    DESIGN NOTE:
    1) What gets stored in SNAP's feature storage
    For the time being, only int types are stored to SNAP's
    feature store, and the rest will go straight to the extra attr dicts.
    The following is an illustration of what gets stored where:
    >>> g = sx.Graph()
    >>> g.add_nodes([(0, {'foo': 'bar'}), (1, {'foo': 1})])
    >>> # Node 0's foo is in extra dict, Node 1's foo is in SNAP

    2) Treatment of edge attributes for undirected graphs
    Since we use TNEANet as the underlying graph data structure, we are
    emulating the undirected graph's behavior by sorting the pair of nodes
    of an edge in the ascending order, so that we consistently access the
    same internal attribute storage.
    For example, edge attribute queries for both (1, 4) and (4, 1) will
    look at the internal storage for (1, 4)
    """
    def __init__(self, graph, key):
        self._graph = graph
        if isinstance(key, int):
            self._is_node = True
        elif isinstance(key, tuple) and len(key) == 2 \
            and isinstance(key[0], int) and isinstance(key[1], int):
            self._is_node = False
        else:
            raise SnapXTypeError("Argument 2 must be either node (int) or edge (2-tuple).")

        # Need to convert a (src, dst) pair to the EI in the case of edge.
        try:
            if self._is_node:
                self._key = key
                self._extra_attr = self._graph._node_extra_attr
            else:
                # IMPORTANT NOTE: src and dst gets reordered for UNDIRECTED graphs.
                src, dst = key if graph.is_directed() else graph._order_edge(*key)
                self._key = key if self._is_node else self._graph.snap_graph.GetEI(src, dst).GetId()
                self._edge = (src, dst)
                self._extra_attr = self._graph._edge_extra_attr

        except:
            raise SnapXKeyError("Failed to get the edge ID for {}".format(str(key)))

        # TODO: Support floats and strs
        # For iteration over Snap's attribute stores
        self._snap_attr_names = self._graph.snap_graph.IntAttrNameNI if self._is_node else \
                              self._graph.snap_graph.IntAttrNameEI

        # For setting values to Snap's attr stores
        self._snap_attr_setter = self._graph.snap_graph.AddIntAttrDatN if self._is_node else \
                             self._graph.snap_graph.AddIntAttrDatE

        # For getting values from Snap's attr stores
        self._snap_attr_getter = self._graph.snap_graph.GetIntAttrDatN if self._is_node else \
                             self._graph.snap_graph.GetIntAttrDatE

        # For deleting values from snap's attr stores
        self._snap_attr_del = self._graph.snap_graph.DelAttrDatN if self._is_node else \
                             self._graph.snap_graph.DelAttrDatE

    def __yield_snap_attrs(self):
        _attr_names = TStrV()
        self._snap_attr_names(self._key, _attr_names)
        for _attr in _attr_names:
            yield _attr

    def __iter__(self):
        # First yield snap attributes
        for _attr in self.__yield_snap_attrs():
            yield _attr

        # Now yield the rest
        try:
            extra_attr_dict = self._extra_attr[self._key] if self._is_node else \
                              self._extra_attr[self._edge[0]][self._edge[1]]
            for _attr in extra_attr_dict:
                yield _attr
        except KeyError:
            pass

    def __contains__(self, key):
        for _attr in self:
            if _attr == key:
                return True

        return False

    def __len__(self):
        return sum(1 for _ in iter(self))

    def __getitem__(self, attr):
        try:
            return self._snap_attr_getter(self._key, attr)
        except RuntimeError:
            extra_attr_getter = self._node_extra_attr_getter \
                                if self._is_node else \
                                self._edge_extra_attr_getter
            return extra_attr_getter(self._key, attr)

    def _node_extra_attr_setter(self, key, val, attr):
        """Sets the node attr to val.
        Should be used only for attr types not directly supported by Snap."""
        if key not in self._graph:
            raise KeyError

        if key not in self._graph._node_extra_attr:
            self._graph._node_extra_attr[key] = {}
        self._graph._node_extra_attr[key][attr] = val

    def _node_extra_attr_getter(self, key, attr):
        """Gets the node attr val.
        Should be used only for attr types not directly supported by Snap."""
        try:
            return self._graph._node_extra_attr[key][attr]
        except KeyError:
            return None

    def _edge_extra_attr_setter(self, key, val, attr):
        """Sets the edge attr to val.
        Should be used only for attr types not directly supported by Snap."""
        u, v = self._edge
        if u not in self._graph._edge_extra_attr:
            self._graph._edge_extra_attr[u] = {}
        if v not in self._graph._edge_extra_attr:
            self._graph._edge_extra_attr[v] = {}

        if v not in self._graph._edge_extra_attr[u]:
            datadict = {}
            self._graph._edge_extra_attr[u][v] = datadict
            if u != v:
                self._graph._edge_extra_attr[v][u] = datadict

        self._graph._edge_extra_attr[u][v][attr] = val

    def _edge_extra_attr_getter(self, key, attr):
        # TODO: Clean up design of setters & getters
        u, v = self._edge
        try:
            return self._graph._edge_extra_attr[u][v][attr]
        except KeyError:
            return None

    def __setitem__(self, attr, val):
        if not isinstance(attr, str):
            raise SnapXTypeError("Argument 2 must be type str.")

        setter = self._node_extra_attr_setter \
                 if self._is_node else \
                 self._edge_extra_attr_setter
        # Dispatch to corresponding setters if the type is supported by Snap.
        # Currently only int is supported
        if isinstance(val, int):
            setter = self._snap_attr_setter

        setter(self._key, val, attr)

    def __delitem__(self, attr):
        if attr not in self:
            return

        if isinstance(self[attr], int):
            self._snap_attr_del(self._key, attr)
        else:
            extra_attr_dict = self._extra_attr[self._key] if self._is_node else \
                              self._extra_attr[self._edge[0]][self._edge[1]]
            del extra_attr_dict[attr]

    def __str__(self):
        strs = []
        for k in iter(self):
            strs.append("'{}': {}".format(k, repr(self[k])))
        return "{" + ", ".join(strs) + "}"

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.__str__())

