"""Sum total value given an array"""

def sum_total(arr):
    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum_total(arr[1:])


if __name__ == "__main__":
    values = [3, 8, 4, 3]

    result = sum_total(values)

    print(result)
