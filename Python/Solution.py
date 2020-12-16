#!/usr/bin/python3.7
from typing import List
import collections

class Solution:
    def interpret(self, command: str) -> str:
        res = command.replace("()","o")
        res = res.replace("(al)","al")
        return res
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2: return 0
        res = 0
        nums.sort()
        left,right=0,len(nums)-1
        while left<right:
            tmp = nums[left] + nums[right]
            if tmp == k: 
                res += 1
                left+=1
                right-=1
            elif tmp < k:
                left += 1
            else:
                right -= 1
        return res
    def concatenatedBinary(self, n: int) -> str:
        mod = pow(10,9) + 7
        def helper(n: int):
            if n <= 0:
                return ""
            return helper(n-1)+str(bin(n))[2:]
        return str(int(helper(n),2)%mod)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dic = collections.defaultdict(list)
        for u,v,w in times:
            dic[u].append((v,w))
        visited = {K:0}
        queue = [(K,0)]
        while queue:
            cnode,ctime = queue.pop(0)
            for nnode,ntime in dic[cnode]:
                t = ctime + ntime
                if nnode not in visited or t < visited[nnode]:
                    visited[nnode] = t
                    queue.append((nnode,t))
        if len(visited) == N:
            return max(visited.values())
        return -1
    


if __name__ == '__main__':
    s = Solution()
    l = [('A',5),('B',8),('A',100)]
    d = collections.defaultdict(list)
    for s,v in l:
        d[s].append(v)
    
    print(d)
    # print(s.concatenatedBinary(3))

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
