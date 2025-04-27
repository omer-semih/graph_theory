import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math import inf
from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.gt import eccentricity
except Exception as e:
    print(e)
    import_exception = e



class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["gt"], import_exception)

    def test_1_public(self):
        self.assertEqual(2, eccentricity(5, shuffle_list([(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 2), (0, 3)]), 0))

    def test_2_public(self):
        self.assertEqual(inf, eccentricity(5, shuffle_list([(1, 2), (0, 0), (3, 0), (1, 4), (4, 2)]), 4))


if __name__ == '__main__':
    unittest.main()
