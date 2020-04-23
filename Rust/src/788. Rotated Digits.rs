/*788. Rotated Digits

我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

 

示例：

输入: 10
输出: 4
解释: 
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。
*/
struct Solution{

}

impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        // 思路 在(0,1,2,5,6,8,9)且必有一位(2,5,8,9)
        let mut res=0i32;
        let nums1=vec!['0','1','2','5','6','8','9'];
        let nums2=vec!['2','5','6','9'];
        for i in 0..=n{
            let s = i.to_string();
            let temp= s.chars();
            // if temp.all(|e| nums1.contains(&e)) && temp.any(|e| nums2.contains(&e)){
            if temp.clone().all(|e| nums1.contains(&e)) && temp.clone().any(|e| nums2.contains(&e)){
                res+=1;
            }
        }
        res
    }
}

fn main(){
    let n = 10i32;
    let res = Solution::rotated_digits(n);
    assert_eq!(4i32,res);
}