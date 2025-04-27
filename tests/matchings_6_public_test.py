import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.matchings
except Exception as e:
    print(e)
    import_exception = e

from tests.matchings_helper import SA_equal_matching


class Problem6Public(ThegTestCase):

    def wrap(self, edges1, edges2, matching):
        edges1 = shuffle_list(edges1)
        edges2 = shuffle_list(edges2)
        x = homework.matchings.xor_edges(edges1, edges2)
        self.assertTrue(SA_equal_matching(x, matching),
                        f"your computed xor={x} of {edges1=} {edges2=} is not equivalent to {matching=}")

    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def test_1_public(self):
        self.wrap([], [], [])

    def test_2_public(self):
        self.wrap([(1, 0), (2, 3)], [(1, 2), (3, 2)], [(1, 0), (1, 2)])

    def test_3_public(self):
        self.wrap([(1, 0), (2, 3)], [(1, 2), (3, 2)], [(1, 0), (1, 2)])


if __name__ == '__main__':
    unittest.main()
