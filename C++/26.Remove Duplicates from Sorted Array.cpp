#include<iostream>
#include<vector>
using namespace std;
/*
26.从排序数组中删除重复数据
给定排好序的数组删除重复元素
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int removeDuplicate(vector<int>& nums)
    {
        //双指针i和j
        int i=0;
        if(nums.size()==0) return 0;
        for(int j=1;j<nums.size();j++){
            if(nums[j]!=nums[i]){
                //易错点 双指针中慢指针什么时候自增
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
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
    vector<int> nums({1,1,2,2,3,3});
    cout<<solution->removeDuplicate(nums)<<endl;
    delete solution;
    return 0;
}
