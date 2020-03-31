/*606. Construct String from Binary Tree
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例:
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn tree2str(t: Option<Rc<RefCell<TreeNode>>>) -> String {
        if let Some(t) = t {
            let t = t.borrow();
            match (t.left.clone(),t.right.clone()){    
                (None,None)=>t.val.to_string(),
                (left,None)=>{
                    t.val.to_string()+"("+&Solution::tree2str(left)+")"
                },
                (None,right)=>{
                    t.val.to_string()+"()"+"("+&Solution::tree2str(right)+")"
                },
                (left,right)=>{
                    t.val.to_string()+"("+&Solution::tree2str(left)+")"+"("+&Solution::tree2str(right)+")"
                }
            }
        }else{
            String::from("")
        }
    }
}
