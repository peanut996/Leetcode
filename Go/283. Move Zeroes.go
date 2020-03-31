package main

/*283. Move Zeroes
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
*/
// import "fmt"

func moveZeroes(nums []int) {
	slow, quick := 0, 0
	for ; quick < len(nums); quick++ {
		if nums[quick] != 0 {
			nums[slow], nums[quick] = nums[quick], nums[slow]
			slow++
		}
	}
}

// func main() {
// 	nums := []int{0, 1, 0, 3, 12}
// 	moveZeroes(nums)
// 	fmt.Println(nums)
// }
