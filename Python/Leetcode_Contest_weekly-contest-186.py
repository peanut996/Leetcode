#!/usr/bin/python3.7

from typing import List
import itertools
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)):
            tmp=s[:i].count('0')+s[i:].count('1')
            res = (tmp if tmp > res else res)
        return res


    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)
        m = 0
        if n==k: return sum(cardPoints)
        for i in range(k+1):
            # print(cardPoints[i:i+n-k])
            tmp = s - sum(cardPoints[i:i+n-k])
            print(tmp)
            m = m if m>tmp else tmp
        return m



if __name__ == '__main__':
    cardPoints = [96,90,41,82,39,74,64,50,30]
    k = 8
    solution = Solution()
    try:
        assert solution.maxScore(cardPoints,k)==536
    except AssertionError:
        print(solution.maxScore(cardPoints,k))
        print('解答错误')
