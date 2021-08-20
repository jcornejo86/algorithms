# Breadth-First Search

Breadth-first search is a graph algorithm which allows you to find the shortest distance between two things.

You can use breadth-first search to:
- Write a checkers AI that calculates the fewest moves to victory
- Find the doctor closest to you in your network

## Introduction to graphs

- A graph models a set of connections. Each graph is made up of nodes and edges.
- A node can be directly connected to many other nodes. Those nodes are called its neighbors.
- Graphs are a way to model how different things are connected to one another.

## Breadth-first search

It can help answer two types of questions:

- Is there a path from node A to node B?
- What is the shortest path from node A to node B?


Note:
A queue is called a FIFO data structure: First In, First Out. In contrast, a stack is a LIFO data structure: Last In, First Out.

A graph can be represented with a hash table. Example:

    graph = {}
    graph["me"] = ["friend Bea", "sister", "dad", "mom"]
    graph["sister"] = ["friend Bob", "dad", "mom"]
    graph["friend Bob"] = ["Tom", "Paul"]



## Big O

Breadth-first search takes O(number of people + number of edges), and it’s more commonly written as O(V+E) (V for number of vertices, E for number of edges).
