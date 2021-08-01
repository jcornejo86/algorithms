# Problem

Suppose you double the size of the list from exercise 1_1.
What’s the maximum number of steps now?


# Solution

Remember: **In general, for any list of n, binary search will take log2 n.**

Now we have a list of 128*2 names (256), so it will take log2 256.

# Explanation

2^x = 256

Get factors of 256.

256 | 2
128 | 2
64  | 2
32  | 2
16  | 2
8   | 2
4   | 2
2   | 2
1

2^x = 2^8

Now that we have the equation in the same base, we can remove the base. That gives us:

x = 8

**So the maximum number of steps that would take is 8.**
