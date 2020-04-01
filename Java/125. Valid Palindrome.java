// package Java;
// /*125. Valid Palindrome
// 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
// 说明：本题中，我们将空字符串定义为有效的回文串。
// */
// class Solution {
//     public boolean isPalindrome(String s) {
//         int l=0,r=s.length()-1;
//         while(l < r){
//             while(l<r & !Character.isLetterOrDigit(s.charAt(l))) l++;
//             while(l<r & !Character.isLetterOrDigit(s.charAt(r))) r--;
//             if(Character.toLowerCase(s.charAt(l)) !=  Character.toLowerCase(s.charAt(r))) return false;
//             l++;r--;
//         }
//         return true;
//     }
// }
