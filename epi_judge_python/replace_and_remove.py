import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    length = len(s)
    s = ([i for i in s if i is not "b"])
    size = size - (length - len(s))

    for i in range(0, len(s)):
        if s[i] == "a":
            size += 1
            s[i] = "d"
            s.insert(i, "d")
    return s[:size]


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return res_size
    # return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
