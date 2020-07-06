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
        expected_data = [f"{n}: {repr(AttributeDict(self.G, n))}" for n in range(9)]
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


