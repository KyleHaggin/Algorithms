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
    if rounds_left > 0:
        thirds = len(rps)//3
        rock = rps[:thirds]
        paper = rps[thirds:thirds*2]
        scissors = rps[thirds*2:]

        [item.extend(['rock']) for item in rock[:len(rock)//3]]
        [item.extend(['paper']) for item in rock[len(rock)//3:len(rock)//3*2]]
        [item.extend(['scissors']) for item in rock[len(rock)//3*2:]]

        [item.extend(['rock']) for item in paper[:len(rock)//3]]
        [item.extend(['paper']) for item in paper[len(rock)//3:len(rock)//3*2]]
        [item.extend(['scissors']) for item in paper[len(rock)//3*2:]]

        [item.extend(['rock']) for item in scissors[:len(rock)//3]]
        [item.extend(['paper']) for item in scissors[len(rock)//3:len(rock)//3*2]]
        [item.extend(['scissors']) for item in scissors[len(rock)//3*2:]]

        rps_recursive_helper(rock, rounds_left-1)
        rps_recursive_helper(paper, rounds_left-1)
        rps_recursive_helper(scissors, rounds_left-1)

        rps = rock+paper+scissors

    return rps


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    total = 3**n
    third_total = total//3
    # Create the initial list
    rps = []
    for x in range(third_total):
        rps.append(['rock'])
    for x in range(third_total):
        rps.append(['paper'])
    for x in range(third_total):
        rps.append(['scissors'])
    rps = rps_recursive_helper(rps, n-1)
    return rps


print(rock_paper_scissors(3))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
