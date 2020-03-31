/*1013. Partition Array Into Three Parts With Equal Sum
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
*/
struct Solution{

}

impl Solution {
    pub fn can_three_parts_equal_sum(a: Vec<i32>) -> bool {
        let sum = a.iter().sum::<i32>() as usize;
        if sum%3 !=0{
            return false;
        }
        let  (mut left,mut right,mut leftsum,mut rightsum)=(0,a.len()-1,0,0);
        let  (mut leftsum,mut rightsum)=(a[left] as usize,a[right] as usize);
        while left+1<right{
            if leftsum==sum/3 && rightsum==sum/3{
                return true;
            }
            if leftsum!=sum/3 {
                left+=1;
                leftsum+=a[left] as usize;
            }
            if rightsum!=sum/3{
                right-=1;
                rightsum+=a[right] as usize;
            } 
        }
        return false;
    }
}

fn main(){
    assert_eq!(Solution::can_three_parts_equal_sum(vec![0,2,1,-6,6,7,9,-1,2,0,1]),false);   
}