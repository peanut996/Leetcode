#include<iostream>
#include<vector>
#include<math.h>
// #include<bits/stdc++.h>
using namespace std;

/**
 * 1266.访问所有点的最短时间
 *  切比雪夫距离
 *  思路：多点距离-两点距离-切比雪夫距离(max(x,y))
 * */
class Solution
{
private:
public:
    Solution();
    ~Solution();
    int minTimeToVisitAllPoints(vector<vector<int>>& points)
    {
        int sum=0;
        for (int i=0;i<points.size()-1;i++){
            sum+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]));
        }
        return sum;
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
    vector<vector<int>> points({{1,1},{3,4},{-1,0}});
    cout<<solution->minTimeToVisitAllPoints(points)<<endl;
    delete solution;
    return 0;
}
