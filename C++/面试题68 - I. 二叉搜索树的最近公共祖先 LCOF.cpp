#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>


/*面试题68 - I. 二叉搜索树的最近公共祖先 LCOF
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
*/
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution
{
private:
public:
    Solution();
    ~Solution();
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p->val<root->val&&q->val<root->val){
            return lowestCommonAncestor(root->left,p,q);
        }
        if(p->val>root->val&&q->val>root->val){
            return lowestCommonAncestor(root->right,p,q);
        }
        return root;
    }
};

Solution::Solution()
{
}

Solution::~Solution()
{
}
