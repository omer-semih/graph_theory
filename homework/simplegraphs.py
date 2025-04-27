# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Additional modifications by Ömer Faruk Semih


# Problem 1
#
# Write a function odd_vertices(n, edges) that returns
# the list of odd-degree vertices sorted in ascending order.
# The degree of a vertex is the number of edges incident
# to that vertex.
# Argument n specifies that the graph has n>0 vertices
# numbered from 0 to n-1. Argument edges is a list of pairs of
# vertices denoting undirected edges. If vertex i is connected
# to vertex j, then edges contains either the pair (i,j) or
# the pair (j,i). If a vertex does not appear in any edge, it is
# an isolated vertex and thus has degree 0 (which is even).
# If a pair appears multiple times in edges (in either order),
# this means the corresponding vertices are linked multiple times.
# A loop of the form (i,i) contributes 2 to the degree of vertex i.
def odd_vertices(n, edges):

    degrees = [0]*n  # list to keep track of the degree of each vertex
    for edge in edges:
        # increment degree for both vertices
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    # collect vertices with odd degrees and sort them
    return sorted([i for i in range(n) if degrees[i] % 2 == 1])


# Problem 2
#
# Write a function is_simple(n, edges) that decides whether
# an undirected graph is simple.
# Argument n specifies that the graph has n>0 vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges. If vertex i is connected to
# vertex j, then edges contains either the pair (i,j) or
# the pair (j,i). If a pair appears multiple times in edges
# (in any order), this means the corresponding vertices are linked
# multiple times.
# A graph is simple if no two vertices are connected more than
# once, and the graph has no loop of the form (i,i).
# The function should return True if the graph is simple, and
# False otherwise.
def is_simple(n, edges):
    seen = set()  # store the edges we have already seen
    for u, v in edges:
        if u == v:  # if there's a self loop , graph is not simple
            return False
        edge = tuple(sorted((u, v)))  # normalize the edge order
        if edge in seen:  # if edge already exists , graph is not simple
            return False
        seen.add(edge)  # mark this edge as seen

    return True  # if we reach here , graph is simple


# Problem 3
#
# Write a function is_connected(n,edges) that decides
# whether an undirected graph is connected (i.e. there exists
# a path between any two vertices).
# Argument n specifies that the graph has n>0 vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges (if vertex i is connected to
# vertex j, then edges contains either the pair (i,j) or the
# pair (j,i)).
# The function should return True if the graph is connected,
# or False otherwise.
def is_connected(n, edges):
    assert n > 0  # make sure there's at least one vertex
    adj = {i: [] for i in range(n)}  # create adjacency list

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False]*n  # track visited vertices

    # recursive function for depth first search
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)

    return all(visited)  # check if all vertices are visited


# Problem 4
#
# Write a function is_edge_connected(n,edge) that decides
# whether an undirected graph is edge-connected (i.e. any two
# edges can be part of a common path).
# Argument n specifies that the graph has n>0 vertices numbered
# from 0 to n-1. Argument edges is a list of pairs of vertices
# denoting undirected edges (if vertex i is connected to
# vertex j, then edges contains either the pair (i,j) or the
# pair (j,i)).
# The function should return True if the graph is edge-connected,
# or False otherwise.
def is_edge_connected(n, edges):
    assert n > 0

    for e in edges:
        assert type(e) is tuple

    if not edges:  # no edges means edge-connected
        return True

    nodes_in_edges = set()
    for u, v in edges:  # collect all nodes that are part of some edge
        nodes_in_edges.add(u)
        nodes_in_edges.add(v)

    node_mapping = {node: idx for idx, node in enumerate(
        nodes_in_edges)}  # reindex nodes starting from zero
    k = len(nodes_in_edges)  # new number of nodes

    new_edges = [(node_mapping[u], node_mapping[v])
                 for (u, v) in edges]  # new edge-list with new indices

    return is_connected(k, new_edges)  # check if the new graph is connected
