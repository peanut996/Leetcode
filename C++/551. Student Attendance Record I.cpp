#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*551. Student Attendance Record I
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

    'A' : Absent，缺勤
    'L' : Late，迟到
    'P' : Present，到场

如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:
输入: "PPALLP"
输出: True
示例 2:
输入: "PPALLL"
输出: False
示例 3:
输入: "LLPPALL"
输出: True
*/

class Solution
{
private:
public: 
    Solution();
    ~Solution();
    bool checkRecord(string s) {
        int L=0,A=0;
        A += s[0] == 'A' ? 1 : 0;
        A += s[1] == 'A' ? 1 : 0;
        for (int i = 2; i < s.size(); ++i) {
            if (s[i] == 'A') A++;
            if (s[i] == 'L' & s[i-1] == 'L'& s[i-2] == 'L') L++;
        }
        return A <= 1 & L < 1;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    string s = "PPALLL";
    Solution* solution = new Solution();
    cout<<solution->checkRecord(s)<<endl;
}
