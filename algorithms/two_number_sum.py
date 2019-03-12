def two_number_sum(array, targetSum):
    array.sort()

    for num in array:
        candidate = targetSum - num

        if candidate in array:
            return [num, candidate]
    return []
