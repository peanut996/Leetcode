/*面试题 08.11. Coin LCCI
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
*/

impl Solution {
    pub fn ways_to_change(n: i32) -> i32 {
        let n = n as usize;
        let coins:Vec<usize> = vec![25,10,5,1];
        let mut dp:Vec<usize> = vec![0;n+1];

        // base case
        //刚好可以用一个硬币凑成的情况，是一种情况
        // while i == coin :
        //  dp[i] = dp[i - coin] => dp[0]
        dp[0]=1;

        /**
         * 状态转移方程 dp[i]+=dp[i]+dp[i-coin]
         */
        // coin放到外层循坏是为了防止dp[6]的[1,5]和[5,1]颠倒情况
        for coin in coins{
            for i in coin..=n{
                let i = i as usize;
                dp[i]=(dp[i]+dp[i-coin as usize])%1000000007
            }
        }
        dp[n] as i32
    }
}