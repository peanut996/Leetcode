/**
 * 十大排序算法
 */
public class Sort {
  /**
   * 快速排序n 平均时间复杂度 n*log(n) 最坏n2
   * 
   * @param nums 待排序数组
   */
  public static void quickSort(int[] nums, int start, int end) {
    if (start >= end) {
      return;
    }
    int pivot = nums[start];
    int left = start, right = end;
    while (left < right) {
      // 先动右边
      while (left < right && nums[right] >= pivot) {
        right--;
      }
      if (left < right)
        nums[left] = nums[right];
      while (left < right && nums[left] <= pivot) {
        left++;
      }
      if (left < right)
        nums[right] = nums[left];
      if (left >= right)
        nums[left] = pivot;
    }

    quickSort(nums, start, left - 1);
    quickSort(nums, left + 1, end);
  }
}
