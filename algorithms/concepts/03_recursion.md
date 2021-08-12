# Recursion

Recursion is where a function calls itself.

There’s no performance benefit to using recursion; in fact, loops are sometimes
better for performance.

# Base case and recursive case

Because a recursive function calls itself, we can end up in an infinite loop.
It's very important to define an exit condition.

That’s why every recursive function has two parts:
- base case (when the function doesn't call itself again)
- recursive case

**Recursive functions use the call stack**

# The Stack

The stack is a list with only two actions:
- Push: Insert on the top
- Pop: Remove and read from the top

This data structure is called a stack. The stack is a simple data structure.

## The call stack

Computers uses a stack internally called the call stack.

Considering this example:
    def open_main_door():
        open_kitchen_door()
        open_cabinet()

Our computer is going to allocate memory for that function call `open_main_door`
and for all the variables (if any).

Next, our computer will allocate memory for the second call  `open_kitchen_door`

So the call stack so far looks like this:

|open_kitchen_door|
|-----------------|
|open_main_door   |

Once we are done with `open_kitchen_door`, that function call will be removed (pop)
from the stack and it will add the next function call.

|open_cabinet     |
|-----------------|
|open_main_door   |

Once done, it will remove `open_cabinet`.

|open_main_door   |

Lastly, it will exit from `open_main_door`

# Key points

- Using Recursion can make code cleaner.
- Recursion can consume a lot of memory. This is because each function is saved in memory (call stack).
- All function calls go onto the call stack.
- A stack has two operations: push and pop.
- the call stack can get very large, which takes up a lot of memory.
- If a recursion function takes too much memory, the code can be rewrite using a loop instead.
- Some languages support the use of tail recursion.
