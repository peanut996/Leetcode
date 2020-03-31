package main

/*414. Third Maximum Number
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.
*/
import (
	"math"
)

func thirdMax(nums []int) int {
	first, second, third := math.MinInt64, math.MinInt64, math.MinInt64
	for _, num := range nums {
		if num > third {
			if num > second {
				if num > first {
					third, second, first = second, first, num
					continue
				} else if num < first {
					third, second = second, num
				}
			} else if num < second {
				third = num
			}
		}
	}
	if third == math.MinInt64 {
		return first
	}
	return third
}

// func main() {
// 	nums := []int{3, 2, 2, 1}
// 	fmt.Println(thirdMax(nums))

// }
