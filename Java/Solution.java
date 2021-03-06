import java.io.*;
import java.util.*;
class Solution {
    public int minArray(int[] numbers) {
        int length = numbers.length;
        for (int i = 1; i < length; i++) {
            if (numbers[i] < numbers[i - 1]) {
                return numbers[i];
            }
        }
        return numbers[0];
    }

    /**
     * 贪心 最小单元 1710. 卡车上的最大单元数 请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] =
     * [numberOfBoxesi, numberOfUnitsPerBoxi] ：
     * 
     * numberOfBoxesi 是类型 i 的箱子的数量。 numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。 整数
     * truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。
     * 
     * 返回卡车可以装载 单元 的 最大 总数。
     * 
     * @param boxTypes
     * @param truckSize
     * @return
     */
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (int[] o1, int[] o2) -> o2[1] - o1[1]);
        int index = 0, res = 0;
        while (index < boxTypes.length && truckSize > 0) {
            if (boxTypes[index][0] <= truckSize) {
                res += boxTypes[index][1] * boxTypes[index][0];
                truckSize -= boxTypes[index][0];
                index++;
            } else {
                res += boxTypes[index][1] * truckSize;
                break;
            }
        }
        return res;
    }

    /**
     * 
     * 两数之和变种
     * 
     * 1711. 大餐计数 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
     * 
     * 你可以搭配 任意 两道餐品做一顿大餐。
     * 
     * 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第i道菜的美味程度
     * 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。
     * 
     * 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
     * 
     * 
     * 
     * 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/count-good-meals
     * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
     * 
     * @param deliciousness
     * @return
     */
    public int countPairs(int[] deliciousness) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int mod = 1000000000 + 7;
        long res = 0;
        for (int n : deliciousness) {
            for (int i = 0; i < 22; i++) {
                if (map.containsKey((1 << i) - n)) {
                    res += map.get((1 << i) - n) % mod;
                }
            }
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        return (int) (res % mod);
    }

    /***
     * 返回 括号匹配的深度 /*1111. Maximum Nesting Depth of Two Valid Parentheses Strings
     * 
     * @param seq
     * @return
     */
    public int[] maxDepthAfterSplit(String seq) {
        int[] nums = new int[seq.length()];
        int tag = 0;
        for (char c : seq.toCharArray()) {
            nums[tag++] = c == '(' ? tag & 1 : (tag + 1) & 1;
        }
        return nums;
    }

    /***
     * 反转链表
     * 
     * @param head
     * @return
     */
    public ListNode ReverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        while (curr != null) {
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        return prev;
    }

    /**
     * 189.旋转数组
     * 
     * @param nums
     * @param k
     */
    public void rotate(int[] nums, int k) {
        // 两次循环
        // int length = nums.length;
        // int[] newNums = new int[length];
        // for (int i = 0; i < length; i++) {
        // newNums[(i+k)%length] = nums[i];
        // }
        // for (int i = 0; i < length; i++) {
        // nums[i]=newNums[i];
        // }

        // 三次翻转
        k %= nums.length;
        reverse(nums, nums.length - k, nums.length - 1);
        reverse(nums, 0, nums.length - k - 1);
        reverse(nums, 0, nums.length - 1);
    }

    /**
     * 123.买卖股票的最佳时间III
     * 
     * @param prices
     * @return
     */
    public int maxProfit(int[] prices) {
        return 0;
    }

    /**
     * 数组内翻转函数
     * 
     * @param nums
     * @param start
     * @param end
     */
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = temp;
        }
    }

    /**
     * 数组内交换函数
     * 
     * @param nums
     * @param i
     * @param j
     */
    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    /**
     * 最大得分 
     * @param s
     * @param x
     * @param y
     * @return
     */
    public int maximumGain(String s, int x, int y) {
        String str1 = "ab";
        String str2 = "ba";
        String blank = "";
        int res = 0;
        while (s.contains(str1) || s.contains(str2)) {
            if (x > y) {
                if (s.contains(str1)) {
                    s = s.replaceFirst(str1, blank);
                    res += x;
                    continue;
                }
                s = s.replaceFirst(str2, blank);
                res += y;
            } else {
                if (s.contains(str2)) {
                    s = s.replaceFirst(str2, blank);
                    res += y;
                    continue;
                }
                s = s.replaceFirst(str1, blank);
                res += x;
            }
        }
        return res;
    }
    static int count =1;
    public static int foo(int year){
        for(int i =0;i<=year;i++){
            if(i==2 || i==4){
                count ++;
                foo(year-i);
            }
            if (i==5){
                count --;
                break;
            }
        }
        return count;
    }
    
    public static void main(String[] args) {
        System.out.println(foo(15));
    }
}