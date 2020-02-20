#!/usr/bin/python

import sys


# def rps_recursive_helper(n, rps):
#     thirds = len(rps)//3
#     if len(rps[0]) < n:
#         for x in range(thirds):
#             i = x*3
#             rps[i] = rps[i]+['rock']
#             rps[i+1] = rps[i+1]+['paper']
#             rps[i+2] = rps[i+2]+['scissors']


def rps_recursive_helper(rps, rounds_left):
    rps_play = [['rock'], ['paper'], ['scissors']]
    if rounds_left == 0:
        return rps
    else:
        print('click')
        for x in range(2):
            rps_recursive_helper(rps+rps_play[x], rounds_left-1)


def rock_paper_scissors(n):
    rps = []
    rps = rps_recursive_helper(rps, n)
    return rps

# def rock_paper_scissors(n):
#     # Define rps plays
#     # rps_play = ['rock', 'paper', 'scissors']
#     total = 3**n
#     third_total = total//3
#     # Initialize as list
#     if n == 0:
#         return rps
#     # Create the initial list
#     if rps == []:
#         for x in range(third_total):
#             rps.append(['rock'])
#         for x in range(third_total):
#             rps.append(['paper'])
#         for x in range(third_total):
#             rps.append(['scissors'])
#     thirds = len(rps)//3
#     rps_recursive_helper(n, rps)
#     return rps

# test2 = [['rock'], ['rock'], ['rock'], ['paper'], ['paper'], ['paper'], ['scissors'], ['scissors'], ['scissors']]
# rps_recursive_helper(3, test2)
# print(test2)
print(rock_paper_scissors(2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
