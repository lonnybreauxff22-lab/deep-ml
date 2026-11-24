def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    res = []
    if len(a[0]) != len(b):
        return -1
    else:
        for i in range(len(a)):
            num_for = 0
            for w in range(len(a[0])):
                num_for += a[i][w] * b[w]
            res.append(num_for)
    return res
                