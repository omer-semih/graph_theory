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
from lightning.lightning import make_grid, make_maze, draw_maze, get_neighbors, solve_maze
from functools import reduce


class LightningCase(ThegTestCase):
    def test_1(self):
        self.assertTrue(True)

    def test_make_grid(self):
        self.assertTrue(make_grid(10, 20))

    def test_make_maze(self):
        self.assertTrue(make_maze(10, 20, 30, 40))

    def test_draw_maze(self):
        rows = 10
        cols = 18
        maze = make_maze(rows, cols, 50, 50)
        text = draw_maze(rows, cols, maze, [])
        print(f"{text}")
        self.assertTrue(draw_maze(10, 18, maze, []))

    def test_get_neighbors(self):
        rows = 5
        cols = 10
        maze = make_maze(rows, cols, 50, 26)
        print(draw_maze(rows, cols, maze, []))
        num_edges = reduce(lambda a, b: a + b,
                           [len(maze[row][col]) for row in range(rows)
                            for col in range(cols)])
        neighbors = [n for row in range(rows)
                     for col in range(cols)
                     for n in get_neighbors(row, col, rows, cols, maze)]
        self.assertEqual(num_edges * 2, len(neighbors))

    def test_solve_maze(self):
        rows = 60
        cols = 45
        path = []
        while not path:
            maze = make_maze(rows, cols,
                             horizontal_openness=75,
                             vertical_openness=25)
            grid = make_grid(rows, cols)
            path = solve_maze(rows, cols, maze, grid)
        if path:
            print(draw_maze(rows, cols, maze, path))
