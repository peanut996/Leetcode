#!/usr/bin/python3.7
# 剑指 Offer 57 - II. 和为s的连续正数序列
from typing import List


def findContinuousSequence(self, target: int) -> List[List[int]]:
    left,right,res = 1,2,[]
    while right <= target//2 +1:
        cur_sum = sum(list( i for i in range(left,right+1)))
        if cur_sum < target: right += 1
        if cur_sum > target: left += 1
        if cur_sum == target:
            res.append(list(range(left,right+1)))
            left += 1
    return res

# 暴力速度还快一点
# def findContinuousSequence(self, target: int) -> List[List[int]]:
#     slow,quick,temp=0,0,0
#     queue=[i+1 for i in range(target)]
#     result=[]
#     for i in range(len(queue)-1):
#         slow,quick=i,i+1
#         temp=queue[slow]+queue[quick]
#         while temp<target:
#             quick+=1
#             temp+=queue[quick]
#         if temp==target:
#             result.append(queue[slow:quick+1])
#     return result

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')


