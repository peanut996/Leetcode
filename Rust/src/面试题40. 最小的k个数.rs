/*面试题40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

*/

impl Solution {
    pub fn get_least_numbers(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let mut arr =arr;
        arr.sort_unstable();
        arr=arr[..k as usize].to_vec();
        arr
    }
}
