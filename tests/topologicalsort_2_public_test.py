import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.topologicalsort
except Exception as e:
    print(e)
    import_exception = e


def topological_sort(n, constraints):
    return homework.topologicalsort.topological_sort(n, shuffle_list(constraints))


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["topologicalsort"], import_exception)

    def test_1_private(self):
        constraints = [(3, 2), (4, 2), (4, 5), (8, 4), (6, 3), (6, 2), (8, 0),
                       (5, 0), (8, 5), (9, 8), (9, 3), (10, 2),
                       (10, 5), (10, 8), (10, 0), (1, 9), (1, 0), (7, 6),
                       (0, 7), (9, 10), (1, 8)]
        self.assertEqual(topological_sort(11, constraints),
                         [1, 9, 10, 8, 4, 5, 0, 7, 6, 3, 2])


if __name__ == '__main__':
    unittest.main()
