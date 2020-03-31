/*700. Search in a Binary Search Tree
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    // 递归
    pub fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(root) = root {
            if root.borrow().val ==val{
                Some(root)
            }else if root.borrow().val>val{
                Solution::search_bst(root.borrow().left.clone(),val)
            }else{
                Solution::search_bst(root.borrow().right.clone(),val)
            }
        }else{
            None
        }
    }
    
    // 迭代
    pub fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let mut root =root;
        while root!=None && root.clone().unwrap().borrow().val !=val{
            if root.clone().unwrap().borrow().val>val{
                root=root.clone().unwrap().borrow().left.clone();
            }else{
                root=root.clone().unwrap().borrow().right.clone();
            }
        }
        root
    }
}
