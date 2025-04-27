import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import_exception = None
try:
    from homework.adjacencymatrix import count_k_step_walks
except Exception as e:
    print(e)
    import_exception = e

from tests.theg import ThegTestCase, shuffle_list


class Problem3Public(ThegTestCase):

    def test_code_check(self):
        self.code_check(["adjacencymatrix"], import_exception)

    def test_1_public(self):
        edges = shuffle_list([(1, 2), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])
        self.assertEqual(1, count_k_step_walks(6, 0, 1, 1, edges))

    def test_2_public(self):
        edges = shuffle_list([(0, 1), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)])
        self.assertEqual(3, count_k_step_walks(5, 2, 1, 1, edges))


if __name__ == '__main__':
    unittest.main()
