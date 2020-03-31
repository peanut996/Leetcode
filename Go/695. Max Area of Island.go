package main

/*695. Max Area of Island
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
岛屿和岛屿相连接可组成大的岛屿，也就是说这题求的是上下左右四个方向相连接起来的最大规模，搜索问题
示例:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
*/

func maxAreaOfIsland(grid [][]int) int {
	area, maxarea := 0, 0

	//i表示纵向坐标，j表示横向坐标
	for i := range grid {
		for j := 0; j < len(grid[i]); j++ {
			area = getArea(grid, i, j)
			if maxarea < area {
				maxarea = area
			}
		}
	}
	return maxarea
}

func getArea(grid [][]int, i, j int) int {
	if i < 0 || j < 0 || i == len(grid) || j == len(grid[i]) {
		return 0
	}
	if grid[i][j] == 1 {
		grid[i][j] = 0
		//DFS
		return 1 + getArea(grid, i+1, j) + getArea(grid, i-1, j) + getArea(grid, i, j+1) + getArea(grid, i, j-1)
	}
	return 0
}
