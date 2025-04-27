# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from lecture.rubik import *
from typing import List, Optional


# initial order        face indices                 face names
#    +--+                 +-----+                    +----+
#    |RR|                 |20 21|                    | U  |
#    |RR|                 |22 23|                    |    |
# +--+--+--+--+     +-----+-----+----+-----+    +----+----+----+----+
# |BB|WW|GG|YY|     |12 13| 0 1 | 4 5| 8  9|    | L  | F  | R  | B  |
# |BB|WW|GG|YY|     |14 15| 2 3 | 6 7|10 11|    |    |    |    |    |
# +--+--+--+--+     +-----+-----+----+-----+    +----+----+----+----+
#    |OO|                 |16 17|                    | D  |
#    |OO|                 |18 19|                    |    |
#    +--+                 +-----+                    +----+
#
# A cube is represented by a string of 24 characters.  Each character is
# the initial of the color of one face, ordered as above.
# However, as an optimization, we use an integer rather than array,
#  i.e. an integer interpreted in base 6, whose kth digit is 0, 1, ...5
#  according to cubeColors (defined below).


def solve_cube(cube: str, twists: List[str]) -> Optional[List[str]]:
    """Given a string of length 24 such as
    'BWYRBBRGROYGGGYBYOWOWOWR' representing the stickers on each side of
    the 2x2 Rubik's cube, return a list of strings representing
    twists which can be made in the order returned, to solve
    the cube.  The number of twists in the returned list must
    be minimum.  E.g., if you return a list of length 8, it will
    be considered incorrect if there exists a list of length 7 (or
    fewer) which also solves the cube with the given twists.
    Only twists given in `twists` are allowed to be used to
    solve the cube.
    E.g., if ["R2", "L-", "U+"] is returned,
    then the cube can be solved by "R2" followed by
    "L-", and then by "U+".
    If no solution is found, return None, however this
    should never happen, unless the given cube does not
    really describe a possible initial cube state, of
    if the cube cannot be solved using twists given in `twists`.

    If the cube is already solved, return the empty list, [].

    You are free to do this any way you can, provided the solution
    works in the docker image in which the code will be auto-tested.
    However, the most straightforward solution would be to use
    the API provided in lecture.rubik:
      cubeToInt() -- convert string such as 'BWYRBBRGROYGGGYBYOWOWOWR', to int
          whose base-6 representation represents the cube.
      rotateCube() -- return a new cube (int) after performing exactly one twist
      solved() -- determines whether the given cube (int) is in a solved state
    """
    assert isinstance(cube, str)
    c0 = cubeToInt(cube)
    raise NotImplementedError()


if __name__ == '__main__':
    cube, twists = shuffleCube(8, rotations9)
    print(f"{twists=}")
    print(f"{cube=}")
    solution = solve_cube(cube, rotations9)
    print(f"{solution=}")
    c = cubeToInt(cube)
    for twist in solution:
        c = rotateCube(c, twist)
        print(f"{twist} -> {cubeToStr(c)}")
