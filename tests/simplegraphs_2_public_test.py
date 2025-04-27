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



def is_simple(n, edges):
    return homework.simplegraphs.is_simple(n, shuffle_list(edges))


class Problem2Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["simplegraphs"], import_exception)

    def test_1_public(self):
        #  Königsberg 7 bridges
        self.assertIs(False,
                      is_simple(4, [(0, 2), (2, 3), (3, 0), (2, 0), (2, 1), (3, 1), (1, 2)]))

    def test_2_public(self):
        self.assertIs(True,
                      is_simple(5, [(0, 1), (1, 2), (3, 2), (0, 3), (2, 0), (1, 3), (4, 1), (4, 2)]))


if __name__ == '__main__':
    unittest.main()
