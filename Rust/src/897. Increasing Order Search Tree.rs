/*897. Increasing Order Search Tree
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn increasing_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn inorder(root: Option<Rc<RefCell<TreeNode>>>,nums :&mut Vec<i32>){
            if let Some(root)=root {
                inorder(root.borrow().left.clone(), nums);
                nums.push(root.borrow().val);
                inorder(root.borrow().right.clone(),nums);
            }
        }
        let mut nums: Vec<i32>=Vec::new();
        inorder(root,&mut nums);
        let mut curr =Some(Rc::new(RefCell::new(TreeNode::new(0)))).clone();
        let mut head=curr.clone();
        for i in nums{
            curr.as_ref().unwrap().borrow_mut().right=Some(Rc::new(RefCell::new(TreeNode::new(i))));
            curr=curr.clone().unwrap().borrow().right.clone();
        }
        head=head.clone().unwrap().borrow().right.clone();
        head
    }
}