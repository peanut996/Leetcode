package main

/*1071. Greatest Common Divisor of Strings
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

*/

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}
	for {
		diff := len(str1) - len(str2)
		if diff == 0 {
			return str1
		} else if diff > 0 {
			str1 = str1[len(str2):]
		} else {
			str2 = str2[len(str1):]
		}
	}
}

// func main() {
// 	str1, str2 := "ABCABC", "ABC"
// 	fmt.Println(gcdOfStrings(str1, str2))
// }
