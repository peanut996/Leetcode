/*653. Two Sum IV - Input is a BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn find_target(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> bool {
        // 思路：中序遍历得出Vec 然后再遍历数组
        let mut nums =Vec::new();
        // 中序遍历
        fn inorder(root: Option<Rc<RefCell<TreeNode>>>,nums: &mut Vec<i32>){
            if let Some(root) = root {
                inorder(root.borrow().left.clone(), nums);
                nums.push(root.borrow().val as i32);
                inorder(root.borrow().right.clone(), nums);
            }
        }
        inorder(root, &mut nums);
        for i in 0..nums.len(){
            for j in i+1..nums.len(){
                if nums[i]+nums[j]==k {
                    return true;
                }
            }
        }
        false
    }
}