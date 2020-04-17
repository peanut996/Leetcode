#!/usr/bin/python3.7
# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

# 不占用额外内存空间能否做到？

 

# 示例 1:

# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 思路 先翻转再解压(相当于沿着对称轴旋转)
        matrix[:]=zip(*reversed(matrix)) 

def main():
    solution = Solution()
    try:
        assert exec
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
