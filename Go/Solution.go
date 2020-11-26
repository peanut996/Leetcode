package main

import (
	"fmt"
)

func verifyPostorder(postorder []int) bool {
	var helper func(i, j int) bool
	helper = func(i, j int) bool {
		if i >= j {
			return true
		}
		pointer := i
		for postorder[pointer] < postorder[j] {
			pointer++
		}
		mid := pointer
		for postorder[pointer] > postorder[j] {
			pointer++
		}

		return pointer == j && helper(i, mid-1) && helper(mid, j-1)
	}
	return helper(0, len(postorder)-1)
}
func main() {
	fmt.Println("Hello World!")
}
