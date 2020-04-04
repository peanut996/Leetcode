#include<iostream>
#include<vector>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*42. Trapping Rain Water
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int trap(vector<int>& height){
        if (height.empty()) return 0;
        int n = height.size();
        int left = 0,right = n-1,res = 0;
        int l_max = height[0],r_max = height[n-1];
        while (left <= right) {
            l_max=max(l_max,height[left]);
            r_max=max(r_max,height[right]);
            // res=min(l_max,r_max) - height[i]
            if (l_max < r_max) {
                res += l_max - height[left];
                left++;
            } else {
                res += r_max - height[right];
                right--;
            }
        }
        return res;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}

int main(int argv,char** argc){
    vector<int> height({0,1,0,2,1,0,1,3,2,1,2,1});
    Solution* solution = new Solution();
    cout<<solution->trap(height)<<endl;
}
