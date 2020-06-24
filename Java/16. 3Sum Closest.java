/**
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
 * 找出 nums 中的三个整数，使得它们的和与 target 最接近。
 * 返回这三个数的和。假定每组输入只存在唯一答案。
 * 
 */
// class Solution {
//     public int threeSumClosest(int[] nums, int target) {
//         // 先排序
//         Arrays.sort(nums);

//         // 双指针 
//         int res = nums[0] + nums[1] + nums[2];
//         for (int i = 0 ;i < nums.length; i++) {
//             int start = i + 1;
//             int end = nums.length - 1;
//             while (start < end){
//                 int sum = nums[i] + nums[start] + nums[end];
//                 if (Math.abs(target - res) > Math.abs(target - sum)){
//                     // 更新结果
//                     res = sum;
//                 }
//                 if (sum > target) {
//                     end--;
//                 }else if(sum < target) {
//                     start++;
//                 }else{
//                     return res;
//                 }
//             }
//         }
//         return res;
//     }
// }