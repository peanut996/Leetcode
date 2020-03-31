/*876. Middle of the Linked List
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

示例：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
*/
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // 思路1：结点进数组，取数组len()/2元素
        // 思路2：遍历两遍链表，第一遍记录长度，第二遍遍历到len()/2位置 
        // 思路3：快慢指针，slow走一步，quick走两步
        let (slow,quick)=(head.clone(),head.clone());
        // 注意quick的判定条件
        while  quick!=None && quick.as_ref().unwrap().next!=None {
            slow=slow.as_ref().unwrap().next;
            quick=quick.as_ref().unwrap().next.as_ref().unwrap().next;
        }
        slow
    }
}
