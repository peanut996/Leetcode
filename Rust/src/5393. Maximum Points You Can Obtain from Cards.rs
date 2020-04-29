/*5393. Maximum Points You Can Obtain from Cards
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
*/

impl Solution {
    pub fn max_score(card_points: Vec<i32>, k: i32) -> i32 {
        let n:i32=card_points.len() as i32;
        let mut max = 0i32;
        let s:i32 = card_points.iter().sum();
        for i in 0..=k{
            let t :i32 =card_points[i as usize..(i+n-k) as usize].iter().sum();
            if max < (s-t){
                max = s-t; 
            }
    
        }
        max
    }    
}