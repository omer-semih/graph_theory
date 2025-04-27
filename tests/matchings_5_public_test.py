import sys
import os

# testing find_augmenting_path

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.matchings
except Exception as e:
    print(e)
    import_exception = e


def find_augmenting_path(n, edges, matching):
    edges = shuffle_list(edges)
    matching = shuffle_list(matching)
    path = homework.matchings.find_augmenting_path(n, edges, matching)
    if path is None:
        return None
    if homework.matchings.is_augmenting_path(n, edges, matching, path):
        return path
    return None


class Problem5Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def test_1_public(self):
        matching2 = [(1, 6), (2, 4), (7, 0), (5, 3)]
        edges_2_3 = [(1, 2), (1, 6), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 0), (5, 7), (5, 0), (6, 7), (7, 0)]
        self.assertIs(None, find_augmenting_path(8, edges_2_3, matching2))

    def test_2_public(self):
        p = find_augmenting_path(4, [(0, 1), (1, 2), (3, 2)], [(2, 1)])
        self.assertTrue(p == [0, 1, 2, 3] or p == [3, 2, 1, 0])

    def test_3_public(self):
        args4 = (18, [(0, 1), (1, 2), (2, 4), (2, 3), (3, 6), (4, 5), (5, 6), (6, 7),
                      (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (11, 13), (12, 14),
                      (14, 15), (13, 15), (15, 16), (16, 17)],
                 [(1, 2), (3, 6), (4, 5), (7, 8), (9, 10), (11, 13), (12, 14), (15, 16)])
        self.assertTrue(find_augmenting_path(*args4))

    def test_12_public(self):
        args = (6, [(0, 1), (1, 2), (0, 2), (3, 2), (3, 4), (4, 5), (5, 3), (5, 2)], [(0, 2), (5, 3)])
        n, edges, matching = args
        self.assertTrue(find_augmenting_path(*args))


if __name__ == '__main__':
    unittest.main()
