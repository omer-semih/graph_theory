# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys
import os

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.theg import ThegTestCase
from lecture.rubik import *


class RubikCase(ThegTestCase):
    def test_getDigit(self):
        self.assertEqual(getDigit(3 + 4 * 6 + 5 * 6 * 6, 0), 3)
        self.assertEqual(getDigit(3 + 4 * 6 + 5 * 6 * 6, 1), 4)
        self.assertEqual(getDigit(3 + 4 * 6 + 5 * 6 * 6, 2), 5)

    def test_getDigit2(self):
        for d1 in range(6):
            for position in range(24):
                d2 = getDigit(cubeInitSolved, position)
                cube1 = setDigit(cubeInitSolved, position, d1)
                self.assertEqual(getDigit(cube1, position), d1)
                cube2 = setDigit(cube1, position, d2)
                self.assertEqual(getDigit(cube2, position), d2)
                self.assertEqual(cube2, cubeInitSolved)

    def test_inverses(self):
        for x, y in inverses:
            self.assertEqual(cubeInitSolved, rotateCube(rotateCube(cubeInitSolved, x), y))
            self.assertEqual(cubeInitSolved, rotateCube(rotateCube(cubeInitSolved, y), x))

    def test_r2(self):
        for r2, rp, rm in [('L2', 'L+', 'L-'),
                           ('R2', 'R+', 'R-'),
                           ('U2', 'U+', 'U-'),
                           ('D2', 'D+', 'D-'),
                           ('F2', 'F+', 'F-'),
                           ('B2', 'B+', 'B-')]:
            # assert that L2 rotation is the same as twice L+ and same as twice L-
            # same for R2, U2, D2, F2 and B2
            self.assertEqual(rotateCube(cubeInitSolved, r2), rotateCube(rotateCube(cubeInitSolved, rp), rp))
            self.assertEqual(rotateCube(cubeInitSolved, r2), rotateCube(rotateCube(cubeInitSolved, rm), rm))

    def test_cycles(self):
        for rotation in rotationCycles:
            #                F       R         B        L        D        U
            c1 = cubeToInt("WWWW" + "GGGG" + "YYYY" + "BBBB" + "OOOO" + "RRRR")
            c1 = rotateCube(c1, rotation)
            digits = foldRightDigits(c1, 24, 6,
                                     [], lambda acc, digit: acc + [digit])
            # now assert that there are 4 of each digit
            for d in range(6):
                self.assertEqual(4, digits.count(d))
