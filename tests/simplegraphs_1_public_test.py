import sys
import os

import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    import homework.simplegraphs
except Exception as e:
    print(e)
    import_exception = e




def odd_vertices(n, edges):
    return homework.simplegraphs.odd_vertices(n, shuffle_list(edges))


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["simplegraphs"], import_exception)

    def test_1_public(self):
        self.assertEqual([0, 3],
                         odd_vertices(4, [(0, 3), (3, 2), (1, 2), (3, 1)]))

    def test_2_public(self):
        self.assertEqual([],
                         odd_vertices(3, [(1, 1)]))


if __name__ == '__main__':
    unittest.main()
