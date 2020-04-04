#include<iostream>
#include <algorithm>
using namespace std;
/*696. Count Binary Substrings
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。
*/

class Solution
{
private:
public:
    Solution();
    ~Solution();
    int countBinarySubstrings(string s) {
        // 思路：Group每个数字重复出现的次数，然后min(group[i],group[i-1])满足，累加即可
        // 这里采用两个指针记录group[-2],group[-1],及时更新
        int res=0,prev=0,curr=1;
        for (int i = 1;i < s.size();i++) {
            if (s[i] != s[i-1]) {
                res+=min(curr,prev);
                prev = curr;
                curr = 1;
            } else {
                curr++;
            }
        }
        return res + min(curr,prev);
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
}
