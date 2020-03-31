#include <bits/stdc++.h>
using namespace std;
/*
35.

*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int searchInsert(vector<int>& nums,int target)
    {
        //寻找数组是否含有target或者target位置
        for (int i=0; i<nums.size(); i++){
            if (nums[i]>=target)
                return i;
        }
        
        //若target大于数组所有值则返回数组长度
        return nums.size();
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
    vector<int> nums({1,2,4,5});
    int target = 3;
    cout<<solution->searchInsert(nums,target)<<endl;
    delete solution;
    return 0;
}
