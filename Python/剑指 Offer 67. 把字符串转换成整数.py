#!/usr/bin/python3.7
# 剑指 Offer 67. 把字符串转换成整数
# from typing import List

class Solution:
    def strToInt(self, s: str) -> int:
        if not s: return 0
        tag,ret = 1,0
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        s = s.strip()
        if s and s[0] == '-': tag = -1
        if s and s[0] in '+-':
            s = s[1:]
        while s and s[0].isdigit():
            if ret > bndry or ret == bndry and s[0] > '7': return int_max if tag == 1 else int_min 
            ret = ret *10 + ord(s[0]) - ord('0')
            s = s[1:]
        return ret * tag
        
        

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
