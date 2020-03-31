use std::rc::Rc;
use std::cell::RefCell;
/*

*/
//Definition for a binary tree node.
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
impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match(p,q){
            (None,None)=>true,
            (None,_)|(_,None)=>false,
            (Some(pr),Some(qr))=>{
                let (pr,qr)=(pr.as_ref(),qr.as_ref());
                let (pr,qr)=(pr.borrow(),qr.borrow());
                if pr.val==qr.val{
                    Self::is_same_tree(pr.left.clone(),qr.left.clone())&&Self::is_same_tree(pr.right.clone(),qr.right.clone())
                }else{
                    false
                }
            }
        }
    }
}
struct Solution{
    
}

impl Solution{
}

fn main(){

}