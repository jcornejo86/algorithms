# Dijkstra's algorithm

An algorithm that is used for finding the shortest distance, or path, from starting node to target node in a weighted graph.

Dijkstra’s algorithm has four steps:

- Find the cheapest node. This is the node you can get to in the least amount of time.
- Check whether there’s a cheaper path to the neighbors of this node. If so, update their costs.
- Repeat until you’ve done this for every node in the graph.
- Calculate the final path.

# Terminology

- When you work with Dijkstra’s algorithm, each edge in the graph has a number associated with it. These are called **weights**.
- A graph with weights is called a **weighted graph**. A graph without weights is called an **unweighted graph**.
- To calculate the shortest path in an unweighted graph, use **breadth-first search**. To calculate the shortest path in a weighted graph, use **Dijkstra’s algorithm**.
- Graphs can also have cycles (undirected graph).
- An undirected graph means that both nodes point to each other.
- **Dijkstra’s algorithm only works on graphs with no cycles, or on graphs with a positive weight cycle.**

# Note

you can’t use **negative-weight edges** with Dijkstra’s algorithm. If you want to find the shortest path in a graph that has negative-weight edges, you will use the
**Bellman-Ford algorithm**.
