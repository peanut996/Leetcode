/*1162. As Far from Land as Possible
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。
*/
impl Solution {
    pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid=grid;
        let n =grid.len() as i32;
        let mut land = Vec::new();
        // 寻找陆地
        for r in (0..n){
            for c in (0..n) {
                if grid[r as usize][c as usize] == 1 {
                    land.push((r,c))
                }
            }
        }
        // 判断是否全为陆地或者海洋
        if land.len()==0 as usize || land.len() ==(n*n) as usize{
            return -1
        }
        // 方向tuple
        let directions= vec![(1,0),(-1,0),(0,1),(0,-1)];
        let mut res=-1;

        while !land.is_empty(){
            res+=1;
            let mut temp = Vec::new();
            for (r,c) in land{
                for (x,y) in &directions{
                    let (nx,ny) = (r+x,c+y);
                    if -1<nx && nx<n &&-1<ny && ny<n && grid[nx as usize][ny as usize]==0 {
                        // 标记为已访问过
                        grid[nx as usize][ny as usize]=-1;
                        temp.push((nx,ny));
                    } 
                }
            }
            land=temp;
        }
        res
    }
}
