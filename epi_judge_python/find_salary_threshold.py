from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    members = len(current_salaries)
    total = 0
    end_index = 0
    for i, salary in enumerate(current_salaries):
        cap_effect = (members - i) * salary
        if cap_effect + total == target_payroll:
            return salary
        elif cap_effect + total > target_payroll:
            end_index = i
            break
        total += salary
    if i == members - 1:
        return -1.0
    remaining = members - end_index
    target = ((target_payroll - total) / remaining)
    return target


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
