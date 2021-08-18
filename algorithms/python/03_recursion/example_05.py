"""Find the maximum number in a list"""

def find_max(arr):

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

if __name__ == "__main__":
    my_list = [4, 1, 8, 3, 0]

    max = find_max(my_list)

    print(max)
