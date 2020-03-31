/*563. Binary Tree Tilt
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入: 
         1
       /   \
      2     3
输出: 1
解释: 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1

注意:

    任何子树的结点的和不会超过32位整数的范围。
    坡度的值不会超过32位整数的范围
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn find_tilt(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0i32;
        fn helper(root: Option<Rc<RefCell<TreeNode>>>,res :&mut i32){
            if let Some(root) = root {
                let mut root=root.borrow_mut(); 
                match (root.left.clone(),root.right.clone()){
                    (None,None)=>(),
                    (None,Some(right))=>{
                        helper(Some(right.clone()),res);
                        root.val+=right.borrow().val;    
                        *res+=right.borrow().val.abs();
                    },
                    (Some(left),None)=>{
                        helper(Some(left.clone()),res);
                        root.val+=left.borrow().val;    
                        *res+=left.borrow().val.abs();
                    },
                    (Some(left),Some(right))=>{
                        helper(Some(left.clone()),res);
                        helper(Some(right.clone()),res);
                        root.val+=left.borrow().val+right.borrow().val;    
                        *res+=(left.borrow().val-right.borrow().val).abs();
                    }
                }
            }
        }
        helper(root,&mut res);
        res
    }
}
