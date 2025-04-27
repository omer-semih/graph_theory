import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.matchings import is_maximal_matching
except Exception as e:
    print(e)
    import_exception = e


class Problem2Public(ThegTestCase):
    def wrap_is_maximal_matching(self, parity, n, edges, matching):
        edges = shuffle_list(edges)
        matching = shuffle_list(matching)

        if parity:
            self.assertTrue(is_maximal_matching(n, edges, matching),
                            f"{matching} is a maximal matching for {n=} {edges=}")
        else:
            self.assertFalse(is_maximal_matching(n, edges, matching),
                             f"{matching} is NOT a maximal matching for {n=} {edges=}")

    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def test_1_public(self):
        self.wrap_is_maximal_matching(True, 4, [(0, 1), (1, 2), (2, 3), (3, 0)],
                                      [(0, 1), (2, 3)])

    def test_2_public(self):
        # not a maximal matching because not a matching
        self.wrap_is_maximal_matching(False, 4,
                                      [(0, 1), (1, 2), (2, 3), (3, 0)],
                                      [(0, 1), (3, 2), (2, 3)])

    def test_3_public(self):
        self.wrap_is_maximal_matching(False, 4,
                                      [(0, 1), (1, 2), (2, 3), (3, 0)],
                                      [(0, 1), (2, 1)])


if __name__ == '__main__':
    unittest.main()
