package main

import "strings"

/*1160. Find Words That Can Be Formed by Characters
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。



示例：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
*/

func countCharacters(words []string, chars string) int {
	res := 0
loop:
	for _, s := range words {
		for _, b := range s {
			if strings.Count(s, string(b)) > strings.Count(chars, string(b)) {
				continue loop
			}
		}
		res += len(s)
	}
	return res

}
