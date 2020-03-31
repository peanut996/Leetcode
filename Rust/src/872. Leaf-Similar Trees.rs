/*872. Leaf-Similar Trees
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let (mut nums1,mut nums2) = (Vec::new(),Vec::new());
        fn get_leaf(root: Option<Rc<RefCell<TreeNode>>>,nums :&mut Vec<i32>){
            if let Some(root)=root {
                if root.borrow().left== None && root.borrow().right==None{
                    nums.push(root.borrow().val);
                }else{
                    get_leaf(root.borrow().left.clone(),nums);
                    get_leaf(root.borrow().right.clone(),nums);
                }
            }
        }
        get_leaf(root1,&mut nums1);
        get_leaf(root2,&mut nums2);
        if nums1==nums2{
            return true
        }
        false
    }
}
