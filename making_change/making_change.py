#!/usr/bin/python

import sys


# def making_change(amount, denominations):
#     denominations.sort()
#     num_ways = {}
#     for denomination in denominations:


def making_change(amount, denominations):
    m = len(denominations)
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(amount+1)]

    # Base case amount == 0
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(m):
        for j in range(denominations[i], amount+1):
            table[j] += table[j-denominations[i]]

    return table[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
