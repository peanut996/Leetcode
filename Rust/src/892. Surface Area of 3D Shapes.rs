/*892. Surface Area of 3D Shapes
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例：
输入：[[1,2],[3,4]]
输出：34

*/
impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        // 思路:先计算每个总面积，再减去被重叠的部分
        // 亮点:只需要处理左边和下边的柱体
        let length=grid.len();
        let mut area =0i32;
        for i in 0..n{
            for j in 0..n{
                let level = grid[i][j];
                if level > 0{
                    area+=level*4+2;
                    if i>0 {
                        area-=level.min(grid[i-1][j])*2;
                    }
                    if j>0 {
                        area-=level.min(grid[i][j-1])*2;
                    }
                } 
            }
        }
        area
    }
}
