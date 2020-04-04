#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>
using namespace std;
/*657. Robot Return to Origin
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

示例 1:
输入: "UD"
输出: true
解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    bool judgeCircle(string moves) {
        int i=0,r=0,c=0;
        while (i < moves.size()) {
            if (moves[i]=='U') c++; 
            if (moves[i]=='D') c--; 
            if (moves[i]=='L') r--; 
            if (moves[i]=='R') r++; 
            i++;
        }
        return r==0 & c==0;
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
