from typing import List, Tuple

from random import shuffle


def rebase_edges(m: int, edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Add m to each vertex in the given list of edges.  if m is larger
    than the number of vertices in the graph, this will result in a new graph
    isomorphic to the first, with no vertices in common."""
    return [(a + m, b + m) for a, b in edges]


def gen_cycle(n: int) -> List[Tuple[int, int]]:
    """Generate edges of a cycle graph with vertices through n-1 inclusive."""
    return [(a, a + 1) for a in range(n - 1)] + [(n - 1, 0)]


def permute_edges(n: int, edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Randomly rename the vertices given a list of edges, maintaining n-many vertices"""
    permutation = [i for i in range(n)]
    shuffle(permutation)
    return [(permutation[a], permutation[b]) for a, b in edges]


def gen_eulerian_graph(n: int) -> List[Tuple[int, int]]:
    """Generate a list of tuples designating edges of a graph
    having n vertices.  The edges """
    assert n >= 3
    m1 = n // 2
    m2 = n - m1
    assert m1 >= 2
    assert m2 >= 1
    cycle1 = permute_edges(m1, gen_cycle(m1))
    cycle2 = rebase_edges(m1, permute_edges(m2, gen_cycle(m2)))
    return cycle1 + cycle2 + [(cycle1[0][0], cycle2[0][0]),
                              (cycle2[0][0], cycle1[1][0]),
                              (cycle1[0][0], cycle1[1][0])]
