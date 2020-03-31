#include<iostream>
// #include<bits/stdc++.h>
using namespace std;

/**
 * 5311. 将数字变成 0 的操作次数
 * 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
 * */
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int numberOfSteps (int num) {
        return num==0 ? 0 : (num%2 ==0 ?  1+numberOfSteps(num>>1): 1+numberOfSteps(num-1));
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    Solution* s =new Solution();
    cout<<s->numberOfSteps(14)<<endl;
    return 0;
}
