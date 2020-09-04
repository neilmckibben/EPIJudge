from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    matrix = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(0, len(individual_play_scores)):
        factor = individual_play_scores[i]
        row = matrix[i]
        prev = None
        if i != 0:
            prev = matrix[i - 1]
        value = 0
        for j in range(1, len(row)):
            value = 0
            if factor <= j:
                if j % factor == 0:
                    value += 1
                elif j - factor > 0:
                    value += row[j - factor]
                matrix[i][j] = value
            if prev:
                matrix[i][j] += prev[j]
    for a in matrix:
        print(a)
    return matrix[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))


[0, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2]