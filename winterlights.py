"""
https://codility.com/programmers/task/winter_lights/
"""


def solution(S):
    rel = [[0] * 1024, [0] * 1024]
    rel[0][1 << int(S[0])] = 1
    sum = 1
    for k in range(1, len(S)):
        for i in range(1024):
            rel[k & 1][i] = rel[(k + 1) & 1][i ^ (1 << int(S[k]))]
        rel[k & 1][1 << int(S[k])] += 1
        for i in range(10):
            sum += rel[k & 1][1 << i]
        sum += rel[k & 1][0]
        sum %= 1000000007
    return sum
