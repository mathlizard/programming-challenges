""" 
https://codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/slalom_skiing/
"""

import bisect


def longestIncreasingSubsequence(s):
    """ returns the length of the longest increasing subsequence in s """
    min_tail = [None] * (len(s) + 1)
    min_tail[0] = -1
    # longest increasing subsequence length
    lis_len = 0
    for i in range(len(s)):
        index = bisect.bisect_left(min_tail, s[i], 0, lis_len + 1)
        if min_tail[index] is None:
            lis_len += 1
            min_tail[index] = s[i]
        else:
            min_tail[index] = min(min_tail[index], s[i])
    return lis_len


def solution(A):
    k = max(A) + 1
    # put a slalom in 'A'
    A_ext = [((k << 1) + p, (k << 1) - p, p) for p in A]
    # call longestIncreasingSubsequence with the flattened 'A_ext'
    return longestIncreasingSubsequence( [x for tup in A_ext for x in tup] )
 
