"""

EX1 - Question 2 - PYTHON
Eran Levy - 311382360

Run Example: Can see on the test i wrote.

"""
import doctest
from typing import Any


def func(node):
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


"""
    breadth_first_search function:
        Generic BFS function (on any type of graph).
        The neighbor_function function receive a node and returns all his neighbors
"""


def breadth_first_search(start: Any, end: Any, neighbor_function) -> list:
    # -- TESTS --
    '''
     >>> breadth_first_search((0, 1), (2, 2),func)
     [(0, 1), (1, 1), (2, 1), (2, 2)]

     >>> breadth_first_search((0, 0), (2, -2),func)
     [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)]

     >>> breadth_first_search((0, 4), (2, -2),func)
     [(0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (2, -1), (2, -2)]

    '''
    # -- END OF TESTS --
    visit = []
    queue = []

    visit.append(start)  # All the nodes we visited
    queue.append([start])

    while len(queue) > 0:
        path = queue.pop(0)  # Start the path from the start node of the graph
        last_node_in_path = path[-1]  # Taking the last node in the path. if it's equal to end node we done.
        if last_node_in_path == end:
            return path
        for neighbour in neighbor_function(last_node_in_path):
            if neighbour not in visit:  # This causes the search to stop if we can't find the end
                visit.append(neighbour)
                new_path = list(path)  # I wrapped the path var with a list to our output.
                new_path.append(neighbour)
                queue.append(new_path)


if __name__ == "__main__":
    doctest.testmod()
