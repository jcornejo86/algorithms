# Quick Sort

Quicksort is a sorting algorithm which uses a general technique called **divide-and-conquer**.

# Inductive proofs

Let's analyze how quick sort works with different size of arrays:

- Empty arrays and arrays with just one element will be the base case.
- An array of two elements: Check if first element is smaller than the second. If it isn't, swap them.
- An array of three elements:
    - First, pick an element from the array. This element is called the pivot.
    - Now find the elements smaller than the pivot and the elements larger than the pivot.
    - The two sub-arrays aren’t sorted. They’re just partitioned. But if they were sorted, the final sort would be: [sub-array smaller] + pivot + [sub-array larger]
    - How to sort the sub-arrays ? -> Using recursion, applying the same logic above.

# Big O Notation

Quicksort speed depends on the pivot you choose.

- In the worst case, quicksort O(n2) time (For example an array that's already sorted choosing always the pivot as the first element of the array).
- In the average case it will take O(n log n) time.

## How to choose the pivot ?

Always choose a random element in the array as the pivot. That will make quicksort complete in O(n log n) time on average.
