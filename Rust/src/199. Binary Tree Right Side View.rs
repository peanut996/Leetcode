/*199. Binary Tree Right Side View

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
*/
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        // 思路：BFS：层次遍历取最后一个 DFS：root(判断res数组长度)->右结点->左结点 
        let mut res: Vec<i32> = vec![];
        let mut depth:usize = 0;
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>,depth: usize,res: &mut Vec<i32>){
            if let Some(root) = root {
                if depth == res.len(){
                    res.push(root.borrow().val);
                }
                dfs(root.borrow().left.clone(), depth+1, res);
                dfs(root.borrow().right.clone(), depth+1, res);
            }
        }
    
        dfs(root,depth,&mut res);
        res
    }
}