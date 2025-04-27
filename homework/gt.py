# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Problem 1
#
# Write a function eccentricity(n,edge,i) that compute the
# eccentricity of vertex i.
# Argument n specifies that the DIRECTED graph has n>0 vertices
# numbered from 0 to n-1. Argument edges is a list of pairs of
# vertices denoting directed edges. If vertex i has an outgoing
# edge going to vertex j, then edges contains the pair (i,j).
# The distance dist(i,j) between two vertices i and j is the
# minimum number of edges of paths that connect i to j. If i=j,
# their distance is 0. The eccentricity of vertex i is the maximum
# distance dist(i,j) to all other vertices j. If the graph is
# not connected, the eccentricity of all vertices is math.inf.
def eccentricity(n, edges, i):
    raise NotImplementedError()


# Problem 2
#
# Write a function distance(n,edge,i,j) that compute the
# distance between vertices i and j.
# Argument n specifies that the graph has n>0 vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges. If vertex i is connected to vertex j,
# then edge contains either the pair (i,j) or the pair (j,i).
# If a pair appears multiple time in edge (in any order), it means
# the corresponding vertices are linked multiple times.
# The distance between two vertices i and j is the minimum number
# of edges of paths that connect i to j. If i=j, their distance
# is 0, and if the two vertices are not connected, their distance
# should be returned as math.inf.
def distance(n, edges, i, j):
    raise NotImplementedError()


