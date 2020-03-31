/*219. Contains Duplicate II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
*/
struct Solution{

}

impl Solution{
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let k =k as usize;
        let length = nums.len();
        for i in 0..length{
            let temp=nums[i];
            for j in i+1..length{
                if temp==nums[j] && j-i<=k{
                    return true;
                }
            }
        }
        return false;
    }
}

fn main(){
    let nums=vec![1,2,3,1,2,3];let k=2;
    assert_eq!(Solution::contains_nearby_duplicate(nums,k),false);
}