import itertools
import doctest

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from networkx import Graph
from networkx.algorithms.approximation.vertex_cover import *

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
    >>> my_graph = nx.Graph()
    >>> my_graph.add_nodes_from([1, 2, 3, 4, 5])
    >>> my_graph.add_edges_from([(3, 1), (3, 2), (4, 5)])
    >>> naive_approach(my_graph)
    2
    '''
    # Create a list of all the vertices in the graph
    vertices = list(graph.nodes())

    # Set the initial minimum vertex cover to be the size of the graph
    min_vertex_cover = len(vertices)

    # Loop through all possible combinations of vertices
    for i in range(1, len(vertices) + 1):
        for vertex_combination in itertools.combinations(vertices, i):
            # Create a copy of the graph and remove the selected vertices
            temp_graph = graph.copy()
            temp_graph.remove_nodes_from(vertex_combination)

            # Check if all edges have been covered by the selected vertices
            all_edges_covered = nx.number_of_edges(temp_graph) == 0

            # If all edges have been covered, update the minimum vertex cover
            if all_edges_covered:
                min_vertex_cover = min(min_vertex_cover, len(vertex_combination))

    # Return the minimum vertex cover
    return min_vertex_cover


if __name__ == '__main__':
    doctest.testmod()

    nodes = [i for i in range(5, 19)]  # 5,...23 nodes
    prob = [np.random.random() for i in range(14)]

    ratio = []

    i = 0
    for i in range(14):
        print(f'loop {i}/14, be patient...')
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
