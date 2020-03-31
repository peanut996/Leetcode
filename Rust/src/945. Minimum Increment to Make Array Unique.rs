/*945. Minimum Increment to Make Array Unique
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。

示例:
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
*/


impl Solution {
    pub fn min_increment_for_unique(a: Vec<i32>) -> i32 {
        // 思路：排序再遍历
        let mut a =a;
        let mut res=0i32;
        a.sort();
        for i in 0..a.len(){
            if a[i]<=a[i-1]{
                res+=a[i-1]-a[i]+1;
                a[i]=a[i-1]+1;
            }
        }
        res
    }
}
