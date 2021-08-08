def selection_sort_smallest(arr):
    new_array = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))

    return new_array

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

if __name__ == "__main__":
    unordered_array = [5, 3, 6, 2, 10]
    print("Unordered List:")
    print(unordered_array)

    sorted_smallest = selection_sort_smallest(unordered_array)

    print("Sorted List By Smallest:")
    print(sorted_smallest)
