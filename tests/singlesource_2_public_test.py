import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.singlesource
except Exception as e:
    print(e)
    import_exception = e


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["singlesource"], import_exception)

    def wrap(self, expected, n, edges, src):
        edges = shuffle_list(edges)
        distances = homework.singlesource.single_source_distances_undirected(n, edges, src)
        if expected is None:
            self.assertIs(None, distances, f"expected None, but got {distances} for {n=} {edges=} {src=}")
        else:
            self.assertEqual(expected, distances, f"expected {expected}, but got {distances}, for {n=} {edges=} {src=}")

    def test_1_public(self):
        edges = [(0, 1, 1), (2, 1, 2), (2, 0, 4)]
        self.wrap([0, 1, 3],
                  3, edges, 0)

    def test_2_public(self):
        # 0 -> 1 -> 0 is a negative weight cycle
        edges = [(0, 1, -1), (2, 1, 2), (2, 0, 4)]
        self.wrap(None,
                  3, edges, 0)

    def test_3_public(self):
        # 0 -> 1 -> 0 is a negative weight cycle
        edges = [(0, 1, 1), (2, 1, 2), (2, 0, 4), (1, 3, -10), (2, 3, 1)]
        self.wrap(None,
                  4, edges, 0)

    def test_4_public(self):
        # 0 -> 1 -> 0 is a negative weight cycle
        edges = [(0, 1, 1), (2, 1, 2), (2, 0, 4), (1, 3, 3), (2, 3, 1)]
        self.wrap([4, 3, 1, 0],
                  4, edges, 3)


if __name__ == '__main__':
    unittest.main()
