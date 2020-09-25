/*66. Plus One
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
*/
package main

// import "fmt"

func plusOne(digits []int) []int {
	length := len(digits)
	list := []int{1}
	list[0] = 1
	for i := length - 1; i >= 0; i-- {
		digits[i]++
		if digits[i]%10 != 0 {
			return digits
		}
		digits[i] = 0
	}
	return append(list, digits...)

}

// func main() {
// 	digits := []int{1, 2, 3}
// 	fmt.Println(plusOne(digits))
// }
