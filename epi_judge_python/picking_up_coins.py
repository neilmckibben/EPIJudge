from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    gain = list(coins)
    frontGai
    def play(coins):
        if coins and len(coins) >= 2:
                front, back = coins[0], coins[-1]
                front_next, back_next = coins[1], coins[-2]
                front_gain = front - front_next
                back_gain = back - back_next
                if front_gain > back_gain:
                    return coins.pop(0)
                else:
                    return coins.pop(len(coins) - 1)
        elif len(coins) == 1:
            return coins.pop()
        return 0
    max_score = 0
    while coins:
        max_score += play(coins)
        print(coins)
        play(coins)
        print(coins)
    return max_score


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
