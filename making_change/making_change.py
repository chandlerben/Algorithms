#!/usr/bin/python

import sys

old_denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations):
    ways = [denominations[0]] * (amount + 1)
    steps = 0
    del denominations[0]

    for value in denominations:
        for higher_amount in range(value, amount + 1):
            remainder = higher_amount - value
            ways[higher_amount] += ways[remainder]
            steps += 1

    print(steps)
    return ways[amount]


print(making_change(350, old_denominations))

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
