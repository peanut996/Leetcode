/*687. Longest Univalue Path
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5

输出:

2
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn longest_univalue_path(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn helper(root: Option<Rc<RefCell<TreeNode>>>,res: &mut i32)->i32{
            if let Some(root) = root {
                // let (mut left,mut right)=(root.borrow().left.as_ref().unwrap().borrow().val,root.borrow().right.as_ref().unwrap().borrow().val);
                let (mut left,mut right)=(helper(root.borrow().left.clone(),res),helper(root.borrow().right.clone(),res));
                if let Some(l) = root.borrow().left.clone() {
                    if l.borrow().val == root.borrow().val{
                        left+=1
                    }else{
                        left=0
                    }
                }else{
                    left=0
                }
                if let Some(r) = root.borrow().right.clone() {
                    if r.borrow().val == root.borrow().val{
                        right+=1
                    }else{
                        right=0
                    }
                }else{
                    right=0
                }
                *res=(*res).max(left+right);
                left.max(right)
            }else{
                0
            }
        }
        let mut res=0i32;
        helper(root, &mut res);
        res
    }
}