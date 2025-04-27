import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase, shuffle_list

import_exception = None
try:
    from homework.euleriancycles import is_eulerian_cycle, find_eulerian_cycle
except Exception as e:
    print(e)
    import_exception = e


class Problem1Public(ThegTestCase):
    def check_list_length(self, g0, found):
        self.assertTrue(found is None or isinstance(found, list), f"find_eulerian_cycle should return a list or None, (not {found}) when given {g0}")
        if isinstance(found, list):
            self.assertEqual(len(g0[1]), len(found), f"find_eulerian_cycle should return a list of length={len(g0[1])}, not length={len(found)}, when input is {g0}")

    def test_code_check(self):
        self.code_check(["euleriancycles"], import_exception)

    def test_1_public(self):
        g0 = (4, shuffle_list([(0, 1), (1, 2), (2, 3), (3, 0)]))
        found = find_eulerian_cycle(*g0)
        self.check_list_length(g0,found)
        self.assertIs(True, is_eulerian_cycle(*g0, found),
                      f"{found} is not an eulerian cycle of {g0=}")

    def test_0b_public(self):
        g0 = (6, shuffle_list([(0, 1), (1, 2), (2, 3), (0, 2)]))
        found = find_eulerian_cycle(*g0)
        self.check_list_length(g0,found)
        self.assertIs(None, found,
                      f"{found} is not an eulerian cycle of {g0=}")

    def test_2_public(self):
        g1 = (4, shuffle_list([(2, 0), (2, 1), (3, 1), (1, 2), (0, 2), (2, 3),
                               (3, 0), (3, 2), (0, 1), (0, 0)]))
        found = find_eulerian_cycle(*g1)
        self.check_list_length(g1,found)
        self.assertIs(True, is_eulerian_cycle(*g1, found),
                      f"{found} is not an eulerian cycle of {g1=}")


if __name__ == '__main__':
    unittest.main()
