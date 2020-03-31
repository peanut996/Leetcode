/*671. Second Minimum Node In a Binary Tree
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:

输入: 
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
*/

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn find_second_minimum_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        // 递归思路十分巧妙，因为根节点为最小，要么子节点为空要么比根节点大，找出子节点较小的即可
        if let Some(root) = root {
            match(root.borrow().left.clone(),root.borrow().right.clone()){
                (None,None)|(_,None)|(None,_)=>-1,
                (Some(left),Some(right))=>{
                    // 候选值
                    let (mut l,mut r)=(left.borrow().val,right.borrow().val);
                    // 若相同，递归找下去第二小的结点
                    if (root.borrow().val==l){
                        l=Solution::find_second_minimum_value(Some(left))
                    }
                    if (root.borrow().val==r){
                        r=Solution::find_second_minimum_value(Some(right))
                    }
                    if l!=-1 && r!=-1 {
                        return l.min(r)
                    }
                    if  l!=-1{
                        return l;
                    }else{
                        // l为-1，若r为-1，或者不为-1都返回
                        return r;
                    }
                }        
            }
        }else{
            -1
        }
    }
}
}