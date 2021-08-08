# Big O notation

Big O notation tells you how fast an algorithm is.

Generally you want to choose the most efficient algorithm—whether you’re trying to optimize for time or space.

**Big O establishes a worst-case run time**

## Running Times (fastest to slowest)

|              | Complexity  | Example               |
|--------------|-------------|-----------------------|
| O(1)         | Constant    |                       |
| O(log n)     | Logarithmic | Binary Search         |
| O(n)         | Linear      | Simple Search         |
| O(n * log n) | Log linear  | Quicksort             |
| O(n^2)       | Quadratic   | Selection Sort        |
| O(n^3)       | Cubic       |                       |
| O(2^n)       | Exponential |                       |
| O(n!)        | Factorial   | Traveling Salesperson |

## Running Times Array vs List

|              | Arrays  | Lists  |
|--------------|---------|--------|
| Reading      | O(1)    | O(n)   |
| Insertion    | O(n)    | O(1)   |
| Deletion     | O(n)    | O(1)   |

## Notes

- Algorithm speed isn’t measured in seconds, but in growth of the number of operations.
- Run time of algorithms is expressed in Big O notation.
- O(log n) is faster than O(n), and it gets a lot faster as the list of items you’re searching grows.
