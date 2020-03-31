/*669. Trim a Binary Search Tree
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例:

输入:
    1
   / \
  0   2

  L = 1
  R = 2

输出:
    1
      \
       2

*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn trim_bst(root: Option<Rc<RefCell<TreeNode>>>, l: i32, r: i32) -> Option<Rc<RefCell<TreeNode>>> {
        fn trim(root: Option<Rc<RefCell<TreeNode>>>,l: i32, r: i32) ->Option<Rc<RefCell<TreeNode>>>{
        // let trim =|root: Option<Rc<RefCell<TreeNode>>>|{
            if let Some(root) =root{
                let mut root  = root.borrow_mut();
                if root.val > r {
                    return trim(root.left,l ,r);
                }else if root.val < l{
                    return trim(root.right,l ,r);
                }else{
                    root.left=trim(root.left,l ,r);
                    root.right=trim(root.right,l ,r);
                }
            }
            root
        };
        trim(root,l ,r)
    }
}