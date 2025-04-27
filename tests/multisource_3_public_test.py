import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.multisource
except Exception as e:
    print(e)
    import_exception = e



import math


def floyd_warshall_3(n, edges, op_plus, e_plus, op_times, e_times):
    return homework.multisource.floyd_warshall_3(n, shuffle_list(edges), op_plus, e_plus, op_times, e_times)


def path(Succ, source, destination):
    return homework.multisource.path(Succ, source, destination)


class Problem3Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["multisource"], import_exception)

    def test_1_public(self):
        from tests.multisource_helper import evaluate_path_pa1, op_min, op_add
        n = 5
        edges = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, -1), (3, 4, 2)]
        self.assertEqual(True, evaluate_path_pa1(n, edges, op_min, math.inf, op_add, 0, floyd_warshall_3, path))


if __name__ == '__main__':
    unittest.main()
