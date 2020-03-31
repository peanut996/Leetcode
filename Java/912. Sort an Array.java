package Java;

// import java.util.Arrays;

/*912. Sort an Array
给定一个整数数组 nums，将该数组升序排列。
*/
// class Solution{
//     private void swap(int[] nums, int i, int j) {
//         int temp = nums[i];
//         nums[i] = nums[j];
//         nums[j] = temp;
//     }
//     public int[] sortArray(int[] nums){
//         Arrays.sort(nums);
//         return nums;
//     }
//     // 冒泡算法
//     public int[] bubbleSort(int[] nums) {
//         for(int i=nums.length-1;i>0;i--){
//             for (int j=1;j<=i;j++){
//                 if (nums[j-1]>nums[j]) swap(nums,j-1,j);
//             }
//         }
//         return nums;
//     }

//     // 选择排序
//     public int[] selectionSort(int[] nums){
//         for(int i=nums.length-1;i>0;++i){
//             int max = 0;
//             for (int j=0;j<=i;++j){
//                 if (nums[max]<nums[j]) max=j;
//             }
//             swap(nums,max,i);
//         }
//         return nums;
//     }

//     // 插入排序
//     public int[] insertionSort(int[] nums) {
//         for(int i=1;i<nums.length;++i){
//             int j=i;
//             while( j>0 && nums[j-1]>nums[j]){
//                 swap(nums, j-1, j);
//                 --j;
//             }
//         }
//         return nums;
//     }

//     // 希尔排序
//     public int[] shellSort(int[] nums) {
//         int gap = nums.length>>1;
//         while(gap > 0){
//             for (int i=0;i<gap;++i){
//                 // 插入排序
//                 for(int j=i+gap;j<nums.length;j+=gap){
//                     int temp=j;
//                     while(temp>i&&nums[temp-gap]>nums[temp]){
//                         swap(nums,temp-gap,temp);
//                         temp-=gap;
//                     }
//                 }
//             }
//             gap>>=1;
//         }
//         return nums;
//     }
//     public int[] mergeSort(int[] nums,int left,int right){
//         if (left >= right){
//             return nums;
//         }
//         int mid =(left+right)/2;
//         mergeSort(nums,left,mid);
//         mergeSort(nums,mid+1,right);
//         // 合并
//         int[] temp = new int[right-left+1];
//         int i=left,j=mid+1,curr=0;
//         while(i<=mid&&j<=right){
//             if(nums[i]>nums[j]){
//                 temp[curr++]=nums[j++];
//             }else{
//                 temp[curr++]=nums[i++];
//             }
//         }
//         while(i<=mid) temp[curr++]=nums[i++];
//         while(j<=right) temp[curr++]=nums[j++];

//         // 拷贝回去
//         for(int k=0;k<temp.length;++k){
//             nums[left+k]=temp[k];
//         }
//         return nums;
//     }

//     // 快速排序
//     public int[] quickSort(int[] nums,int left,int right){
//         if(left>=right) return nums;
//         // 初始值为nums[left]
//         int low=left+1,high=right;
//         while(low<=high){
//             if(nums[low]>nums[left]){
//                 swap(nums,low,high);
//                 high--;
//             }else{
//                 low++;
//             }
//         }
//         low--;
//         swap(nums,left,low);
//         quickSort(nums,left,low-1);
//         quickSort(nums,high+1,right);
//         return nums;
//     }
//     public int[] heapSort(int[] nums) {
//         heapify(nums);                                 // 新建一个最大堆
//         for (int i = nums.length - 1; i >= 1; i--) {
//             swap(nums, 0, i);                       // 弹出最大堆的堆顶放在最后
//             rebuildHeap(nums, 0,i-1);          // 重建最大堆
//         }
//         return nums;
//     }
    
//     private void heapify(int[] nums) {
//         for (int i = 1; i < nums.length; i++) {
//             int par = (i-1)>>1;                       // 找到父节点
//             int child = i;                            // 定义子节点
//             while (child>0&&nums[par]<nums[child]) {  // 从子节点到根节点构建最大堆
//                 swap(nums, par, child);
//                 child = par;
//                 par = (par-1) >> 1;
//             }
//         }
//     }
    
//     private void rebuildHeap(int[] nums, int par, int last) {
//         int left = 2*par+1;                           // 左子节点
//         int right = 2*par+2;                          // 右子节点
//         int maxIndex = left;
    
//         if (right<=last && nums[right]>nums[left]) {  // 找到最大子节点
//             maxIndex = right;
//         }
    
//         if (left<=last && nums[par] < nums[maxIndex]) {// 和最大子节点比较
//             swap(nums, par, maxIndex);                 // 互换到最大子节点
//             rebuildHeap(nums, maxIndex, last);         // 重建最大子节点代表的子树
//         }
//     }
//     public static void main(String[] args) {
//         Solution s =new Solution();
//         int[] nums= new int[]{5,4,7,3,2,1};
//         s.heapSort(nums);
//         System.out.println( Arrays.toString(nums));
//     }
// }