# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Recall that v0, and v1, are called adjacent vertices in a
# simple graph if (v0, v1) is an edge.  A k-step walk is a sequence
# of pairwise adjacent vertices, [v0, v1, v2, ..., vk]
# (not necessarily all unique), and is said to trace a path
# from v0 to vk.
# For example if G is an undirected simple 3-vertex graph with
# edges {(0,1), (1,2)}, then [0] is a 0-step walk from 0 to 0;
# [0,1] is a 1-step walk from 0 to 1; [0,1,2] is a 2-step walk
# from 0 to 2; [0,1,0,1,2] is a 4-step walk from 0 to 2;
# and [0,1,2,1,0,1,2,1,2,1] is a 9-step walk from 0 to 1.
# Furthermore, [0,2] is not a walk at all, because (0,2) is not
# an edge.
# Write a function count_k_step_walks(n,k,v1,v2,edges) that
# finds the number of distinct k-step walks between two given
# vertices v1 and v2.
# * n is the number of vertices (n>=2)
# * k is the number of steps between the vertices in question
# * v1,v2 are two vertices, I.e., each is an integer between
#     0 and n-1 inclusive.
# * edges is a list of pairs, each pair indicates an undirected edge.
# For this question we are only concerned with simple graphs
# containing 2 vertices or more. I.e., no self loops, at most
# one edge between any two vertices, and all edges are undirected.
def count_k_step_walks(n, k, v1, v2, edges):
    for v in range(n):
        # the instructions promise that (v,v) is never in edges
        assert (v, v) not in edges, f"invalid edges given, contains ({v}, {v})"

    for a, b in edges:
        # the instructions claim that if (a,b) is in edges, then (b,a) is not
        assert (b, a) not in edges, f"invalid edges given, contains ({a},{b}) and ({b},{a})"

    for i in range(len(edges)):
        e = edges[i]
        # the instructions claim that e is not twice in edges
        assert all(e != edges[j] for j in range(i+1, len(edges))), f"{e} appears multiple times in {edges}"

    raise NotImplementedError()


