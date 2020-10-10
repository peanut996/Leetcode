#!/usr/bin/python3.7
# 剑指 Offer 38. 字符串的排列
from typing import List
# 隐式回溯
class Solution:
    def permutation(self, s: str) -> List[str]:
        # return list(map(''.join,list(itertools.permutations(s))))
        res= []
        s=list(sorted(s))
        def dfs(s: List[str], tmp: List[str]):
            if not s: res.append(''.join(tmp))
            for i in range(len(s)):
                if i>0 and s[i] == s[i-1]: continue
                dfs(s[:i]+s[i+1:],tmp+[s[i]])
        dfs(s,[])
        return res

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
