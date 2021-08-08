from pprint import pprint

def most_view_sort(unsorted_array):
    sorted_array = []

    while unsorted_array:
        most_viewed = 0
        remove_index = 0
        candidate = None

        for idx, element in enumerate(unsorted_array):
            if element["views"] >= most_viewed:
                most_viewed = element["views"]

                candidate = element
                remove_index = idx

        sorted_array.append(candidate)
        unsorted_array.pop(remove_index)

    return sorted_array

if __name__ == "__main__":
    movies = [
        {"title": "No wonder why", "views": 57},
        {"title": "Tell me", "views": 74},
        {"title": "Rocket", "views": 234},
        {"title": "Living in the sand", "views": 134},
        {"title": "Water", "views": 146},
        {"title": "The little things", "views": 42},
    ]
    print("Unorder Movie List:")
    pprint(movies)

    sorted_most_view = most_view_sort(movies)

    print("Sorted List By Most Viewed:")
    pprint(sorted_most_view)
