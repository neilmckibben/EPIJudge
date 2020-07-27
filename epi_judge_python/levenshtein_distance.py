from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    matrix = [[0] * len(B) for _ in A]
    def calculate(aPointer, bPointer):
        if aPointer < 0:
            return 1 + bPointer
        if bPointer < 0:
            return 1 + aPointer
        if matrix[aPointer][bPointer] == 0:
            aChar, bChar = A[aPointer], B[bPointer]
            if aChar == bChar:
                matrix[aPointer][bPointer] = calculate(aPointer - 1, bPointer - 1)
            else:
                delete = calculate(aPointer - 1, bPointer - 1)
                subB = calculate(aPointer - 1, bPointer)
                subA = calculate(aPointer, bPointer - 1)
                matrix[aPointer][bPointer] = 1 + min(delete, subB, subA)
        return matrix[aPointer][bPointer]

    return calculate(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
