"""面试题 10.01. Sorted Merge LCCI
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。
"""

from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        C=A[:m]+B[:n]
        C.sort()
        A[:]=C



def main():
    A=[1,2,6,0,0,0]
    B=[2,3,4]
    m,n=3,3
    solution=Solution()
    solution.merge(A,m,B,n)
    assert A==[1, 2, 2, 3, 4, 6]


if __name__ == '__main__':
    main()