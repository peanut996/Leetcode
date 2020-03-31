package main

/*119. Pascal's Triangle II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
*/

// import "fmt"

func getRow(rowIndex int) []int {
	result := []int{1}
	for i := 1; i < rowIndex+1; i++ {
		result = append([]int{0}, result...)
		for index := range result {
			if index < i {
				result[index] = result[index+1] + result[index]
			}
		}
	}
	return result
}

// func main() {
// 	fmt.Println(getRow(5))
// }
