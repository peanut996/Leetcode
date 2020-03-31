#include<iostream>
#include<vector>
// #include<bits/stdc++.h>
using namespace std;

/**1313.解压缩码
 * [a,b]表示有a个b
 * 每两位展开数组最后合并
 * 如[1,2,3,4]中[1,2]表示1个2，[3,4]表示3个4
 * 最终结果[2,4,4,4]
 * */

class Solution
{
private:
public:
    Solution();
    ~Solution();
    vector<int> decompressRLElist(vector<int>& nums)
    {
        vector<int> result({});
        for (int i=0;i<nums.size(); i+=2){
            for (int j=0;j<nums[i];j++){
                result.push_back(nums[i+1]);
            }
        }

        return result;
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
    vector<int> nums({1,2,3,4});
    vector<int> r(solution->decompressRLElist(nums));
    cout<<"[";
    for(int i=0;i<r.size();i++){
        cout<<r[i];
        if(i!=r.size()-1){
            cout<<",";
        }
    }
    cout<<"] "<<endl;
    delete solution;
    return 0;
}
