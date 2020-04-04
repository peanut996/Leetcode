#include<iostream>
#include <algorithm>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*541. Reverse String II
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"

要求:

    该字符串只包含小写的英文字母。
    给定字符串的长度和 k 在[1, 10000]范围内。

*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    string reverseStr(string s, int k) {
        for(int i=0;i<s.size();i+=2*k){
            if(s.size()-i>k){
                // 可用reverse()代替
                for(int j=i;j<i+k/2;j++){
                    char temp=s[j];
                    s[j]=s[2*i+k-j-1];
                    s[2*i+k-j-1]=temp;
                }
            }else{
                // 可用reverse()代替
                for(int j=i;j<(i+s.size())/2;j++){
                    char temp=s[j];
                    s[j]=s[s.size()-1-j+i];
                    s[s.size()-1-j+i]=temp;
                }
            }
        }
        return s;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    Solution* solution = new Solution();
    string s = "abcdefg";
    int k=2;
    cout<<solution->reverseStr(s,k)<<endl;
}
