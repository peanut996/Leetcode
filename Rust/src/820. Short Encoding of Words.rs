/*820. Short Encoding of Words
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

 

示例：

输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
*/
impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        let mut res=0i32;
        // 字符串翻转
        let mut words: Vec<String> =words.into_iter().map(|word| word.chars().rev().collect::<String>()).collect();
        // 字典排序
        words.sort();
        
        (0..words.len()).for_each(|i| {
            if i+1<words.len() && words[i+1].starts_with(&words[i]){
                res+=0;
            }else{
                res+=words[i].len() as i32+1;
            }
        });
        res
    }
}