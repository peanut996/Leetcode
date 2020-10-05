#!/usr/bin/python3.7
# 剑指 Offer 50. 第一个只出现一次的字符
# from typing import List

def firstUniqChar(self, s: str) -> str:
    str_dict = dict()
    for i in s:
        if i not in str_dict.keys():
            str_dict[i] = 1
        else:
            str_dict[i] += 1
    for k,v in str_dict.items():
        if v == 1:return k
    if 1 not in str_dict.values(): return ' '

    # python 字典默认有序 判断键是否存在赋值bool类型 
    # dic = {}
    # for c in s:
    #     dic[c] = not c in dic
    # for k, v in dic.items():
    #     if v: return k
    # return ' '

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
