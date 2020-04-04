#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*709. To Lower Case
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例：
输入: "Hello"
输出: "hello"
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    string toLowerCase(string str) {
        for (char &c : str) {
            if (c >= 65 && c <= 90) {
                c+=32;
            }
        }
        return str;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    string s = "Hello";
    Solution* solution = new Solution();
    cout << solution->toLowerCase(s) << endl;
}
