/*783. Minimum Distance Between BST Nodes
给定一个二叉搜索树的根结点 root，返回树中任意两节点的差的最小值。

 

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树结点对象(TreeNode object)，而不是数组。

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
