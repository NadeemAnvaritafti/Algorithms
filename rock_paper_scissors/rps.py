#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    choices = ['rock', 'paper', 'scissors']
    array = []

    def recursive_function(newlist, plays):
        if plays == 0:
            return array.append(newlist)
        for i in range(0, len(choices)):
            recursive_function(newlist + [choices[i]], plays - 1)

    recursive_function([], n)

    return array


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
