// package Java;
// /*415. Add Strings
// 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

// 注意：

//     num1 和num2 的长度都小于 5100.
//     num1 和num2 都只包含数字 0-9.
//     num1 和num2 都不包含任何前导零。
//     你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
// */
// class Solution {
//     public String addStrings(String num1, String num2) {
//         // 双指针倒序相加
//         int i=num1.length()-1,j=num2.length()-1,tag=0;
//         StringBuilder builder =new StringBuilder();
//         while(i>=0|j>=0){
//             int n1= i>=0? num1.charAt(i)-'0':0;
//             int n2= j>=0? num2.charAt(j)-'0':0;
//             int temp = n1+n2+tag;
//             tag = temp/10;
//             builder.append(temp%10);
//             i--;j--;
//         }
//         if(tag == 1) builder.append(1);
//         return builder.reverse().toString();
//     }
// }