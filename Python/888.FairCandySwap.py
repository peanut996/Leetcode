"""
888. 公平的糖果棒交换
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。

因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。

 

示例 1：

输入：A = [1,1], B = [2,2]
输出：[1,2]
示例 2：

输入：A = [1,2], B = [2,3]
输出：[1,2]
示例 3：

输入：A = [2], B = [1,3]
输出：[2,3]
示例 4：

输入：A = [1,2,5], B = [2,4]
输出：[5,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fair-candy-swap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
      # 暴力 直接 TLE
      """
      res = [0] * 2
      for i in range(len(A)):
          for j in range(len(B)):
              a = A[:]
              b = B[:]
              a[i],b[j] = b[j],a[i]
              if sum(a) == sum(b):
                  res[0],res[1] = A[i],B[j]
                  return res
      return res
      """
      target = (sum(A) + sum(B)) // 2
      set_B = set(B)
      for a in A:
          # b的糖果数量是期望值与a剩余糖果之差
          b = target - (sum(A) - a)
          if b in set_B:
              return [a,b]
      return [] 
