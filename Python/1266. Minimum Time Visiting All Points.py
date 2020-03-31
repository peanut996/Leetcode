#!/usr/bin/python3.7
from typing import List

'''
/**
 * 1266.访问所有点的最短时间
 *  切比雪夫距离
 *  思路：多点距离-两点距离-切比雪夫距离(max(x,y))
 * */
'''
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum([max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))  for i in range(len(points)-1)])


def main():
    points = [[1,1],[3,4],[-1,0]]
    solution=Solution()
    print(solution.minTimeToVisitAllPoints(points))


if __name__ == '__main__':
    main()