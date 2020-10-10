#!/usr/bin/python3.7
# 剑指 Offer 48. 最长不含重复字符的子字符串
# from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        dic = dict()
        dic[s[0]] = 0
        dp[0]=res= 1
        for i in range(1,len(s)):
            # 需要判定之前重复字符下标距离 是否在最长子串中
            if s[i] not in dic or i-dic[s[i]] > dp[i-1]:
                # 不在 当前
                dp[i] = dp[i-1] + 1
            else:
                # 在的话 更新当前dp值
                dp[i] = i - dic[s[i]]
            dic[s[i]] = i
            res = max(res,dp[i])
        return res

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
