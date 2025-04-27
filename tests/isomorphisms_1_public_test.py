import sys
import os

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase

import_exception = None
try:
    from homework.isomorphisms import is_isomorphism
except Exception as e:
    print(e)
    import_exception = e




class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["isomorphisms"], import_exception)

    def test_1_public(self):
        self.assertFalse(is_isomorphism(2, [], [(0, 1)], [0, 1]))

    def test_2_public(self):
        self.assertIs(True, is_isomorphism(1, [], [], [0]))

    def test_3_public(self):
        g1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        g2 = [(0, 3), (0, 2),
                                            (1, 3), (1, 4),
                                            (2, 4)]
        bij = [0, 2, 4, 1, 3]
        self.assertIs(True, is_isomorphism(5,
                                           g1,
                                           g2,
                                           bij),
                      f"{bij} is a bijection from {g1} to {g2}")
        g1 = []
        bij = [1]
        self.assertIs(False, is_isomorphism(1, g1, g1, bij),
                      f"{bij} is NOT a bijectection from {g1} to {g1}")
