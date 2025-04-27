import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.euleriancycles import is_eulerian
except Exception as e:
    print(e)
    import_exception = e




class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["euleriancycles"], import_exception)

    def test_1_public(self):
        self.assertIs(True,
                      is_eulerian(5, shuffle_list([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
                                              (3, 1), (4, 1), (3, 2), (2, 4), (4, 3)])))

    def test_2_public(self):
        self.assertIs(False,
                      is_eulerian(4, shuffle_list([(0, 2), (2, 3), (3, 0), (2, 0), (2, 1), (3, 1), (1, 2)])))

    def test_3_public(self):
        self.assertIs(True, is_eulerian(4, []))


if __name__ == '__main__':
    unittest.main()
