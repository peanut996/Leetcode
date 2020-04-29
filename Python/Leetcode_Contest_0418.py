#!/usr/bin/python3.7

from typing import List
class Solution:
    
    def minCount(self, coins: List[int]) -> int:
        length=len(coins)
        res=0
        for i in coins:
            if i&1:
                res += int(i/2)+1
            else:
                res+= i/2
        return res



    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        des = [[] for _ in range(n)]
        res = 0
        for r in relation:
            des[r[0]].append(r[1])

        def dfs(i: int,nums: List[int]) -> int:
            temp = 0
            if i>k:
                return 0
            if i==k and n-1 in nums:
                return 1
            for d in nums:
                temp+=dfs(i+1,des[d])
            return temp
                
        res = dfs(1,des[0])
        return res
    

    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        c,r,h = 0,0,0
        status = [[0,0,0]]
        res = [-1] *len(requirements)
        for i in increase:
            c,r,h = c+i[0],r+i[1],h+i[2]
            status.append([c,r,h])

        length=len(status)
        for i,requirement in enumerate(requirements):
            left,right=0,length-1
            while left<=right:
                mid = left + (right - left)//2
                if status[mid][0] >= requirement[0] and status[mid][1] >= requirement[1] and status[mid][2] >= requirement[2]:
                    res[i]=mid
                    right=mid-1
                else:
                    left=mid+1
        return res


def main():
    solution = Solution()
    increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]]
    requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
    result = solution.getTriggerTime(increase,requirements)
    try:
        assert result == [-1,4,3,3,3]
        pass
    except AssertionError:
        print(result)
        print('解答错误')


if __name__ == '__main__':
    main()
