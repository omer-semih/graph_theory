# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# In all exercises after this note, the graph is assumed
# to be:
#  --- a simple graph (i.e., no self-loops and at most one edge
#     between any two given vertices)
#  --- with at least one vertex,
#  --- with zero or more edges,
#  --- and edges should be interpreted as UNDIRECTED.

# A helper function. Feel free to use or ignore.
def nedge(edge):
    """Normalize an edge into increasing order of vertices"""
    a, b = edge
    if a < b:
        return a, b
    else:
        return b, a


# Problem 1
#
# Detect matching:
# You must implement a function that takes list of edges and
# determines whether it is a matching.
# You must implement the function is_matching(n,edges,pairs).
#   --- n is number of vertices, numbered 0 through n-1
#   --- edges is a valid list of UNDIRECTED edges.
#   --- pairs is a list of pairs of integers, warning there is
#        no guarantee that they correspond to actual edges.
# Your function must return True if the list pairs designates
# a valid matching for the graph, and must return False otherwise.
def is_matching(n, edges, matching):
    raise NotImplementedError()


# Problem 2
#
# Detect maximal matching
# You must implement a function that takes list of edges and
# determines whether it designates a maximal matching.
# You must implement the function
# is_maximal_matching(n,edges,pairs).
#   --- n is number of vertices, numbered 0 through n-1
#   --- edges is a valid list of UNDIRECTED edges.
#   --- pairs is a list of pairs of integers, warning there is
#        no guarantee they are edges.
# Your function must return True if the list pairs designates
# a maximal matching for the graph, and must return False otherwise.
def is_maximal_matching(n, edges, matching):
    raise NotImplementedError()


# Problem 3
#
# Detect perfect matching
# You must implement a function that takes list of edges and
# determines whether it designates a perfect matching.
# You must implement the function is_perfect_matching(n,edges,pairs).
#   --- n is number of vertices, numbered 0 through n-1
#   --- edges is a valid list of UNDIRECTED edges.
#   --- pairs is a list of pairs of integers, warning there is
#        no guarantee they correspond to actual edges.
#
# Your function must return True if the list pairs designates
# a perfect matching for the graph, and must return False otherwise.
def is_perfect_matching(n, edges, matching):
    raise NotImplementedError()


# Problem 4
#
# Detect augmenting path
# You must implement a function that takes list of edges, valid
# matching, and a proposed path. Your task is to determine
# whether the proposed path is a valid path which designates
# an augmenting path with respect to the matching.
# You must implement the function
#    is_augmenting_path(n,edges,matching,path).
#  --- n is number of vertices, numbered 0 through n-1
#  --- edges is a valid list of UNDIRECTED edges.
#  --- matching is a valid matching
#  --- path is a list of integers (not a list of edges); warning
#       there is no guarantee they are vertices.   If any of
#       these integers is not a vertex, return False.
# Your function must return True if the list designates an
# alternating path with respect to the matching, and must
# return False otherwise.
# Note, that you do not need to validate edges nor matching,
# but you do need to validate path.
def is_augmenting_path(n, edges, matching, path):
    raise NotImplementedError()


# Problem 5
#
# Generate augmenting path
# Note this exercise is considered difficult, and consequently it
# is more points than the other exercises.
# In this exercise you will be given an UNDIRECTED graph including
# a valid set of edges and a valid matching.
# You do not need to validate the edges, nor the matching.
# Your task is to implement a function
# find_augmenting_path(n,edges,matching) which will return
# None if there is no augmenting path, or return such a path in
# the form of a LIST OF VERTICES, not a list of edges.
#   --- n is number of vertices, numbered 0 through n-1
#   --- edges is a valid list of UNDIRECTED edges.
#   --- matching is a valid matching
# Note that in some cases there are many possible augmenting
# paths.   You may return any one of them.
def find_augmenting_path(n, edges, matching):
    raise NotImplementedError()


# Problem 6
#
# XOR edges
# Given two valid lists of edges, return an XOR of the two edge
# lists.  I.e., return a maximum possible sized list of graph
# edges which are either in one of the given lists or the other
# but not in both.
# The list your function returns is not allowed to contain
# duplicates.  For example the invalid return value
# [(1,2),(0,1),(1,2)] contains a duplicate, and so
# does [(1,2),(0,1),(2,1)].
# You must implement the function: xor_edges(edges1,edges2)
#   --- edges1 - A list of pairs of valid vertices,
#   --- edges2 - A list of pairs of valid vertices,
# You may assume that neither of the given matchings contains
# duplicate edges.  For example edges1 never equals [(1,2),(1,2)],
# [(1,2),(2,1)],  nor [(1,2),(2,3),(2,1)].
# You may also assume that every integer mentioned in either
# of the given matchings is a valid vertex.
def xor_edges(edges1, edges2):
    raise NotImplementedError()


# Problem 7
#
# Generate maximum matching
#
# Your task is to write a function find_maximum_matching(n,edges)
# which will generate and return a maximum matching for the graph.
# Your function should return a list of edges, i.e. a list of
# pairs of vertices.
#   --- n is number of vertices, numbered 0 through n-1
#   --- edges is a valid list of UNDIRECTED edges.
# Remember, that in this exercise the matching you return
# is a list of edges, i.e., a list of pairs of vertices.
# In a previous exercise you returned a path as a list of vertices.
# Also remember that the function should never return None.
# Why?  Because a maximum matching always exists.   If the graph
# has no edges, then the maximum matching is [], and if the graph
# has at least one edge, (a,b)  then at least one matching
# exists, namely [(a,b)].
# Important note: You can assume that a working implementation
# of the function  find_augmenting_path(n,edges,matching),
# specified in a previous exercise, is available.  So all you
# need to do here is update a matching using the
# result of find_augmenting_path until no more augmenting is found.
def find_maximum_matching(n, edges):
    # update matching from p
    # ...
    # repeat until no more augmenting path is found
    # ...
    raise NotImplementedError()


