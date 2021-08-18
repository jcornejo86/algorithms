"""Count number of elements in a list"""


def get_total_items(arr):
    if arr:
        arr.pop(0)

        return 1 + get_total_items(arr)

    return 0

if __name__ == "__main__":
    my_list = [4, 1, 8, 3, 0]

    total_items = get_total_items(my_list)

    print(total_items)
