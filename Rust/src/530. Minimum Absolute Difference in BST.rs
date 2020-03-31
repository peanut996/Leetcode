/*530. Minimum Absolute Difference in BST
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
输入：

   1
    \
     3
    /
   2

输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut nums=Vec::new();
        let mut res=i32::max_value();
        // 二叉树中序遍历
        fn inOrder(root: Option<Rc<RefCell<TreeNode>>>,nums :&mut Vec<i32>){
            if let Some(root)=root {
                inOrder(root.borrow().left.clone(), nums);
                nums.push(root.borrow().val);
                inOrder(root.borrow().right.clone(), nums);
            }
            
        }
        inOrder(root, &mut nums);
        for i in (1..nums.len()).iter(){
            if nums[i]-nums[i-1]<res{
                res=nums[i]-nums[i-1]
            }
        }
        res
    }
}
