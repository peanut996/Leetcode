#include<iostream>
#include<algorithm>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*557. Reverse Words in a String III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
*/

class Solution
{
private:
public:
    Solution();
    ~Solution();
    string reverseWords(string s) {
        int length=s.size(), i=0,tag=0;
        while(i<length){
            while(i<length && s[i]==' ') i++;
            tag=i;
            if(i==length) return s;
            while(i<length && s[i]!=' ') i++;
            // 注意两边界限，并不是下标
            reverse(s.begin()+tag,s.begin()+i);
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
    string s = "Let's take LeetCode contest";
    Solution* solution = new Solution();
    cout<<solution->reverseWords(s)<<endl;
}
