# Problem

Suppose you want your todo list to work more like a calendar. Earlier, you were adding things to the end of the list.
Now you want to add them in the order in which they should be done.

Should you use arrays or lists?

# Solution

You should use a list.

# Explanation

With lists, it’s as easy as changing what the previous element points to.
But for arrays, you have to shift all the rest of the elements down. And if there’s no space,
you might have to copy everything to a new location.
