/*167. Two Sum II - Input array is sorted
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
*/
struct Solution{

}

impl Solution{
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let length=numbers.len();
        //暴力遍历也可以叫双指针...
        // let mut slow =0; let mut quick:i32=0;
        for i in 0..length {
            for j in i+1..length {
                if numbers[i]+numbers[j]==target{
                    // slow=i as i32;quick=j as i32;
                    return vec![(i+1) as i32,(j+1) as i32];
                }
            }
        }
        return vec![];
    }
}

fn main(){
    let numbers:Vec<i32>=vec![2, 7, 11, 15];
    let target=9;
    println!("{:?}",Solution::two_sum(numbers, target as i32));
    assert_eq!(Solution::two_sum(numbers, target),[1,2])
}