#include<iostream>
// #include<exception>
// #include<assert.h>
// #include<bits/stdc++.h>

/*面试题68 - II. 二叉树的最近公共祖先 LCOF
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
*/
class Solution
{
private:
public:
    Solution();
    ~Solution();
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root==NULL|| p==root || q==root){
            return root;
        }
        TreeNode* left = lowestCommonAncestor(root->left,p,q);
        TreeNode* right = lowestCommonAncestor(root->right,p,q);

        if (left==NULL){
            return right;
        }else if (right==NULL){
            return left;
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

int main(int argv,char** argc){
}
