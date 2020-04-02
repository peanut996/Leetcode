// package Java;
// /*345. Reverse Vowels of a String
// 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

// 示例:
// 输入: "hello"
// 输出: "holle"
// */
// class Solution {
//     public String reverseVowels(String s) {
//         char[] c=s.toCharArray();
//         int l=0,r=s.length()-1;
//         while(l<=r){
//             while(l<=s.length()-1&&!isVowel(c[l])) l++;
//             while(r>=0&&!isVowel(c[r])) r--;
//             if(l<=r&&isVowel(c[l])&&isVowel(c[r])){
//                 swap(c,l,r);
//                 l++;r--;
//             }
//         }
//         return new String(c);
//     }
//     private void swap(char[] c,int i,int j){
//         char temp=c[i];
//         c[i]=c[j];
//         c[j]=temp;
//     }
//     private boolean isVowel(char ch) {
//         return ch == 'a' | ch == 'A' | ch == 'e' | ch == 'E' | ch == 'i'| ch == 'I'| ch == 'o'| ch == 'O'| ch == 'u'| ch == 'U';
//     }
// }