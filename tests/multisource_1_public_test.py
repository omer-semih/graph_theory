import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.multisource
except Exception as e:
    print(e)
    import_exception = e




def connected_to(n, edges, src):
    return homework.multisource.connected_to(n, shuffle_list(edges), src)


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["multisource"], import_exception)

    def test_1_public(self):
        # Input
        n = 4
        edges = [(0, 1), (1, 1), (1, 2)]
        src = 2
        # connected_to(n,edges,src)
        # Should return 
        # [0,1,2] or any permutation thereof

        self.assertEqual([0, 1, 2], sorted(connected_to(n, edges, src)))


if __name__ == '__main__':
    unittest.main()
