/*面试题51. 数组中的逆序对  LCOF

*/
impl Solution {
    pub fn reverse_pairs(nums: Vec<i32>) -> i32 {

        // 纯暴力解法不可取 但LeetCode没有卡用例
        // let mut res:i32 = 0;
        // for i in 0..nums.len(){
        //     for j in i+1..nums.len(){
        //         if nums[i]>nums[j]{
        //             res+=1;
        //         }
        //     }
        // }
        // res
    
        // 特殊用例
        if nums.len()<=1{
            return 0;
        }

        let mut res = 0i32;
        let length = nums.len();
        let mut nums = nums;
        
        fn merge(nums: &mut Vec<i32>,start: usize,end: usize,res: &mut i32){
            let mut nums_copy:Vec<i32> = vec![];
            let mid = start + ((end - start)>>1);
            let (mut i,mut j) = (start,mid+1);
            while i<=mid && j<=end{
                if nums[i]<=nums[j]{
                    nums_copy.push(nums[i]);
                    i+=1;
                }else{
                    // 和归并排序不同点
                    *res+=(mid - i + 1) as i32;
                    nums_copy.push(nums[j]);
                    j+=1;
                }
            }
            while i<=mid{
                nums_copy.push(nums[i]);
                i+=1;
            }
            while j<=end{
                nums_copy.push(nums[j]);
                j+=1;
            }
            for n in 0..nums_copy.len(){
                nums[start+n]=nums_copy[n];
            }
            
        }
    
        fn mergeSort(nums:&mut Vec<i32>,start: usize,end: usize,res: &mut i32){
            if start >= end {
                return;
            }
            // 防止溢出
            let mid  = start + ((end- start)>>1);
            mergeSort(nums,start,mid, res);
            mergeSort(nums,mid+1,end, res);
            merge(nums, start, end, res);
        }
    
        mergeSort(&mut nums,0,length-1,&mut res);
        res
    }
}