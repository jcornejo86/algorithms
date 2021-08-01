def binary_search(lookup, elements, steps=1):
    total_of_elements = len(elements)
    middle_position = int(total_of_elements / 2)

    if lookup == elements[middle_position]:
        return elements[middle_position], steps

    if len(elements) == 1:
        return None, steps

    if lookup > elements[middle_position]:
        result, steps = binary_search(lookup, elements[middle_position:], steps=steps+1)
    else:
        result, steps = binary_search(lookup, elements[:middle_position], steps=steps+1)

    return result, steps


if __name__ == "__main__":
    elements = [x for x in range(0, 9) if (x % 3) == 0 ]
    lookup = 3

    result, steps = binary_search(lookup, elements)

    if result:
        print("Found ", result, " in ", steps, " step(s).")
    else:
        print("Not found. It took ", steps, "step(s).")
