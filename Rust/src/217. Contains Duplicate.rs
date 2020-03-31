/*217. Contains Duplicate
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例:
输入: [1,2,3,1]
输出: true

*/
struct Solution{

}

impl Solution{
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let length = nums.len();
        for i in 0..length{
            let temp=nums[i];
            for j in i+1..length{
                if temp==nums[j]{
                    return true;
                }
            }
        }
        return false;
    }
}

fn main(){
    let nums=vec![1,2,3,1];
    assert_eq!(Solution::contains_duplicate(nums),true);
}