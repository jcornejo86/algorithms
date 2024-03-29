def quick_sort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)




if __name__ == "__main__":
    arr = [5,1,4,9,2,3,7]

    result = quick_sort(arr)

    print(result)
