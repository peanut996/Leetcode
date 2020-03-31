use std::rc::Rc;
use std::cell::RefCell;


pub struct Solution{
}

impl Solution{
  pub fn gcd(x: i32,y :i32)-> i32{
    if x==0||y==0{
      panic!("Stack Overflow. No GCD Warning.");
    }
  
    // 更相减损术
    // if x<y{
    //   gcd(y, x)
    // }else {
    //   if x==y{
    //     x
    //   }else {
    //     gcd(x-y,y)
    //   }
    // }
  
    // 辗转相除法
    if x%y==0{
      return y
    }else{
      return Solution::gcd(y,x%y)
    }
  }
}

//--------------------------------------------------------
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

#[allow(dead_code)]
impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

//--------------------------------------------------------
// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
  #[inline]
  pub fn from_vec(nums: Vec<i32>)->Option<Rc<RefCell<TreeNode>>>{
    if nums.len()==0{
      return None;
    }
    let head = Some(Rc::new(RefCell::new(TreeNode::new(nums[0]))));
    let mut queue: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();
    queue.push(head.clone());

    let mut i=1;
    while i < nums.len(){
      if !queue.is_empty(){
        if let Some(node)=queue.remove(0) {
          let mut node = node.borrow_mut();
          if nums[i]!=-1{
            // println!("{}",i);
            node.left=Some(Rc::new(RefCell::new(TreeNode::new(nums[i]))));
            queue.push(node.left.clone());
          }
          i+=1;
          if i==nums.len(){
            break;
          }
          if nums[i]!=-1{
            node.right=Some(Rc::new(RefCell::new(TreeNode::new(nums[i]))));
            queue.push( node.right.clone());
          }
          i+=1;

        }
      }else {
        break;
      }
    }
    head
  }
  #[inline]
  pub fn into_vec(root: Option<Rc<RefCell<TreeNode>>>)->Vec<i32>{
    let mut nums: Vec<i32>=Vec::new();
    if let Some(root)= root{
      let mut queue:Vec<Option<Rc<RefCell<TreeNode>>>> =Vec::new();
      queue.push(Some(root).clone());
      while !queue.is_empty(){
        let node =queue.remove(0);
        if node !=None{
          let node = node.unwrap();
          let node=node.borrow();
          nums.push(node.val);
          // 叶子结点自动被过滤
          if !(node.left==None && node.right==None ) {
            // println!("{:?},{:?}",node.left,node.right);
            queue.push(node.left.clone());
            queue.push(node.right.clone());
          }
        }else {
          nums.push(-1);
        }
      }
    }
    nums
  }
  #[inline]
  #[allow(unused_assignments)]
  pub fn inorder_morris_traversal(root: Option<Rc<RefCell<TreeNode>>>) ->Vec<i32> {
    // 1. 如果当前节点的左孩子为空，则**输出当前节点**并将其右孩子作为当前节点。
    // 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
    //    a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
    //    b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。**输出当前节点**。当前节点更新为当前节点的右孩子。
    let mut nums: Vec<i32> = Vec::new();
    let mut prev: Option<Rc<RefCell<TreeNode>>> = None;
    let mut curr: Option<Rc<RefCell<TreeNode>>> = root;
    while curr != None {
      if curr.as_ref().unwrap().borrow().left == None {    //1
        nums.push(curr.as_ref().unwrap().borrow().val);
        curr =curr.clone().unwrap().borrow().right.clone();
      }else{                                               //2
        prev=curr.clone().as_ref().unwrap().borrow().left.clone();

        while prev.as_ref().unwrap().borrow().right!=None && prev.as_ref().unwrap().borrow().right!=curr {
          prev=prev.clone().unwrap().borrow().right.clone();
        }

        if prev.as_ref().unwrap().borrow().right==None{       //2.a
          prev.unwrap().borrow_mut().right=curr.clone();
          curr=curr.unwrap().borrow().left.clone();
        }else{                                                //2.b
          prev.as_ref().unwrap().borrow_mut().right=None;
          nums.push(curr.as_ref().unwrap().borrow().val);
          curr =curr.clone().unwrap().borrow().right.clone();
        }
      }
    }
    nums
  }

  #[inline]
  #[allow(unused_assignments)]
  pub fn preorder_morris_traversal(root: Option<Rc<RefCell<TreeNode>>>) ->Vec<i32> {
    // 1. 如果当前节点的左孩子为空，则**输出当前节点**并将其右孩子作为当前节点。
    // 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
    //    a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。**输出当前节点**。
    //    b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。当前节点更新为当前节点的右孩子。
    let mut nums: Vec<i32> = Vec::new();
    let mut prev: Option<Rc<RefCell<TreeNode>>> = None;
    let mut curr: Option<Rc<RefCell<TreeNode>>> = root;
    while curr != None {
      if curr.as_ref().unwrap().borrow().left == None {    //1
        nums.push(curr.as_ref().unwrap().borrow().val);
        curr =curr.clone().unwrap().borrow().right.clone();
      }else{                                               //2

        prev=curr.clone().as_ref().unwrap().borrow().left.clone();

        while prev.as_ref().unwrap().borrow().right!=None && prev.as_ref().unwrap().borrow().right!=curr {
          prev=prev.clone().unwrap().borrow().right.clone();
        }


        if prev.as_ref().unwrap().borrow().right==None{       //2.a
          nums.push(curr.as_ref().unwrap().borrow().val);
          prev.unwrap().borrow_mut().right=curr.clone();
          curr=curr.unwrap().borrow().left.clone();
        }else{                                                //2.b
          prev.as_ref().unwrap().borrow_mut().right=None;
          curr =curr.clone().unwrap().borrow().right.clone();
        }
      }
    }
    nums
  }
  #[inline]
  #[allow(unused_assignments)]
  pub fn postorder_morris_traversal(root: Option<Rc<RefCell<TreeNode>>>) ->Vec<i32> {
    // 翻转链表实现
    fn push_reverse(from: Option<Rc<RefCell<TreeNode>>>,to: Option<Rc<RefCell<TreeNode>>>,nums: &mut Vec<i32>){
      let mut tmp:Vec<i32> = Vec::new();
      let mut from =from.clone();
      tmp.push(from.as_ref().unwrap().borrow().val);
      if from==to {
        nums.push(from.as_ref().unwrap().borrow().val);
        return;
      }
      while from!=to{
        from=from.clone().unwrap().borrow().right.clone();
        tmp.push(from.as_ref().unwrap().borrow().val);
      }
      while !tmp.is_empty(){
        nums.push(tmp.pop().unwrap());
      }
    }
    // 设置当前节点为临时结点
    // 1. 如果当前节点的左孩子为空，则将其右孩子作为当前节点。
    // 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
    //    a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
    //    b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。**倒序输出当前节点左孩子到前序结点的所有节点**当前节点更新为当前节点的右孩子。
    let mut nums: Vec<i32> = Vec::new();
    let mut prev: Option<Rc<RefCell<TreeNode>>> = None;
    let mut curr: Option<Rc<RefCell<TreeNode>>> = Some(Rc::new(RefCell::new(TreeNode::new(0))));
    curr.as_ref().unwrap().borrow_mut().left=root;
    while curr != None {
      if curr.as_ref().unwrap().borrow().left == None {    //1
        curr =curr.clone().unwrap().borrow().right.clone();
      }else{                                               //2
        // 寻找前序节点
        prev=curr.clone().as_ref().unwrap().borrow().left.clone();
        while prev.as_ref().unwrap().borrow().right!=None && prev.as_ref().unwrap().borrow().right!=curr {          
          prev=prev.clone().unwrap().borrow().right.clone();
        }

        if prev.as_ref().unwrap().borrow().right==None{       //2.a
          prev.unwrap().borrow_mut().right=curr.clone();
          curr=curr.unwrap().borrow().left.clone();
        }else{                                                //2.b
          push_reverse(curr.as_ref().unwrap().borrow().left.clone(),prev.clone(),&mut nums);
          prev.as_ref().unwrap().borrow_mut().right=None;
          curr =curr.clone().unwrap().borrow().right.clone();
        }
      }
    }
    nums
  }
}
