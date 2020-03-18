#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    choices = ['rock', 'paper', 'scissors']
    new_array = []

    if n == 1:
        for i in choices:
            new_array.append([i])

    return new_array


print(rock_paper_scissors(1))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
