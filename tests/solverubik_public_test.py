import sys
import os
import unittest

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase
from lecture.rubik import *

import_exception = None
try:
    from homework.solverubik import solve_cube
except Exception as e:
    print(e)
    import_exception = e
num_tests = 10


class Problem1Public(ThegTestCase):
    def test_code_check(self):
        self.code_check(["solverubik"], import_exception)

    def solve(self, n, rotations):
        cube, twists = shuffleCube(n, rotations)
        solution = solve_cube(cube, rotations)
        for twist in solution:
            self.assertTrue(twist in rotations,
                            f"{twist} in the proposed solution, but not in the valid rotations {rotations}")
        c = cubeToInt(cube)
        for twist in solution:
            c = rotateCube(c, twist)
        self.assertTrue(solved(c),
                        f"failed to solve cube after {len(twists)} twists: {twists}")

    def test_inverses(self):
        for (x, y) in inverses:
            rotations = [x, y]
            c = rotateCube(cubeInitSolved, x)
            solution = solve_cube(cubeToStr(c), rotations)
            self.assertEqual(solution, [y])

            c = rotateCube(cubeInitSolved, y)
            solution = solve_cube(cubeToStr(c), rotations)
            self.assertEqual(solution, [x])

    def test_degrees(self):
        for twist in degrees:
            degree = degrees[twist]
            c = rotateCube(cubeInitSolved, twist)
            # solution of R+ is [R+, R+, R+]
            solution = solve_cube(cubeToStr(c), [twist])
            self.assertEqual(solution, [twist] * (degree - 1))

    def test_0_public(self):
        for n in range(4):
            self.solve(n, ["R+"])

    def test_1_public(self):
        for _ in range(num_tests):
            self.solve(1, rotations9)
            self.solve(1, rotations6)

    def test_2_public(self):
        for _ in range(num_tests):
            self.solve(2, rotations9)
            self.solve(2, rotations6)

    def test_3_public(self):
        for _ in range(num_tests):
            self.solve(3, rotations9)
            self.solve(3, rotations6)


if __name__ == '__main__':
    unittest.main()
