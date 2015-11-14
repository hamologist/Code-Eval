def permutations(data):
    if len(data) <= 1:
        yield data
    else:
        for perm in permutations(data[1:]):
            for i in range(len(data)):
                yield perm[:i] + data[0:1] + perm[i:]
