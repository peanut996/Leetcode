#include<iostream>
#include<vector>
using namespace std;
/*
27.删除元素
就当前数组删除元素且返回之后的数组长度
双指针思路返回数组长度正确但实际并未改变数组
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int removeElement(vector<int>& nums,int val)
    {
        int i=0;
        for (int j=0; j< nums.size(); j++){
            if(nums[j]!=val){
                //易错点 双指针中慢指针什么时候自增
                nums[i]=nums[j];
                i++;
            }
        }
        return i;
    }
};
Solution::Solution(){}
Solution::~Solution(){}
int main(int argc, char* argv[]){
    Solution* solution = new Solution();
    vector<int> nums({1,2,3,3,4,4,5});
    int val=4;
    cout<<solution->removeElement(nums,val)<<endl;
}