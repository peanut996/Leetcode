/*面试题 04.02. Minimum Height Tree LCCI
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。
示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0 
         / \ 
       -3   9 
       /   / 
     -10  5 
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let length = nums.len();
        if nums.len()==0{
            return None
        }
        if nums.len()==1{
            return Some(Rc::new(RefCell::new(TreeNode::new(nums[0]))))
        }
        let mut middle = length/2;
        let mut head =Some(Rc::new(RefCell::new(TreeNode::new(nums[middle]))));
        head.as_ref().unwrap().borrow_mut().left=Solution::sorted_array_to_bst(nums[..middle].to_vec());
        head.as_ref().unwrap().borrow_mut().right=Solution::sorted_array_to_bst(nums[middle+1..].to_vec());
        head
    }
}
