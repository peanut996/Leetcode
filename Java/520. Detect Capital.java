// package Java;
// /*520. Detect Capital
// 给定一个单词，你需要判断单词的大写使用是否正确。

// 我们定义，在以下情况时，单词的大写用法是正确的：

//     全部字母都是大写，比如"USA"。
//     单词中所有字母都不是大写，比如"leetcode"。
//     如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。

// 否则，我们定义这个单词没有正确使用大写字母。
// */
// class Solution {
//     public boolean detectCapitalUse(String word) {
//         int tag=0;
//         char[] words = word.toCharArray();
//         for(int i=0;i<word.length();i++){
//             // 这里的&&具有熔断作用 假如不是大写字符 那么tag++也不会执行
//             if(words[i]<=90 && tag++<i){
//                 return false;
//             }
//         }
//         return tag==words.length || tag<=1;
//     }
// }