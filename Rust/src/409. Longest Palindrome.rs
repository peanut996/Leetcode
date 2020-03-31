/*409. Longest Palindrome
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。

示例:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
*/

pub struct Solution{
}

impl Solution{
    pub fn longest_palindrome(s: String) -> i32 {
        // 根据ascii码存字典 也可以只初始化一个26+26的数组
        let mut chardict =vec![0i32;128];
        for b in s.bytes(){
            chardict[b as usize]+=1;
        }
        let mut res=0i32;
        for i in chardict {
            // 只添加一次中间元素
            if i%2!=0&& res%2==0{
                res+=1
            }
            res+=(i/2i32)*2i32;
        }
        res
    }
}

fn main(){
    let s=String::from("abccccdd");
    assert_eq!(Solution::longest_palindrome(s),7);
}