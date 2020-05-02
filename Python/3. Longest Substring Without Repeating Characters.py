#!/usr/bin/python3.7

# from typing import List
"""3. Longest Substring Without Repeating Characters

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set=set()
        n=len(str)
        r,res = -1,0
        for l in range(n):
            if l!=0:
                Set.remove(s[l-1])
            while r+1<n and not s[r+1] in Set:
                Set.add(s[r+1])
                r+=1
            res=max(res,r-(l-1))
        return res


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
