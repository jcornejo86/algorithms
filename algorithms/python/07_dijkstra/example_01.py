from pprint import pprint

"""
Graph set up
"""

NODE_START = "start"
NODE_FINISH = "finish"
NODE_A = "a"
NODE_B = "b"

# Representation of a graph with its weights and edges.

graph = {}

# Node `Start` with neighbors NODE_A and NODE_B
graph[NODE_START] = {}
graph[NODE_START][NODE_A] = 6
graph[NODE_START][NODE_B] = 2

# Node `NODE_A` with neighbor NODE_FINISH
graph[NODE_A] = {}
graph[NODE_A][NODE_FINISH] = 1

# Node `NODE_B` with neighbors NODE_A and NODE_FINISH
graph[NODE_B] = {}
graph[NODE_B][NODE_A] = 3
graph[NODE_B][NODE_FINISH] = 5

graph[NODE_FINISH] = {}


# Hash table to store the costs for each node.
# The cost of a node is how long it takes to get to that node from the start.

infinity = float("inf")

costs = {}
costs[NODE_A] = 6
costs[NODE_B] = 2
costs[NODE_FINISH] = infinity

# Hash table to keep track of the nodes parents

parents = {}
parents[NODE_A] = NODE_START
parents[NODE_B] = NODE_START
parents[NODE_FINISH] = None

# Array to keep track of nodes that have been visited
processed = []

"""
Implementation
"""

def find_shortest_path():
    # Find the lowest cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        # Go through all the neighbors of this node.
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            # Is it cheaper to get to this neighbor by going through this node ?
            if costs[n] > new_cost:
                costs[n] = new_cost  # Update the cost of this node.
                parents[n] = node    # This node becomes the new parent for this neighbor.

        # Mark the node as processed.
        processed.append(node)

        # Find the next node to process.
        node = find_lowest_cost_node(costs)

    return parents

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


if __name__ == "__main__":

    result = find_shortest_path()

    pprint(result)
