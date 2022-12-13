'''

GitHub link: https://github.com/networkx/networkx/blob/main/networkx/algorithms/approximation/vertex_cover.py

A. Check what the theoretical approximation ratio of the algorithm you found.

    The total weight of the set is guaranteed to be at most twice the total
    weight of the minimum weight vertex cover.
    The algorithm gets graph and weight, the weight is optional
    If weight None, every node has weight 1.

    math:
       w(S) \leq 2 * w(S^*)

    where $S$ is the vertex cover returned by this function,
    $S^*$ is the vertex cover of minimum weight out of all vertex
    covers of the graph, and $w$ is the function that computes the
    sum of the weights of each node in that given set.
'''
from itertools import combinations
import doctest

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from networkx import Graph
from networkx.algorithms.approximation.vertex_cover import *


def naive_approach(graph: Graph) -> int:
    '''
    We can naively solve the problem by iterating over all the subsets of the vertices
    and using only those vertices, forming a new graph containing all the edges contained by these vertices.
    Then we can check if this new graph, contains all the edges of the original graph or not based on
    which it can be a candidate for the vertex cover.
    Out of all the candidates, we print the set, which has the minimum size.

    >>> my_graph = nx.Graph()
    >>> my_graph.add_nodes_from([1, 2, 3])
    >>> my_graph.add_edges_from([(3, 1), (3, 2)])
    >>> naive_approach(my_graph)
    1
    >>> my_graph = nx.Graph()
    >>> my_graph.add_nodes_from([])
    >>> my_graph.add_edges_from([])
    >>> naive_approach(my_graph)
    0
    '''
    # Initialize the minimum vertex cover to be the number of vertices in the graph
    min_vertex_cover = len(graph)

    # Loop over all possible combinations of vertices
    for i in range(1, len(graph)):
        for vertex_combination in combinations(graph, i):

            # Calculate the number of vertices covered by this combination
            covered_vertices = set()
            for vertex in vertex_combination:
                covered_vertices.update(graph[vertex])  # Update a set with the union of itself and others

            # Update the minimum vertex cover if this combination covers fewer vertices
            min_vertex_cover = min(min_vertex_cover, len(covered_vertices))

    return min_vertex_cover


if __name__ == '__main__':
    doctest.testmod()

    nodes = [i for i in range(5, 23)]  # 5,...23 nodes
    prob = [np.random.random() for i in range(18)]

    ratio = []

    i = 0
    for i in range(18):
        print(f'loop {i}/18, be patient.')
        graph = nx.gnp_random_graph(nodes[i], prob[i])  # random graph
        approx = len(min_weighted_vertex_cover(graph))  # call the approximation vertex cover algorithm
        complete = naive_approach(graph)  # call the complete algorithm, can't found
        approximation_ratio = complete - approx  # calc the ratio between them
        ratio.append(approximation_ratio)

    fig, ax = plt.subplots()

    ax.plot(range(i + 1), nodes, 'blue')
    ax.plot(range(i + 1), prob, 'red')
    ax.plot(range(i + 1), ratio, 'black')
    ax.set_title('Number of nodes (blue) | probability (red) | ratio (black)')
    plt.show()
