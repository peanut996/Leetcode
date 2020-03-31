/*1022. Sum of Root To Leaf Binary Numbers
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn getSum(root: Option<Rc<RefCell<TreeNode>>>,mut num: i32,res:&mut i32){
            if let Some(root)=root {
                num = (num<<1)+root.borrow().val;
                if root.borrow().left ==None && root.borrow().right ==None{
                    *res+=num;
                }else{
                    getSum(root.borrow().left.clone(),num,res);
                    getSum(root.borrow().right.clone(), num,res);
                }
            }
        }
        let (mut num,mut res)=(0,0);
        getSum(root,num,&mut res);
        res
    }
}