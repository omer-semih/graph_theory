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




def floyd_warshall_2(n, edges, op_plus, e_plus, op_times, e_times):
    return homework.multisource.floyd_warshall_2(n, shuffle_list(edges), op_plus, e_plus, op_times, e_times)


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["multisource"], import_exception)

    def test_import_student(self):
        self.assertIsNone(import_exception, f"failed to import student python file: {import_exception}")

    def test_1_public(self):
        from math import inf
        from tests.multisource_helper import op_min, op_add
        n = 5
        edges = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, -1), (3, 4, 2)]
        self.assertEqual([[0, 1, 5, 4, 5],
                          [3, 0, 4, 3, 4],
                          [inf, inf, 0, inf, inf],
                          [inf, inf, 1, 0, 2],
                          [inf, inf, 0, -1, 0]],
                         floyd_warshall_2(n, edges, op_min, inf, op_add, 0))

    def test_2_public(self):
        from math import inf
        from tests.multisource_helper import op_min, op_max
        n = 5
        edges = [(0, 1, 7), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, 3), (3, 4, 2), (0, 3, 1)]
        self.assertEqual([[inf, 7, 1, 3, 4],
                          [3, inf, 1, 3, 4],
                          [0, 0, inf, 0, 0],
                          [0, 0, 1, inf, 2],
                          [0, 0, 1, 3, inf]],
                         floyd_warshall_2(n, edges, op_max, 0, op_min, inf))


if __name__ == '__main__':
    unittest.main()
