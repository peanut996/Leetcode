/*118. Pascal's Triangle
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

示例：
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
struct Solution{

}

impl Solution{
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut result=Vec::with_capacity(num_rows as usize);
        for i in 0..num_rows as usize{

            
            let mut v:Vec<i32>=(0..i+1).map(|_| 1).collect();
            
            if i > 0{
                for j in 1..i{
                    let lastrow:&Vec<i32> =&result[i-1];
                    v[j]=lastrow[j-1]+lastrow[j];
                }
            }
            result.push(v);
        }
        result
    }
}

fn main(){
    let num_rows = 5;
    let result:Vec<Vec<i32>>=Solution::generate(num_rows);
    // for i in result {
    //     println!("----------");
    //     for j in i{
    //         println!("{}",j);
    //     }
    // }
    assert_eq!(result,vec![vec![1], vec![1, 1], vec![1, 2, 1], vec![1, 3, 3, 1], vec![1, 4, 6, 4, 1]])
}