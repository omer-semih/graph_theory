import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.topologicalsort
except Exception as e:
    print(e)
    import_exception = e



def is_topological_order(n, constraints, permutation):
    return homework.topologicalsort.is_topological_order(n, shuffle_list(constraints), permutation)


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["topologicalsort"], import_exception)

    def test_1_private(self):
        self.assertTrue(is_topological_order(4, [(1, 3), (1, 2)], [0, 1, 3, 2]))

    def test_2_private(self):
        self.assertFalse(is_topological_order(4, [(1, 3), (1, 2)], [0, 3, 1, 2]))


if __name__ == '__main__':
    unittest.main()
