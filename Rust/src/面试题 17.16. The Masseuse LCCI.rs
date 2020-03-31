/*面试题 17.16. The Masseuse LCCI
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

注意：本题相对原题稍作改动
*/
use std::cmp::max;
impl Solution {
    pub fn massage(nums: Vec<i32>) -> i32 {
        // 动态规划 转移方程 
        // dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        // dp[i][1]=dp[i-1][0]+time
        // 只和dp[i-1][0/1]有关 使用两个变量存取即可
        // 另一种做法 dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        let (mut choose,mut not_choose)=(0i32,0i32);
        for num in nums{
            // let (not_choose_copy,choose_copy)=(not_choose,choose);
            // not_choose=max(not_choose_copy,choose_copy);
            // choose=max(not_choose_copy+num,choose_copy);
            (not_choose,choose)=(max(not_choose,choose),max(not_choose+num,choose));
        }
        max(not_choose,choose)
    }
}
