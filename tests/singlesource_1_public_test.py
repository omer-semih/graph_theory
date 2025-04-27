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




def find_path_distance(n, edges, path):
    return homework.singlesource.find_path_distance(n, shuffle_list(edges), path)


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["singlesource"], import_exception)

    def wrap(self, expected, n, edges, path):
        edges = shuffle_list(edges)
        p = homework.singlesource.find_path_distance(n, edges, path)
        self.assertEqual(expected, p, f"{expected=} got {p} for {n=} {edges=} {path=}")

    def test_1_public(self):
        edges = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3), (2, 5, 1), (3, 4, 2), (4, 5, -2), (5, 2, -1)]
        self.wrap(2, 6, edges,  [0, 4, 5])

    def test_2_public(self):
        edges = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3), (2, 5, 1), (3, 4, 2), (4, 5, -2), (5, 2, -1)]
        self.wrap(0, 6, edges,  [4])

    def test_3_public(self):
        edges = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3), (2, 5, 1), (3, 4, 2), (4, 5, -2), (5, 2, -1)]
        self.wrap(None, 6, edges,  [])


if __name__ == '__main__':
    unittest.main()
