/*1038. Binary Search Tree to Greater Sum Tree
给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。

    注意：该题目与538. Convert BST to Greater Tree相同
*/
impl Solution {
    pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut num =0i32;
        fn inOrder(root: Option<Rc<RefCell<TreeNode>>>, num: &mut i32){
            if let Some(root)=root {
                inOrder(root.borrow().right.clone(), num);
                *num+=root.borrow().val;
                root.borrow_mut().val=*num;
                inOrder(root.borrow().left.clone(), num);
            }
            
        }
        inOrder(root.clone(), &mut num);
        root    
    }
}
