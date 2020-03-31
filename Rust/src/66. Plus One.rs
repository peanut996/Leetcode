/*66. Plus One
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
*/

pub struct Solution{
}

impl Solution{
	pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
		let mut digits =digits;
		for i in (0..digits.len()).rev(){
			digits[i]+=1;
			if digits[i]%10 !=0{
				return digits;
			}
			digits[i]=0;
		}
		digits.insert(0,1);
		return digits;
    }
}

fn main(){
	let digits =vec![1,2,3];
	let solution= Solution {};
	let result=Solution::plus_one(digits);
	assert_eq!(result,[1,2,4]); 
}