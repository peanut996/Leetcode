#!/usr/bin/python3.7
from typing import List
import collections
from Function import quick_sort
class Solution:
    def interpret(self, command: str) -> str:
        res = command.replace("()", "o")
        res = res.replace("(al)", "al")
        return res

    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        res = 0
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp == k:
                res += 1
                left += 1
                right -= 1
            elif tmp < k:
                left += 1
            else:
                right -= 1
        return res

    def concatenatedBinary(self, n: int) -> str:
        mod = pow(10, 9) + 7

        def helper(n: int):
            if n <= 0:
                return ""
            return helper(n-1)+str(bin(n))[2:]
        return str(int(helper(n), 2) % mod)

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dic = collections.defaultdict(list)
        for u, v, w in times:
            dic[u].append((v, w))
        visited = {K: 0}
        queue = [(K, 0)]
        while queue:
            cnode, ctime = queue.pop(0)
            for nnode, ntime in dic[cnode]:
                t = ctime + ntime
                if nnode not in visited or t < visited[nnode]:
                    visited[nnode] = t
                    queue.append((nnode, t))
        if len(visited) == N:
            return max(visited.values())
        return -1

    def quick_sort(self,alist, start, end):
        """快速排序"""
        if start >= end:  # 递归的退出条件
            return
        mid = alist[start]  # 设定起始的基准元素
        low = start  # low为序列左边在开始位置的由左向右移动的游标
        high = end  # high为序列右边末尾位置的由右向左移动的游标
        while low < high:
            # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
            while low < high and alist[high] >= mid:
                high -= 1
            # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
            alist[low] = alist[high]
            # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
            while low < high and alist[low] < mid:
                low += 1
            # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
            alist[high] = alist[low]

        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
        alist[low] = mid  # 将基准元素放到该位置,
        # 对基准元素左边的子序列进行快速排序
        self.quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
        # 对基准元素右边的子序列进行快速排序
        self.quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后

    def FindCommonElements(self,array1, array2):
        pass

    def maximumGain(self, s: str, x: int, y: int) -> int:
        sub_str1 = 'ab'
        sub_str2 = 'ba'
        blank = ''
        res = 0
        while sub_str1 in s or sub_str2 in s:
            if y > x:
                if sub_str2 in s:
                    s = s.replace(sub_str2, blank,1)
                    res += y
                    continue
                if sub_str1 in s:
                    s = s.replace(sub_str1, blank,1)
                    res += x
            else:
                if sub_str1 in s:
                    s = s.replace(sub_str1, blank,1)
                    res += x
                    continue                
                if sub_str2 in s:
                    s = s.replace(sub_str2, blank,1)
                    res += y                
        
        return res

    def generateMatrix(self, n: int) -> List[List[int]]:
        """[summary]
        59.螺旋矩阵 II

        Args:
            n (int): [description]

        Returns:
            List[List[int]]: [description]
        """
        left,right,top,bottom = 0,n-1,0,n-1
        nums = [[0] * n for _ in range(n)]
        target = n*n
        num = 1
        while num <= target:
            for i in range(left,right+1):
                nums[top][i] = num
                num += 1
            top+=1
            
            for i in range(top,bottom+1):
                nums[i][right] = num
                num += 1
            right -= 1
            
            for i in range(right,left-1,-1):
                nums[bottom][i] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom,top-1,-1):
                nums[i][left] = num
                num += 1
            left += 1
        return nums
                

if __name__ == '__main__':
    
    l = [0,2,4,6,1,3,5]
    quick_sort(l, 0, len(l) - 1)
    print(l)

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
