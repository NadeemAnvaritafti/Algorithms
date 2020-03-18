#!/usr/bin/python

import argparse

array = [1050, 270, 1540, 3800, 2]
# expected = 3530


def find_max_profit(prices):
    current_profit = float('-inf')
    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)-1):
            if prices[j] - prices[i] > current_profit:
                temp = prices[j] - prices[i]
                current_profit = temp
    return current_profit


# Find the greatest difference between two indices given that the smaller value is at an index before the bigger value's index
print(find_max_profit(array))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
