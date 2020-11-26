package Java;

import java.util.Stack;

class MinStack {

  Stack<Integer> stack = new Stack<Integer>();
  Stack<Integer> minStack = new Stack<Integer>();
  /** initialize your data structure here. */
  public MinStack() {

  }
  public void push(int x) {
    stack.push(x);
    if(minStack.isEmpty()||x<=getMin()){
      minStack.push(x);
    }
  }
  
  public void pop() {
    // 注意这里equals 因为是Integer
    if(stack.pop().equals(minStack.peek())){
      minStack.pop();
    }
  }
  
  public int top() {
    return stack.peek();

  }
  
  public int getMin() {
    return minStack.peek();
  }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(x);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/