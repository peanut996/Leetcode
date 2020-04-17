#!/usr/bin/python3.7

"""面试题13. 机器人的运动范围  LCOF
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
"""

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def getsum(num: int) -> int:
            res=0
            while num:
                res+=num%10
                num= num // 10
            return res
        
        def dfs(i: int,j: int,i_sum: int,j_sum:int) -> int:
            if not 0<=i<m or not 0<=j<n or k<i_sum+j_sum or (i,j) in visited: return 0
            visited.add((i,j))
            return 1+dfs(i+1,j,getsum(i+1),j_sum)+dfs(i,j+1,i_sum,getsum(j+1))
        
        visited=set()
        return dfs(0,0,0,0)

def main():
    solution = Solution()
    try:
        assert 3==solution.movingCount(2,3,1)
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
