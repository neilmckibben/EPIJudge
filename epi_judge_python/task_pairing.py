import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    # TODO - you fill in here.
    print(task_durations)
    task_durations.sort()
    task_list = []
    small, large = 0, len(task_durations) - 1

    while small <= large:
        job = PairedTasks(task_durations[small], task_durations[large])
        task_list.append(job)
        small += 1
        large -= 1

    return task_list


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
