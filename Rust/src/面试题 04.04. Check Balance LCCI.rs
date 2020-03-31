/*面试题 04.04. Check Balance LCCI
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn depth(root: Option<Rc<RefCell<TreeNode>>>)-> i32{
            if let Some(root) = root {
                let left = depth(root.borrow().left.clone()); 
                let right = depth(root.borrow().right.clone());
                left.max(right)+1 
            }else{
                0
            }
        }

        if let Some(root) = root {
            if (depth(root.borrow().left.clone())-depth(root.borrow().right.clone())).abs()>1{
                false
            }else{
                Solution::is_balanced(root.borrow().left.clone())&&Solution::is_balanced(root.borrow().right.clone())
            }
        }else{
            true
        }
        
    }
}
