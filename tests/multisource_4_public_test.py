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



from tests.multisource_helper import evaluate_safest_path_random


def safest_path(n, edges, source, destination):
    return homework.multisource.safest_path(n, shuffle_list(edges), source, destination)


class Problem4Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["multisource"], import_exception)

    def test_1_public(self):
        # from tests.multisource_helper import evaluate_safest_path_random_ex4
        for _ in range(10):
            self.assertTrue(evaluate_safest_path_random(safest_path))

    def test_2_public(self):
        g = (3, [(0, 1, 0.8), (1, 2, 0.5), (0, 2, 0.3)])

        self.assertEqual([0, 1, 2],
                         safest_path(*g, 0, 2))

    def test_3_public(self):
        g = (3, [(0, 1, 0.8), (1, 2, 0.5), (0, 2, 0.3)])
        self.assertEqual([1, 2],
                         safest_path(*g, 1, 2))

    def test_4_public(self):
        g = (3, [(0, 1, 0.8), (1, 2, 0.5), (0, 2, 0.3)])
        self.assertEqual([1],
                         safest_path(*g, 1, 1))

    def test_5_public(self):
        g = (3, [(0, 1, 0.8), (1, 2, 0.5), (0, 2, 0.3)])
        self.assertEqual([],
                         safest_path(*g, 2, 0))


if __name__ == '__main__':
    unittest.main()
