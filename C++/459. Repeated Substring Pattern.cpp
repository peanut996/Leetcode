#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*459. Repeated Substring Pattern
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
 */
class Solution
{
private:
public:
    Solution();
    ~Solution();
    bool repeatedSubstringPattern(string s) {
        return (s+s).find(s,1) != s.size();
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
