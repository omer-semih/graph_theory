import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.matchings import find_maximum_matching
except Exception as e:
    print(e)
    import_exception = e

from tests.matchings_helper import SA_is_matching


class Problem7Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def wrap(self, n, edges, best_len):
        edges = shuffle_list(edges)
        best_matching = find_maximum_matching(n, edges)
        self.assertTrue(SA_is_matching(n, edges, best_matching),
                        f"You computed {best_matching} which is not a matching of {n=} {edges=}")
        self.assertEqual(best_len, len(best_matching),
                         f"a maximum matching of {n=} {edges=} should have length {best_len}. {n=} {edges=}")

    def test_1_public(self):
        edges_2_3 = [(1, 2), (1, 6), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 0), (5, 7), (5, 0), (6, 7), (7, 0)]
        self.wrap(8, edges_2_3, 4)

    def test_2_public(self):
        args1 = (18, [(0, 1), (1, 2), (2, 3), (2, 4), (3, 6), (4, 5), (5, 6), (6, 7),
                      (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (11, 13), (12, 14),
                      (13, 15), (14, 15), (15, 16), (16, 17)])
        self.wrap(*args1, 9)

    def test_3_public(self):
        self.assertEqual([], find_maximum_matching(1, []),
                         "maximum matching of n=1 edges=[] should be []")

    def test_4_public(self):
        n_adl = 17
        edges_adl = [(11, 12), (14, 3), (16, 12), (10, 5), (0, 8), (1, 4), (2, 15), (4, 14), (8, 13), (5, 9),
                     (7, 1), (14, 6), (13, 2), (15, 0), (5, 13), (12, 10), (6, 7), (9, 16), (0, 1)]
        self.wrap(n_adl, edges_adl, 8)


if __name__ == '__main__':
    unittest.main()
