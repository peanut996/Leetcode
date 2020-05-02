#!/usr/bin/python3.7

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res

    def maxDiff(self, num: int) -> int:
        num1 = num
        num2 = num
        num=list(str(num))
        num1=list(str(num1))
        num2=list(str(num2))
        num1_x=9
        num2_x=1
        for i in range(len(num)):
            if num[i]!='9':
                num1_x=num[i]
                break
        for i in range(len(num)):
            if num[i]!='1':
                num2_x=num[i]
                break
        print(num1_x,num2_x)
        for i in range(len(num1)):
            if num1[i]==num1_x:
                num1[i]='9'
        for i in range(len(num2)):
            if num2[i]==num2_x:
                if num2[0]==num2_x:
                    num2[i]='1'
                else:
                    num2[i]='0'

        num1= int(''.join(num1))
        num2= int(''.join(num2))
        return num1-num2
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=list( ord(s) for s in s1)
        s2=list( ord(s) for s in s2)
        s1.sort()
        s2.sort()
        res = []
        for i in range(len(s1)):
            res.append(s1[i]-s2[i])
        print(res)
        r1 = all( i>=0 for i in res)
        r2 = all(i<=0 for i in res)
        result = any([r1,r2])
        return result

if __name__ == '__main__':
    num = 1101057
    num1 = num
    num2 = num
    num=list(str(num))
    num1=list(str(num1))
    num2=list(str(num2))
    num1_x=9
    num2_x=1
    for i in range(len(num)):
        if num[i]!='9':
            num1_x=num[i]
            break
    for i in range(len(num)):
        if num[i]!='1' and num[i]!='0':
            num2_x=num[i]
            break
    for i in range(len(num1)):
        if num1[i]==num1_x:
            num1[i]='9'
    print(num1_x,num2_x)
    tag = ''
    if num2[0] == num2_x:
        tag = '1'
    else:
        tag = '0'
    for i in range(len(num2)):
        if num2[i]==num2_x:
            num2[i]=tag

    
    num1= int(''.join(num1))
    num2= int(''.join(num2))
    print(num1,num2,num2-num1)



    # try:
    #     assert exec
    # except AssertionError:
    #     print('解答错误')
