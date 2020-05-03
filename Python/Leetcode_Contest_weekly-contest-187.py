#!/usr/bin/python3.7

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
      city_start = set( path[0] for path in paths)
      city_end = set( path[1] for path in paths)
      return list(city_end-city_start)[0]


    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distances = []
        try:
            first = nums.index(1)
        except:
            return k==0
        slow,quick=first,first+1
        while quick < len(nums):
            if nums[quick]==1: 
                distances.append(quick-slow-1)
                slow=quick
            quick+=1
        print(distances)
        return all( distance>=k  for distance in distances)
    

    def longestSubarray(self, nums: [int], limit: int) -> int:
        n=len(nums)
        i,j=0,0
        maxs=0
        mins=10**5
        res=0#返回长度
        while j<n:
            if nums[j]>maxs:
                maxs=nums[j]
            if nums[j]<mins:
                mins=nums[j]
            while i<j and maxs-mins>limit:
                if maxs==nums[i]:
                    maxs=max(nums[i+1:j+1])
                elif mins==nums[i]:
                    mins=min(nums[i+1:j+1])
                i += 1
            res = max(res, (j - i)+1)
            j+=1
        return res    

if __name__ == '__main__':
    try:
        solution = Solution()
        # paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        # paths = [["B","C"],["D","B"],["C","A"]]
        # paths = [["A","Z"]]
        # solution.destCity(paths)
        # nums = [1,1,1,1,1]
        # k = 2
        
        limit = 4
    except AssertionError:
        print('解答错误')
