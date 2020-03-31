/*637. Average of Levels in Binary Tree
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例:
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

注意：
    节点值的范围在32位有符号整数范围内。
*/

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        // 思路BFS 收集sum和count 并传递到res数组
        let mut res:Vec<f64>=Vec::new();
        let (mut sum,mut count)=(0.0,0.0);
        let mut queue:Vec<Option<Rc<RefCell<TreeNode>>>>=Vec::new();
        queue.push(root);
        while !queue.is_empty() {
            // 临时队列
            let mut temp:Vec<Option<Rc<RefCell<TreeNode>>>>=Vec::new();
            while !queue.is_empty() {
                if let Some(node) =queue.pop(){
                    let node=node.as_ref().unwrap().borrow();
                    sum+=node.val as f64;
                    count+=1.0;
                    if let Some(left)=node.left.clone(){
                        temp.push(Some(left));
                    }
                    if let Some(right)=node.right.clone(){
                        temp.push(Some(right));
                    }
                };
            }
            res.push(sum/count);
            queue=temp;
            sum=0.0;count=0.0;
        }
        res
    }
}