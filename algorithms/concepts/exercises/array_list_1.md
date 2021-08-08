# Problem

Suppose you’re building an app to keep track of your finances.

Every day, you write down everything you spent money on. At the end of the month,
you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads.

Should you use an array or a list?

# Solution

You should use a list.

# Explanation

Inserting on an array is more complex **O(n)** than inserting on a list **O(1)**.

Although reading is faster on arrays **O(1)**, the majority of the operations are gonna be to insert,
and only few reads a month. Therefore, it will be more efficient to use a list.
