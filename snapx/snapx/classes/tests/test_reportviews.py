import pytest

import snapx as sx
from snapx.classes.reportviews import NodeDataView
from snapx import AttributeDict

# Nodes
class TestNodeView:
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.nv = cls.G.nodes  # NodeView(G)

    # NOTE: Not supported
    # def test_pickle(self):
    #     import pickle

    #     nv = self.nv
    #     pnv = pickle.loads(pickle.dumps(nv, -1))
    #     assert nv == pnv
    #     assert nv.__slots__ == pnv.__slots__

    def test_str(self):
        assert str(self.nv) == "[0, 1, 2, 3, 4, 5, 6, 7, 8]"

    def test_repr(self):
        assert repr(self.nv) == "NodeView((0, 1, 2, 3, 4, 5, 6, 7, 8))"

    def test_contains(self):
        G = self.G.copy()
        nv = G.nodes
        assert 7 in nv
        assert 9 not in nv
        # NOTE: Node removal not supported.
        # G.remove_node(7)
        # G.add_node(9)
        # assert 7 not in nv
        # assert 9 in nv

    def test_getitem(self):
        G = self.G.copy()
        nv = G.nodes
        G.nodes[3]["foo"] = "bar"
        assert nv[7] == {}
        assert nv[3] == {"foo": "bar"}

    def test_iter(self):
        nv = self.nv
        for i, n in enumerate(nv):
            assert i == n
        inv = iter(nv)
        assert next(inv) == 0
        assert iter(nv) != nv
        assert iter(inv) == inv
        inv2 = iter(nv)
        next(inv2)
        assert list(inv) == list(inv2)
        # odd case where NodeView calls NodeDataView with data=False
        nnv = nv(data=False)
        for i, n in enumerate(nnv):
            assert i == n

    def test_call(self):
        nodes = self.nv
        assert nodes is nodes()
        assert nodes is not nodes(data=True)
        assert nodes is not nodes(data="weight")

class TestNodeDataView:
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.nv = NodeDataView(cls.G)
        cls.ndv = cls.G.nodes.data(True)
        cls.nwv = cls.G.nodes.data("foo")

    def test_viewtype(self):
        nv = self.G.nodes
        ndvfalse = nv.data(False)
        assert nv is ndvfalse
        assert nv is not self.ndv

    # NOTE: Not supported
    #def test_pickle(self):
    #    import pickle

    #    nv = self.nv
    #    pnv = pickle.loads(pickle.dumps(nv, -1))
    #    assert nv == pnv
    #    assert nv.__slots__ == pnv.__slots__

    def test_str(self):
        msg = str([(n, AttributeDict(self.G, n)) for n in range(9)])
        assert str(self.ndv) == msg

    def test_repr(self):
        expected = "NodeDataView((0, 1, 2, 3, 4, 5, 6, 7, 8))"
        assert repr(self.nv) == expected
        expected_data = ["{}: {}".format(n, repr(AttributeDict(self.G, n))) for n in range(9)]
        expected = "NodeDataView({" + ", ".join(expected_data) + "})"
        assert repr(self.ndv) == expected
        expected = (
            "NodeDataView({0: None, 1: None, 2: None, 3: None, 4: None, "
            + "5: None, 6: None, 7: None, 8: None}, data='foo')"
        )
        assert repr(self.nwv) == expected

    def test_contains(self):
        G = self.G.copy()
        nv = G.nodes.data()
        nwv = G.nodes.data("foo")
        G.nodes[3]["foo"] = "bar"
        assert (7, {}) in nv
        assert (3, {"foo": "bar"}) in nv
        assert (3, "bar") in nwv
        assert (7, None) in nwv
        # default
        nwv_def = G.nodes(data="foo", default="biz")
        assert (7, "biz") in nwv_def
        assert (3, "bar") in nwv_def

    def test_getitem(self):
        G = self.G.copy()
        nv = G.nodes
        G.nodes[3]["foo"] = "bar"
        assert nv[3] == {"foo": "bar"}
        # default
        nwv_def = G.nodes(data="foo", default="biz")
        assert nwv_def[7], "biz"
        assert nwv_def[3] == "bar"

    def test_iter(self):
        G = self.G.copy()
        nv = G.nodes.data()
        ndv = G.nodes.data(True)
        nwv = G.nodes.data("foo")
        for i, (n, d) in enumerate(nv):
            assert i == n
            assert d == {}
        inv = iter(nv)
        assert next(inv) == (0, {})
        G.nodes[3]["foo"] = "bar"
        # default
        for n, d in nv:
            if n == 3:
                assert d == {"foo": "bar"}
            else:
                assert d == {}
        # data=True
        for n, d in ndv:
            if n == 3:
                assert d == {"foo": "bar"}
            else:
                assert d == {}
        # data='foo'
        for n, d in nwv:
            if n == 3:
                assert d == "bar"
            else:
                assert d is None
        # data='foo', default=1
        for n, d in G.nodes.data("foo", default=1):
            if n == 3:
                assert d == "bar"
            else:
                assert d == 1

def test_nodedataview_unhashable():
    G = sx.path_graph(9)
    G.nodes[3]["foo"] = "bar"
    nvs = [G.nodes.data()]
    nvs.append(G.nodes.data(True))
    H = G.copy()
    H.nodes[4]["foo"] = {1, 2, 3}
    nvs.append(H.nodes.data(True))
    # raise unhashable
    for nv in nvs:
        pytest.raises(TypeError, set, nv)
        pytest.raises(TypeError, eval, "nv | nv", locals())
    # no raise... hashable
    Gn = G.nodes.data(False)
    set(Gn)
    Gn | Gn
    Gn = G.nodes.data("foo")
    set(Gn)
    Gn | Gn


class TestNodeViewSetOps:
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.G.nodes[3]["foo"] = "bar"
        cls.nv = cls.G.nodes

    def n_its(self, nodes):
        return {node for node in nodes}

    def test_len(self):
        G = self.G.copy()
        nv = G.nodes
        assert len(nv) == 9
        # NOTE: Remove node not supported
        # G.remove_node(7)
        # assert len(nv) == 8
        G.add_node(9)
        assert len(nv) == 10

    def test_and(self):
        # print("G & H nodes:", gnv & hnv)
        nv = self.nv
        some_nodes = self.n_its(range(5, 12))
        assert nv & some_nodes == self.n_its(range(5, 9))
        assert some_nodes & nv == self.n_its(range(5, 9))

    def test_or(self):
        # print("G | H nodes:", gnv | hnv)
        nv = self.nv
        some_nodes = self.n_its(range(5, 12))
        assert nv | some_nodes == self.n_its(range(12))
        assert some_nodes | nv == self.n_its(range(12))

    def test_xor(self):
        # print("G ^ H nodes:", gnv ^ hnv)
        nv = self.nv
        some_nodes = self.n_its(range(5, 12))
        nodes = {0, 1, 2, 3, 4, 9, 10, 11}
        assert nv ^ some_nodes == self.n_its(nodes)
        assert some_nodes ^ nv == self.n_its(nodes)

    def test_sub(self):
        # print("G - H nodes:", gnv - hnv)
        nv = self.nv
        some_nodes = self.n_its(range(5, 12))
        assert nv - some_nodes == self.n_its(range(5))
        assert some_nodes - nv == self.n_its(range(9, 12))


class TestNodeDataViewSetOps(TestNodeViewSetOps):
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.G.nodes[3]["foo"] = "bar"
        cls.nv = cls.G.nodes.data("foo")

    def n_its(self, nodes):
        return {(node, "bar" if node == 3 else None) for node in nodes}


class TestNodeDataViewDefaultSetOps(TestNodeDataViewSetOps):
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.G.nodes[3]["foo"] = "bar"
        cls.nv = cls.G.nodes.data("foo", default=1)

    def n_its(self, nodes):
        return {(node, "bar" if node == 3 else 1) for node in nodes}

# Edges Data View
class TestEdgeDataView:
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.eview = sx.reportviews.EdgeView

    # NOTE: Not supported
    # def test_pickle(self):
    #     import pickle

    #     ev = self.eview(self.G)(data=True)
    #     pev = pickle.loads(pickle.dumps(ev, -1))
    #     assert list(ev) == list(pev)
    #     assert ev.__slots__ == pev.__slots__

    def modify_edge(self, G, e, **kwds):
        G.edges[e].update(kwds)

    def test_str(self):
        ev = self.eview(self.G)(data=True)
        rep = str([(n, n + 1, AttributeDict(self.G, (n, n+1))) for n in range(8)])
        assert str(ev) == rep

    def test_repr(self):
        ev = self.eview(self.G)(data=True)
        ad = "AttributeDict({})"
        rep = (
            "EdgeDataView([(0, 1, {}), (1, 2, {}), ".format(ad, ad)
            + "(2, 3, {}), (3, 4, {}), ".format(ad, ad)
            + "(4, 5, {}), (5, 6, {}), ".format(ad, ad)
            + "(6, 7, {}), (7, 8, {})])".format(ad, ad)
        )
        assert repr(ev) == rep

    def test_iterdata(self):
        G = self.G.copy()
        evr = self.eview(G)
        ev = evr(data=True)
        ev_def = evr(data="foo", default=1)

        for u, v, d in ev:
            pass
        assert d == {}

        for u, v, wt in ev_def:
            pass
        assert wt == 1

        self.modify_edge(G, (2, 3), foo="bar")
        for e in ev:
            assert len(e) == 3
            if set(e[:2]) == {2, 3}:
                assert e[2] == {"foo": "bar"}
                checked = True
            else:
                assert e[2] == {}
        assert checked

        for e in ev_def:
            assert len(e) == 3
            if set(e[:2]) == {2, 3}:
                assert e[2] == "bar"
                checked_wt = True
            else:
                assert e[2] == 1
        assert checked_wt

    def test_iter(self):
        evr = self.eview(self.G)
        ev = evr()
        for u, v in ev:
            pass
        iev = iter(ev)
        assert next(iev) == (0, 1)
        assert iter(ev) != ev
        assert iter(iev) == iev

    def test_contains(self):
        evr = self.eview(self.G)
        ev = evr()
        if self.G.is_directed():
            assert (1, 2) in ev and (2, 1) not in ev
        else:
            assert (1, 2) in ev and (2, 1) in ev
        assert not (1, 4) in ev
        assert not (1, 90) in ev
        assert not (90, 1) in ev

    def test_len(self):
        evr = self.eview(self.G)
        ev = evr(data="foo")
        assert len(ev) == 8
        assert len(evr(1)) == 2
        assert len(evr([1, 2, 3])) == 4

        assert len(self.G.edges(1)) == 2
        assert len(self.G.edges()) == 8
        assert len(self.G.edges) == 8

        H = self.G.copy()
        H.add_edge(1, 1)
        assert len(H.edges(1)) == 3
        assert len(H.edges()) == 9
        assert len(H.edges) == 9

# Edge Views
class TestEdgeView:
    @classmethod
    def setup_class(cls):
        cls.G = sx.path_graph(9)
        cls.eview = sx.reportviews.EdgeView

    # NOTE: Not supported
    # def test_pickle(self):
    #     import pickle

    #     ev = self.eview(self.G)
    #     pev = pickle.loads(pickle.dumps(ev, -1))
    #     assert ev == pev
    #     assert ev.__slots__ == pev.__slots__

    def modify_edge(self, G, e, **kwds):
        G._adj[e[0]][e[1]].update(kwds)

    def test_str(self):
        ev = self.eview(self.G)
        rep = str([(n, n + 1) for n in range(8)])
        assert str(ev) == rep

    def test_repr(self):
        ev = self.eview(self.G)
        rep = (
            "EdgeView([(0, 1), (1, 2), (2, 3), (3, 4), "
            + "(4, 5), (5, 6), (6, 7), (7, 8)])"
        )
        assert repr(ev) == rep

    def test_call(self):
        ev = self.eview(self.G)
        assert id(ev) == id(ev())
        assert id(ev) == id(ev(data=False))
        assert id(ev) != id(ev(data=True))
        assert id(ev) != id(ev(nbunch=1))

    def test_data(self):
        ev = self.eview(self.G)
        assert id(ev) != id(ev.data())
        assert id(ev) == id(ev.data(data=False))
        assert id(ev) != id(ev.data(data=True))
        assert id(ev) != id(ev.data(nbunch=1))

    def test_iter(self):
        ev = self.eview(self.G)
        for u, v in ev:
            pass
        iev = iter(ev)
        assert next(iev) == (0, 1)
        assert iter(ev) != ev
        assert iter(iev) == iev

    def test_contains(self):
        ev = self.eview(self.G)
        edv = ev()
        if self.G.is_directed():
            assert (1, 2) in ev and (2, 1) not in ev
            assert (1, 2) in edv and (2, 1) not in edv
        else:
            assert (1, 2) in ev and (2, 1) in ev
            assert (1, 2) in edv and (2, 1) in edv
        assert not (1, 4) in ev
        assert not (1, 4) in edv
        # edge not in graph
        assert not (1, 90) in ev
        assert not (90, 1) in ev
        assert not (1, 90) in edv
        assert not (90, 1) in edv

    def test_len(self):
        ev = self.eview(self.G)
        num_ed = 9 if self.G.is_multigraph() else 8
        assert len(ev) == num_ed

        H = self.G.copy()
        H.add_edge(1, 1)
        assert len(H.edges(1)) == 3 + H.is_multigraph() - H.is_directed()
        assert len(H.edges()) == num_ed + 1
        assert len(H.edges) == num_ed + 1

    def test_and(self):
        # print("G & H edges:", gnv & hnv)
        ev = self.eview(self.G)
        some_edges = {(0, 1), (1, 0), (0, 2)}
        if self.G.is_directed():
            assert some_edges & ev, {(0, 1)}
            assert ev & some_edges, {(0, 1)}
        else:
            assert ev & some_edges == {(0, 1), (1, 0)}
            assert some_edges & ev == {(0, 1), (1, 0)}
        return

    def test_or(self):
        # print("G | H edges:", gnv | hnv)
        ev = self.eview(self.G)
        some_edges = {(0, 1), (1, 0), (0, 2)}
        result1 = {(n, n + 1) for n in range(8)}
        result1.update(some_edges)
        result2 = {(n + 1, n) for n in range(8)}
        result2.update(some_edges)
        assert (ev | some_edges) in (result1, result2)
        assert (some_edges | ev) in (result1, result2)

    def test_xor(self):
        # print("G ^ H edges:", gnv ^ hnv)
        ev = self.eview(self.G)
        some_edges = {(0, 1), (1, 0), (0, 2)}
        if self.G.is_directed():
            result = {(n, n + 1) for n in range(1, 8)}
            result.update({(1, 0), (0, 2)})
            assert ev ^ some_edges == result
        else:
            result = {(n, n + 1) for n in range(1, 8)}
            result.update({(0, 2)})
            assert ev ^ some_edges == result
        return

    def test_sub(self):
        # print("G - H edges:", gnv - hnv)
        ev = self.eview(self.G)
        some_edges = {(0, 1), (1, 0), (0, 2)}
        result = {(n, n + 1) for n in range(8)}
        result.remove((0, 1))
        assert ev - some_edges, result

