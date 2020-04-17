#!/usr/bin/python3.7

"""22. Generate Parentheses
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(curr: str,left: int,right: int):
            if left==0 and right==0:
                res.append(curr)
                return
            # 剪枝
            if right<left: return
            if left>0: dfs(curr+'(',left-1,right)
            if right>0: dfs(curr+')',left,right-1)
        res=[]
        dfs('',n,n)
        return res
        
def main():
    solution = Solution()
    try:
        assert solution.generateParenthesis(3)==["((()))","(()())","(())()","()(())","()()()"]
    except AssertionError:
        print('Wrong Answer.')


if __name__ == '__main__':
    main()
