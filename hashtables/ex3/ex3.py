def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    counts = {}
    mark_to_hit = len(arrays)
    res = []
    # print(arrays[0])
    if len(arrays[1]) < len(arrays[0]): 
        print('interesting')
        arrays[1], arrays[0] = arrays[0], arrays[1]
        return arrays
    for a in arrays:
        for elem in a:
            if elem not in counts:
                counts[elem] = 1
            counts[elem] += 1

    for elem in counts:
        if counts[elem] >= mark_to_hit:
            res.append(elem)
    # print(res)
    # print(counts)
    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
