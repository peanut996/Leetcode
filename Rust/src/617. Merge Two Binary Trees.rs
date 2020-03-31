/*617. Merge Two Binary Trees
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

注意: 合并必须从两个树的根节点开始。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn merge_trees(t1: Option<Rc<RefCell<TreeNode>>>, t2: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        // 思路： 递归合并
        // 可变借用 原地修改t1
        fn merge_trees_mutable(t1: &mut Option<Rc<RefCell<TreeNode>>>, t2: &Option<Rc<RefCell<TreeNode>>>){
            match (t1.clone(),t2.clone()){
                (None,None)|(_,None)=>(),
                (None,t2)=>{
                    *t1=t2.clone();
                },
                (Some(t1),Some(t2))=>{
                    let mut t1=t1.borrow_mut();
                    t1.val+=t2.borrow().val;
                    merge_trees_mutable(&mut t1.left, &t2.borrow().left);
                    merge_trees_mutable(&mut t1.right, &t2.borrow().right);
                }
            }
        }
        let mut t1=t1;
        merge_trees_mutable(&mut t1, &t2);
        t1
    }
}