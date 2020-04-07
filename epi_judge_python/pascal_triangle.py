from test_framework import generic_test


def generate_pascal_triangle(n):
    if n is 0:
        return []
    if n is 1:
        return [[1]]
    if n is 2:
        return [[1], [1, 1]]
    maxtrix = [[1], [1, 1]]
    for i in range(2, n):
        row = []
        prev = 0
        for element in maxtrix[i-1]:
            row.append(element + prev)
            prev = element
        row.append(1)
        maxtrix.append(row)
    return maxtrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
