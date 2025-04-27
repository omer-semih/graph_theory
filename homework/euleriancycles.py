from typing import Any, List, Tuple, Optional, Set

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Problem 1
#
# Write a function is_eulerian(n,edge) that decides if a graph
# is Eulerian.
# Argument n specifies that the graph has n vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges. If vertex i is connected to
# vertex j, then edge contains either the pair (i,j) or
# the pair (j,i). If a pair appears multiple times in edge
# (in any order), it means the corresponding vertices are
# linked multiple times.
# Edges of the form (i,i) ARE ALLOWED.
# The function should return True if the graph contains
# an Eulerian cycle (i.e., a cycle that visits each edge
# exactly once), and False otherwise. Note that a graph with
# no edge is Eulerian (an empty cycle will visit all edges).
def is_eulerian(n, edges):
    raise NotImplementedError()


# Problem 2
#
# Write a function find_eulerian_cycle(m,edges) that finds an
# Eulerian cycle in a graph if the graph is Eulerian.
#
# If there is no Eurlerian cycle, the function should return None.
#
# Argument m specifies that the graph has m vertices numbered
# from 0 to m-1. Argument edges is a list of pairs of vertices
# denoting undirected edges. If vertex i is connected to
# vertex j, then edges contains either the pair (i,j) or
# the pair (j,i). If a pair appears multiple times in edges
# (in any order), it means the corresponding vertices are
# linked multiple times.
# Edges of the form (i,i) ARE ALLOWED.
# Let's assume len(edges)=n.
# The function should return a list of vertex numbers
# [v0,v1,v2,...,vn-1] such that the n edges
# (v0,v1),(v1,v2),(v2,v3),...,(vn-2,vn-1),(vn-1,v0)
# form a cycle that visits each edge of the graph exactly once.
# For clarification, if there are n edges, then this function
# must return a list of length=n or None.
# The list might have repeated vertices.
# E.g, if len(edges)=12, then return a list of length 12,
# or else return None if no such cycle exists.
def find_eulerian_cycle(m, edges):
    if not edges:
        return []

    raise NotImplementedError()


# Problem 3
#
# Write a function is_eulerian_cycle(n,edge,cycle) that decides
# if a cycle is Eulerian, i.e., it visits each edge of the given
# graph exactly once.
#
# Argument n specifies that the graph has m vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges. If vertex i is connected to
# vertex j, then edge contains either the pair (i,j) or
# the pair (j,i). If a pair appears multiple time in edge
# (in any order), it means the corresponding vertices are
# linked multiple times.
# Edges of the form (i,i) ARE ALLOWED.
#
# Argument cycle is a list of m>=0 vertex numbers
# [v0,v1,v2,...,vm-1], a list of length=m, denoting a cycle consisting of m edges
# (v0,v1),(v1,v2),(v2,v3),...,(vm-2,vm-1),(vm-1,v0).
# Note that if the input graph contains multiple occurrences of
# some edge (i,j), then an Eulerian cycle must have as many
# occurrences of this edge.
#
# The function should return True if the given cycle is
# Eulerian and False otherwise.
#
# For clarification, an Eulerian cycle is a length of length = len(edges)
# consisting of vertices, each 0 <= v < n, possibly having some vertices
# repeating, and possibly omitting some vertices.
def is_eulerian_cycle(n, edges, cycle):
    assert is_eulerian(n, edges)

    raise NotImplementedError()


