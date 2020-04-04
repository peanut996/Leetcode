#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*680. Valid Palindrome II
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    bool validPalindrome(string s) {
        auto isPalindrome = [&s](int i,int j) -> bool {
            while (i < j) if (s[i++] != s[j--]) return false;
            return true;
        };
        int l=0,r=s.size()-1;
        while (l < r) {
            if (s[l] != s[r]) return isPalindrome(l+1,r) || isPalindrome(l,r-1);
            l++;r--;
        }
        return true;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    string s = "aba";
    Solution* solution = new Solution();
    cout << solution->validPalindrome(s) << endl;
}
