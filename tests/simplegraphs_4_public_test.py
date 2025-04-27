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




def is_edge_connected(n, edges):
    return homework.simplegraphs.is_edge_connected(n, shuffle_list(edges))


class Problem4Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["simplegraphs"], import_exception)

    def test_1_public(self):
        self.assertIs(True, is_edge_connected(5, [(0, 1), (4, 1), (3, 0), (3, 1)]))

    def test_2_public(self):
        self.assertIs(False, is_edge_connected(5, [(0, 1), (2, 1), (2, 0), (4, 3)]))

    def test_3_public(self):
        self.assertTrue(is_edge_connected(1, [(0, 0)]))

    def test_4_public(self):
        self.assertFalse(is_edge_connected(4, [(0, 1), (3, 2)]))

    def test_5_public(self):
        self.assertTrue(is_edge_connected(4, [(2, 2)]))

    def test_6_public(self):
        self.assertTrue(is_edge_connected(4, [(2, 1)]))

    def test_7_public(self):
        self.assertTrue(is_edge_connected(1, []))

    def test_8_public(self):
        self.assertTrue(is_edge_connected(3, []))

    def test_9_public(self):
        self.assertTrue(is_edge_connected(12, []))


if __name__ == '__main__':
    unittest.main()
