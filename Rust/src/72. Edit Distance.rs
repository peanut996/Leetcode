/*72. Edit Distance
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符
示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
*/
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        // 动态规划经典面试题
        let (m,n) = (word1.len(),word2.len());
        let mut dp:Vec<Vec<usize>>=vec![vec![0;n+1];m+1];
        for i in 0..m+1{
            dp[i][0]=i;
        }
        for j in 0..n+1{
            dp[0][j]=j;
        }
        let (b1,b2) = (word1.into_bytes(),word2.into_bytes());
        for i in 1..m+1{
            for j in 1..n+1{
                if b1[i-1] == b2[j-1]{
                    dp[i][j]=dp[i-1][j-1];
                }else{
                    dp[i][j]=(dp[i-1][j].min(dp[i][j-1])).min(dp[i-1][j-1])+1;
                }
            }
        }
        dp[m][n] as i32
    }
}