/*538. Convert BST to Greater Tree
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn convert_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut num =0i32;
        fn inOrder(root: Option<Rc<RefCell<TreeNode>>>, num:&mut i32){
            if let Some(root)=root {
                inOrder(root.borrow().right.clone(), num);
                *num+=root.borrow().val;
                root.borrow_mut().val=*num;
                inOrder(root.borrow().left.clone(), num);
            }
            
        }
        inOrder(root.clone(), &mut num);
        root    
    }
}