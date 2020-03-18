#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return 0

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


# 0 cookies: 1
# 0

# 1 cookie: 1
# 1


# 2 cookies: 2
# 1, 1
# 2


# 3 cookies: 4
# 1, 1, 1
# 1, 2
# 2, 1
# 3


# 4 cookies: 8
# 1, 1, 1, 1
# 1, 1, 2
# 1, 2, 1
# 1, 3
# 2, 1, 1
# 2, 2
# 3, 1
# 4


# 5 cookies: 16
# 1, 1, 1, 1, 1
# 1, 1, 1, 2
# 1, 1, 2, 1
# 1, 2, 1, 1
# 1, 2, 2
# 1, 1, 3
# 1, 3, 1
# 1, 4
# 2, 1, 1, 1
# 2, 1, 2
# 2, 2, 1
# 2, 3
# 3, 1, 1
# 3, 2
# 4, 1
# 5

# n = 2 * eating_cookies(n-1)

# 1
# 1
# 2
# 4
# 7
# 13
# 24
# 44
# 81
# 149
# 274


# n = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
