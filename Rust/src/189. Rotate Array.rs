/*189. Rotate Array
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
*/
struct Solution{

}

impl Solution{
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k = k as usize;
        let length=nums.len();
        let mut new:Vec<i32> =(0..length).map(|_| 0).collect();
        for i in 0..length{
            new[(i+k)%length]=nums[i];
        }
        for i in 0..length{
            nums[i]=new[i];
        }
    }
}

fn main(){
    let mut nums=vec![1,2,3,4,5,6,7];let k=3;
    Solution::rotate(&mut nums,k);
    assert_eq!(nums,vec![5,6,7,1,2,3,4]);
}