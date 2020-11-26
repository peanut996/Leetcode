// package Java;

// import java.util.Arrays;

// 面试题 01.02. 判定是否互为字符重排
// 时间复杂度On， 空间复杂度O1
// class Solution {
//     public boolean CheckPermutation(String s1, String s2) {
//         if (s1.length() != s2.length()){
//             return false;
//         }
//         char[] c1 = s1.toCharArray();
//         char[] c2 = s2.toCharArray();
//         Arrays.sort(c1);
//         Arrays.sort(c2);
//         return Arrays.equals(c1, c2);
//     }
//     public static void main(String[] args) {
//         Solution s  = new Solution();
//         System.out.println(s.CheckPermutation("abs","asbb"));
//     }
// }