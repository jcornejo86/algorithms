# Problem

Suppose you have a sorted list of 128 names,
and you’re searching through it using binary search.

What’s the maximum number of steps it would take?

# Solution

Remember: **In general, for any list of n, binary search will take log2 n.**

Therefor, we have a list of 128 names, so it will take log2 128.

# Explanation

2^x = 128

Get factors of 128.

128 | 2
64  | 2
32  | 2
16  | 2
8   | 2
4   | 2
2   | 2
1

2^x = 2^7

Now that we have the equation in the same base, we can remove the base. That gives us:

x = 7

**The maximum number of steps that would take is 7.**
