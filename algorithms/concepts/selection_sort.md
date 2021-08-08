# Selection Sort

Selection Sort is a sorting algorithm.

It will require to go through the list many times as elements are in the list.

It has a complexity of **O(n^2)** (Quadratic).

Suppose the following list of movies:
[
    {"title": "Living in the sand", "views": 134},
    {"title": "Rocket", "views": 234},
    {"title": "Water", "views": 146},
]

If we wanted to sort these by most views to least. We will loop over the list one time to find the most viewed one and store it in a new list.

sorted_movie_list_most_viewed:
[
  {"title": "Rocket", "views": 234},
]

Then we will do the same operation to find the most viewed movie of the remaining movies in the list.

sorted_movie_list_most_viewed:
[
  {"title": "Rocket", "views": 234},
  {"title": "Water", "views": 146},
]

And so on until we are done with the list.

sorted_movie_list_most_viewed:
[
  {"title": "Rocket", "views": 234},
  {"title": "Water", "views": 146},
  {"title": "Living in the sand", "views": 134},
]

# Key points

- When you want to store multiple elements, use an array or a list.
- With an array, all your elements are stored right next to each other.
- With a list, elements are spread all over, and one element stores the address of the next one.
- Arrays allow fast reads.
- Linked lists allow fast inserts and deletes.
- All elements in the array should be the same type (all ints, all doubles, and so on).

### Note

Selection Sort is the fundamental to understand Quick Sort.
