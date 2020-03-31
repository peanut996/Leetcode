/*66. Plus One
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
*/
#include<iostream>
#include<vector>
#include<assert.h>

class Solution
{
private:
public:
    Solution();
    ~Solution();
	std::vector<int> plusOne(std::vector<int>& digits) {
		for (int i=digits.size()-1;i>=0;i--){
			digits[i]++;
			if (digits[i]%10 !=0){
				return digits;
			}
			digits[i]=0;
		}
		digits.insert(digits.begin(),1);
		return digits;
		
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
	std::vector<int> digits{1,2,3};
	std::vector<int> result{1,2,4};
    Solution* solution = new Solution();
	assert(solution->plusOne(digits)!=result);
    return 0;
}
