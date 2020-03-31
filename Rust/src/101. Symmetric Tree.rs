/*101. Symmetric Tree
给定一个二叉树，检查它是否是镜像对称的。


*/
struct Solution{

}

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn is_mirror(p: Option<Rc<RefCell<TreeNode>>>,q: Option<Rc<RefCell<TreeNode>>>)->bool{
            match(p,q){
                (None,None)=>true,
                (_,None)|(None,_)=>false,
                (Some(l),Some(r))=>{
                    return {
                        l.borrow().val==r.borrow().val 
                        && is_mirror(l.borrow().left.clone(),r.borrow().right.clone())
                        && is_mirror(l.borrow().right.clone(),r.borrow().left.clone())
                    }
                }
            }
        }
        match root{
            None=>true,
            Some(root)=>is_mirror(root.borrow().left.clone(),root.borrow().right.clone())
        }
    }
}


fn main(){
    let root =Rc::new(RefCell::new(TreeNode::new(0)));
    root.borrow_mut().left=Some(Rc::new(RefCell::new(TreeNode::new(1))));
    root.borrow_mut().right=Some(Rc::new(RefCell::new(TreeNode::new(1))));
    // stack overflow
    // root.borrow_mut().left=Some(root.clone());
    // root.borrow_mut().right=Some(root.clone());
    assert_eq!(Solution::is_symmetric(Some(root)),true);
}