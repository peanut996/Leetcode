#!/usr/bin/python3.7
from typing import List

'''
/**1313.解压缩码
 * [a,b]表示有a个b
 * 每两位展开数组最后合并
 * 如[1,2,3,4]中[1,2]表示1个2，[3,4]表示3个4
 * 最终结果[2,4,4,4]
 * */
'''
class Solution:
    def decompressRLElist(self, nums:List[int]) -> List[int]:
        result=[]
        for i in range(len(nums))[::2]:
            for j in range(nums[i]):
                result.append(nums[i+1])
        return result


def main():
    nums=[1,2,3,4]
    solution=Solution()
    print(solution.decompressRLElist(nums))


if __name__ == '__main__':
    main()