// package Java;
// /*387. First Unique Character in a String
// 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

// 案例:
// s = "leetcode"
// 返回 0.
// s = "loveleetcode",
// 返回 2.

// 注意事项：您可以假定该字符串只包含小写字母。

// */
// class Solution {
//     public int firstUniqChar(String s) {
//         int[] caps=new int[26];
//         for(char c:s.toCharArray()){
//             caps[c-'a']++;
//         }
//         for(char c:s.toCharArray()){
//             if(caps[c-'a']==1){
//                 return s.indexOf(c);
//             }
//         }
//         return -1;
//     }
// }
