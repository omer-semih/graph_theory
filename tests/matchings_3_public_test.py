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


class Problem3Public(ThegTestCase):
    def is_perfect_matching(self, parity, n, edges, matching):
        edges = shuffle_list(edges)
        matching = shuffle_list(matching)
        if parity:
            self.assertTrue(homework.matchings.is_perfect_matching(n, edges, matching),
                            f"{matching} is a perfect matching of {n=} {edges=}")
        else:
            self.assertFalse(homework.matchings.is_perfect_matching(n, edges, matching),
                             f"{matching} is NOT a perfect matching of {n=} {edges=}")

    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def test_1_public(self):
        self.is_perfect_matching(False, 4,
                                 [(0, 1), (1, 2), (2, 3), (3, 0)],
                                 [(1, 2)])

    def test_2_public(self):
        self.is_perfect_matching(True, 4,
                                 [(0, 1), (1, 2), (2, 3), (3, 0)],
                                 [(0, 1), (3, 2)])

    def test_3_public(self):
        self.is_perfect_matching(False, 4,
                                 [(0, 1), (1, 2), (2, 3), (3, 0)],
                                 [(0, 1), (2, 3), (3, 2)])


if __name__ == '__main__':
    unittest.main()
