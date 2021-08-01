def binary_search(list, item):
    low = 0
    high = len(list) - 1

    count = 1
    while low <= high:
        mid  = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return guess, count
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

        count += 1

if __name__ == "__main__":
    my_list = [x for x in range(0, 9) if (x % 3) == 0 ]

    result, steps = binary_search(my_list, 3)

    if result:
        print("Found item ", result, " in ", steps, " step(s).")
    else:
        print("Nothing found.")
