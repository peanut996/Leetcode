package main

/*169. Majority Element
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例:
输入: [3,2,3]
输出: 3

*/
// import "fmt"

func majorityElement(nums []int) int {
	m := make(map[int]int)
	for _, value := range nums {
		m[value]++
	}
	for key, value := range m {
		if value > len(nums)/2 {
			return key
		}
	}
	return 0
}

// func main() {
// 	nums := []int{6, 8, 8}
// 	fmt.Println(majorityElement(nums))
// }
