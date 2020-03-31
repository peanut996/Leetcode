/*94. Binary Tree Inorder Traversal
给定一个二叉树，返回它的中序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut nums=Vec::new();
        fn inOrder(root: Option<Rc<RefCell<TreeNode>>>,nums :&mut Vec<i32>){
            if let Some(root)=root {
                inOrder(root.borrow().left.clone(), nums);
                nums.push(root.borrow().val);
                inOrder(root.borrow().right.clone(), nums);
            }
            
        }
        inOrder(root, &mut nums);
        nums
    }
}
