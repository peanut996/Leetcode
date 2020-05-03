#!/usr/bin/python3.7

# from typing import List
"""1417. Reformat The String
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 
"""

class Solution:
    def reformat(self, s: str) -> str:
        num,alpha = [],[]
        for b in s:
            if b.isdigit():
                num.append(b)
            else:
                alpha.append(b)
        num_length,alpha_length = len(num),len(alpha_length)
        if abs(len(num)-len(alpha))>1:
            return ''
        res = []
        if num_length>alpha_length:
            while num: 
                res.append(num.pop())
                if alpha:
                    res.append(alpha.pop())
        else:
            while alpha:
                res.append(alpha.pop())
                if num:
                    res.append(num.pop())
        return ''.join(res)
                    
        

            
if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
