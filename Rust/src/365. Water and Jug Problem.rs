/*365. Water and Jug Problem
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
你允许：

    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空

示例: (From the famous "Die Hard" example)
输入: x = 3, y = 5, z = 4
输出: True
*/
impl Solution {
  pub fn can_measure_water(x: i32, y: i32, z: i32) -> bool {
      fn gcd (x: i32,y :i32)-> i32 {
          if x%y==0{
              return y
          }else{
              return gcd(y,x%y)
          }
      }
      x+y>=z  && !(x==0||y==0) &&z%gcd(x,y)==0 ||z==0
      
  }
}
