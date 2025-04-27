import sys
import os
import unittest

# testing is_augmenting_path

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.matchings
except Exception as e:
    print(e)
    import_exception = e


def is_augmenting_path(n, edges, matching1, path):
    return homework.matchings.is_augmenting_path(n, shuffle_list(edges), shuffle_list(matching1), path)


class Problem4Public(ThegTestCase):

    def is_augmenting_path(self, parity, n, edges, matching, path):
        edges = shuffle_list(edges)
        matching = shuffle_list(matching)

        if parity:
            self.assertTrue(homework.matchings.is_augmenting_path(n, edges, matching, path),
                            f"{path} is an augmenting path of {n=}, {edges=}, {matching=}")
        else:
            self.assertFalse(homework.matchings.is_augmenting_path(n, edges, matching, path),
                             f"{path} is NOT an augmenting path of {n=}, {edges=}, {matching=}")

    def test_code_check(self):
        self.code_check(["matchings"], import_exception)

    def test_1_public(self):
        self.is_augmenting_path(True, 4,
                                [(0, 1), (1, 2), (2, 3), (0, 3)],
                                [(1, 0)],
                                [3, 0, 1, 2])

    def test_2_public(self):
        self.is_augmenting_path(False, 4,
                                [(0, 1), (1, 2), (2, 3), (3, 0)],
                                [(0, 1), (3, 2)],
                                [1, 3])

    def test_3_public(self):
        self.is_augmenting_path(False, 4,
                                [(0, 1), (1, 2), (2, 3)],
                                [(0, 1)],
                                [])

    def test_4_public(self):
        # odd length path is certainly not an alternating path
        self.is_augmenting_path(False, 4, [(0, 1), (1, 2), (2, 3)],
                                [(0, 1)],
                                [1])

    def test_5_public(self):
        # path contains a non-vertex
        self.is_augmenting_path(False, 4, [(0, 1), (1, 2), (2, 3)],
                                [(0, 1)],
                                [1, 8])

    def test_6_public(self):
        # path contains isolated vertex
        self.is_augmenting_path(False, 10, [(0, 1), (1, 2), (2, 3)],
                                [(0, 1)],
                                [1, 8])

    def test_7_public(self):
        # path contains v[k], v[k+1] which is not an edge
        self.is_augmenting_path(False, 10, [(0, 1), (1, 2), (2, 3)],
                                [(0, 1)],
                                [3, 0])


if __name__ == '__main__':
    unittest.main()
