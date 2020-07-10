def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    counts = {}
    result = []
    for elem in a:
        # print(abs(elem))
        minimized = abs(elem)
        if minimized not in counts:
            counts[minimized] = 0
        counts[minimized] += 1
    print(counts)
    for elem in counts:
        if counts[elem] >= 2:
            result.append(elem)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
