#include<iostream>
#include <algorithm>
using namespace std;
/*686. Repeated String Match
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
*/

class Solution
{
private:
public:
    Solution();
    ~Solution();
    int repeatedStringMatch(string A, string B) {
        int res=1;
        // 注意终止位置为B+2A,分3种情况讨论
        for (string ACopy = A; ACopy.size() <= B.size() + 2*A.size(); ACopy+=A,++res) {
            if (ACopy.find(B) != string::npos) return res;
        }
        return  -1;
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
