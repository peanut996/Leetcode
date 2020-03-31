// package Java;
// /*88. Merge Sorted Array
// 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

// 示例：
// 输入:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3
// 输出: [1,2,2,3,5,6]
// */

// class Solution{
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         int[] list=new int[m+n];
//         int a=0,b=0;
//         if(m==0){
//             System.arraycopy(nums2, 0, nums1, 0, nums2.length);
//         }else if(n==0){
//             return;
//         }else{
//             for (int i=0;i<list.length;i++) {
//                 if(a<m&&b<n){
//                     if(nums1[a]<nums2[b]){
//                         list[i]=nums1[a++];
//                     }else{
//                         list[i]=nums2[b++];
//                     }
//                 }else if(a>=m&&b<n){
//                     list[i]=nums2[b++];
//                 }else if(a<m&&b>=n){
//                     list[i]=nums1[a++];
//                 }
//             }
//             System.arraycopy(list, 0, nums1, 0, m+n);
//         }
//     }
//     public static void main(String[] args) {
//         Solution solution =new Solution();
//         solution.merge(new int[]{2,0}, 1,new int[]{1}, 1);
//     }
// }