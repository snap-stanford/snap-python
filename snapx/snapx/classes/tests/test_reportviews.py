import pytest

import snapx as sx
from snapx.classes.reportviews import NodeDataView

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



