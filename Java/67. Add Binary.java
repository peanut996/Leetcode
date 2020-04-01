// package Java;
// /*67. Add Binary
// 给定两个二进制字符串，返回他们的和（用二进制表示）。

// 输入为非空字符串且只包含数字 1 和 0。
// */
// class Solution {
//     public String addBinary(String a, String b) {
//         int tag=0;
//         StringBuilder builder =new StringBuilder();
//         for(int i=a.length()-1,j=b.length()-1;i>=0||j>=0;--i,--j){
//             int sum = tag;
//             sum+= i>=0 ? a.charAt(i)-'0':0;
//             sum+= j>=0 ? b.charAt(j)-'0':0;
//             builder.append(sum%2);
//             tag=sum/2;
//         }
//         builder.append(tag==1? tag:"");
//         return builder.reverse().toString();
//     }
// }