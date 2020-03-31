/*914. X of a Kind in a Deck of Cards
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

示例:
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

*/
impl Solution {
    pub fn has_groups_size_x(deck: Vec<i32>) -> bool {
        let mut nums: Vec<i32> = (1..=10000).map(|_| 0).collect();
        let length = deck.len();
        for (_,v) in deck.iter().enumerate(){
            nums[*v as usize]+=1;
        }
        for i in (2..=length) {
            if length%i==0{
                if nums.iter().all(|&x| x%(i as i32) == 0){
                    return true
                }
            }
        }
        false
    }
}
