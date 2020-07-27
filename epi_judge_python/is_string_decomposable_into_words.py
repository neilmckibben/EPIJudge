import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    letters = [-1] * (len(domain))

    def validWord(sub_string):
        index = len(sub_string) - 1
        if sub_string in dictionary:
            letters[index] = len(sub_string)
        else:
            for i in range(0, len(sub_string)):
                front, back = sub_string[:i + 1], sub_string[i+1:]
                if back in dictionary and letters[len(front) - 1] != -1:
                    letters[index] = len(back)
                    break
    #Backtrack and see if any combinations are possible
    for i in range(0, len(domain)):
        sub_string = domain[:i + 1]
        validWord(sub_string)

    answer = []
    i = len(letters) - 1
    while i >= 0:
        size = letters[i]
        if size == -1:
            return []
        answer.append(domain[i - size + 1: i + 1])
        i -= letters[i]
    answer = answer[::-1]

    return answer




@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
