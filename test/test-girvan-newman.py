import sys
import unittest

import snap

class TestCommunityGirvanNeuman(unittest.TestCase):

    def test_CommunityGirvanNewman(self):

        Rnd = snap.TRnd(42)
        Graph = snap.GenPrefAttach(100, 10, Rnd)
        exp_val = 0.00963802805072646

        Vec = snap.TCnComV()
        act_val = snap.CommunityGirvanNewman(Graph, Vec)
        self.assertAlmostEqual(exp_val, act_val)

        Vec = snap.TCnComV()
        act_val = snap.CommunityGirvanNewman(Graph, Vec)
        self.assertAlmostEqual(exp_val, act_val)

        Vec = snap.TCnComV()
        act_val = snap.CommunityGirvanNewman(Graph, Vec)
        self.assertAlmostEqual(exp_val, act_val)

if __name__ == '__main__':

    unittest.main()

