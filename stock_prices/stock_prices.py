#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Initialize the profit as the worst case for future comparison
    profit = min(prices) - max(prices)
    # Iterate through entire list minus 1
    for x in range(len(prices)-1):
        # Iterate through entire list after x
        for y in range(len(prices)-1-x):
            index_hldr = y + 1 + x
            profit_hldr = prices[index_hldr] - prices[x]
            # If profit holder is more than the current highest profit
            # set profit to the profit holder
            if profit_hldr > profit:
                profit = profit_hldr

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.'
        )
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}."
          .format(profit=find_max_profit(args.integers), prices=args.integers))
