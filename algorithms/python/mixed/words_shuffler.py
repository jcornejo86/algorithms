import random


def stringShuffler(string):
    if len(string) < 4:
        return string

    startCharIdx = 1
    lastCharIdx = len(string) - 1
    visitedIdx = {0, lastCharIdx}

    newString = []
    newString.append(string[0])

    while startCharIdx < lastCharIdx:
        if ord("a") > ord(string[startCharIdx]) > ord("Z"):
            visitedIdx.add(startCharIdx)
            startCharIdx += 1
            continue

        potentialIdx = random.randint(1, lastCharIdx - 1)
        if potentialIdx not in visitedIdx:
            newString.append(string[potentialIdx])
            visitedIdx.add(potentialIdx)
            startCharIdx += 1

    newString.append(string[lastCharIdx])

    return "".join(newString)

if __name__ == "__main__":
    # Input
    text = """Probably all of you have read a text like this before.
    It's amazing how powerful is our brain. It can take this messy text and make sense of it for you!
    Hope y'all had a great weekend!"""

    # Driver
    result = []
    print('\n' * 2)
    words = text.split(" ")
    for string in words:
        result.append(stringShuffler(string))

    print(" ".join(result))
    print('\n' * 2)

"""
Pablrboy all of you have read a txet like tihs beroef.
It's amnaizg how pueorfwl is our bnrai.
It can tkae this mssey text and make sesne of it for you!
Hpoe yl'al had a great wekndee!
"""
