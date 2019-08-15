from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    counter = 0
    maxProfit = 0.0
    min = float('inf')
    for price in prices:
        if price < min:
            min = price

        if((price - min) > maxProfit):
            maxProfit = price - min
    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
