/*572. Subtree of Another Tree
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子

树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2

给定的树 t：

   4 
  / \
 1   2

返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_subtree(s: Option<Rc<RefCell<TreeNode>>>, t: Option<Rc<RefCell<TreeNode>>>) -> bool {
        // 判断两个节点是否相同
        fn is_equal(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>)->bool{
            match(p,q){
                (None,None)=>true,
                (_,None)|(None,_)=>false,
                (Some(p),Some(q))=>{
                    if p.borrow().val==q.borrow().val{
                        is_equal(p.borrow().left.clone(),q.borrow().left.clone()) && is_equal(p.borrow().right.clone(), q.borrow().right.clone())
                    }else{
                        false
                    }
                }
            }
        }

        // 判断子树
        match(s,t){
            (None,None)=>true,
            (_,None)|(None,_)=>false,
            (Some(s),Some(t))=>{
                if is_equal(Some(s.clone()),Some(t.clone())){
                    true
                }else{
                    // 任意子树满足均可                 
                    Solution::is_subtree(s.borrow().left.clone(),Some(t.clone())) || Solution::is_subtree(s.borrow().right.clone(),Some(t.clone()))
                }
            }

        }   
    }
}