package Java;
/*28. Implement strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
*/
// class Solution{
//     public int strStr(String haystack, String needle) {
//         if (haystack.length()==0) return -1;
        
//         if (needle.length()==0) return 0;
//         for(int i=0;i<haystack.length();i++){
//             if (haystack.charAt(i)==needle.charAt(0)){
//                 int j=0;
//                 while (j<needle.length()){
//                     if (haystack.charAt(i+j)!=needle.charAt(j)){
//                         return -1;
//                     }
//                 }
//                 return i;
//             }
//         }
//         return -1;
//     }
//     public static void main(String[] args) {
//         System.out.println("Hello World!");
//     }
// }