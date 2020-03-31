/*268. Missing Number
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例:
输入: [3,0,1]
输出: 2
*/
struct Solution{

}

impl Solution{
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut new :Vec<i32>=nums;
        let length = new.len();
        //排序 不存在重复元素所以使用unstable
        new.sort_unstable();
        for i in 0..length {
            if new[i]!=(i as i32){
                return i as i32;
            }
        }
        //若前面都没有缺少 默认为最后一个
        return length as i32;
    }
}

fn main(){
    let nums=vec![3,0,1];
    assert_eq!(Solution::missing_number(nums),2);
}