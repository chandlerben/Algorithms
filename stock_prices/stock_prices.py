#!/usr/bin/python

import argparse


def find_max_profit(prices):

    lowest_buy = prices[0]
    biggest_profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        if prices[i] - lowest_buy > biggest_profit:
            biggest_profit = prices[i] - lowest_buy
        if prices[i] < lowest_buy:
            lowest_buy = prices[i]
    return(biggest_profit)


print(find_max_profit([20, 12, 8, 7]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
