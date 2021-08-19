# Hash Table

A hash table is formed by a hash function and arrays. A hash function is a function where you put in a string and you get back a number.

There are some requirements for a hash function:

- It needs to be consistent. It can't return different values for the same given string.
- It should map different words to different numbers. A hash function is no good if it always returns “1” for any word you put in.

Characteristics:

- Consistently maps a name to the same index.
- Maps different strings to different indexes.
- Knows how big your array is and only returns valid indexes.

**Hash tables are probably the most useful complex data structure.**
**They’re also known as hash maps, maps, dictionaries, and associative arrays.**

Hash tables are great when you want to:
- Create a mapping from one thing to another thing
- Look something up

## Collisions

This problem occurs when 2 keys are assigned the same slot in your hash table.

To avoid collisions, you need:
- A low load factor
- A good hash function

### A low load factor

Formula to calculate load factor:
**Number of items in the hash table / total number of slots**

Having a load factor greater than 1 means you have more items than slots in your array.

Once the load factor starts to grow, you need to add more slots to your hash table. This is called resizing.

A good rule of thumb is, resize when your load factor is greater than 0.7.

### A good hash function

- A good hash function distributes values in the array evenly.
- A bad hash function groups values together and produces a lot of collisions.

## Big O

|              | Hash Tables (Average)  | Hash Tables (Worst)  | Arrays | Linked List |
|--------------|------------------------|----------------------|--------|-------------|
| Search       |        O(1)            |        O(n)          |  O(1)  |    O(n)     |
| Insert       |        O(1)            |        O(n)          |  O(n)  |    O(1)     |
| Delete       |        O(1)            |        O(n)          |  O(n)  |    O(1)     |
