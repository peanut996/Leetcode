#!/usr/bin/python3.7

'''
/**
 * 5311. 将数字变成 0 的操作次数
 * 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
 * */
 '''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        return ( 0 if num==0 else( self.numberOfSteps(num>>1)+1 if num&1 == 0 else self.numberOfSteps(num-1)+1) )
    

def main():
    s=Solution()
    print(s.numberOfSteps(7))

if __name__ == '__main__':
    main()
