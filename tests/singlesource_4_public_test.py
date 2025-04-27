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


def shortest_path(n, edges, src, dst):
    return homework.singlesource.shortest_path(n, shuffle_list(edges), src, dst)


class Problem4Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["singlesource"], import_exception)

    def test_1_public(self):
        # no path from 5 to 0

        edges = [(0, 1, 1), (0, 3, 1), (0, 4, 4),
                 (1, 2, 2), (1, 4, 3),
                 (2, 5, 1), (3, 4, 2),
                 (4, 5, -2), (5, 2, -1)]
        self.assertEqual(None, shortest_path(6, edges, 5, 0))


if __name__ == '__main__':
    unittest.main()
