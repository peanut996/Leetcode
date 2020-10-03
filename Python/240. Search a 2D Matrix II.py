#!/usr/bin/python3.7

# from typing import List
# 240. Search a 2D Matrix II

# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:

# 现有矩阵 matrix 如下：

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == []: return False
    row,col = len(matrix),len(matrix[0])
    t_row,t_col = 0,col-1
    if row > 0 and col > 0:
        while(t_row < row and t_col>=0):
            # print(t_row,t_col)
            if matrix[t_row][t_col] > target:
                t_col -= 1
            elif matrix[t_row][t_col] < target:
                t_row += 1
            else:
                return True
        
    return False


if __name__ == '__main__':

    try:
        matrix = [[]]
        assert exec
    except AssertionError:
        print('解答错误')
