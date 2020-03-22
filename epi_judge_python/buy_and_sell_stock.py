from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    # 2 pointer solution
    max_profit = 0
    minimum = float('inf')
    maximum = float('-inf')
    for price in prices:
        if price < minimum:
            minimum = price
        max_profit = max(price - minimum, max_profit)
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
