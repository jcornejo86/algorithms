# Binary Search

Its input is a sorted list of elements. If an element you’re looking for is in that list, binary search returns the position where it’s located. Otherwise, binary search returns null.

With each step of binary search, you look up the element in the middle of the list. Depending on whether the element we look for is higher or lower than the one returned, it will discard one of the half and repeat the same process.

Example:

List of elements: [0, 1, 2, ..., 99, 100]
Search for number 17

Look in the middle:
[0, 1, 2, ..., 50, ..., 99, 100]
               ^

17 is lower than 50, discard all numbers above 50. Look again in the middle:
[0, 1, 2, .., 25, ..., 50]
               ^

17 is lower than 25, discard all numbers above 25. Look again in the middle:
[0, ... , 12, ..., 25]
           ^

17 is higher than 12, discard all numbers below 12. Look again in the middle:
[12, ..., 18, ..., 25]
           ^

17 is lower than 18, discard all numbers above 18. Look again in the middle:
[12, ..., 15, ..., 18]
           ^

17 is higher than 15, discard all numbers below 15. Look again in the middle:
[15, 16, 17, 18]
     ^

17 is higher than 16, discard all numbers below 16. Look again in the middle:
[16, 17, 18]
      ^

17 has been found !

**In general, for any list of n, binary search will take log2 n.**

## Logarithms

log2 8 is like asking, “How many 2s do we multiply together to get 8?” The answer is 3: 2 × 2 × 2. So log2 8 = 3.


### Note

Binary search only works when your list is in sorted order.


## Running Time For Search Algorithms:

- Linear Time (Simple search): 
  If this is a list of 100 numbers, it takes up to 100 guesses

- Logarithmic Time (Binary search):
  If the list is 100 items long, it takes at most 7 guesses.
