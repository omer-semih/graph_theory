import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math import inf
from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.gt import distance
except Exception as e:
    print(e)
    import_exception = e


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["gt"], import_exception)

    def test_1_public(self):
        g = shuffle_list([(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 2)])
        d = distance(5, g, 3, 4)
        self.assertEqual(2, d,
                         f"expecting distance=2 from 3 to 4 in graph {g}")

    def test_2_public(self):
        g = shuffle_list([(1, 2), (0, 0), (3, 0), (1, 4), (4, 2)])
        d = distance(5, g, 4, 3)
        self.assertEqual(inf, d,
                         f"expecting distance=inf from 4 to 3 in {g=}")


if __name__ == '__main__':
    unittest.main()
