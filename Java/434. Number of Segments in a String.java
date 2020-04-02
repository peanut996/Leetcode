// package Java;
// /*434. Number of Segments in a String
// 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

// 请注意，你可以假定字符串里不包括任何不可打印的字符。

// 示例:

// 输入: "Hello, my name is John"
// 输出: 5
// */
// class Solution {
//     public int countSegments(String s) {
//         int i=0,length=s.length(),res=0;
//         while(i<length){
//             while(i<length&&s.charAt(i)==' ') i++;
//             if(i==length) break;
//             while(i<length&&s.charAt(i)!=' ') i++;
//             res++;
//         }
//         return res;
//     }
// }