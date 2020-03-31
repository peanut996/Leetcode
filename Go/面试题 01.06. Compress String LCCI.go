package main

import "strconv"

/*

 */

func compressString(S string) string {
	if len(S) <= 1 {
		return S
	}
	res := ""
	slow, quick := 0, 0
	for quick < len(S) {
		quick++
		if S[quick] != S[slow] {
			res += string(S[slow]) + strconv.Itoa(quick-slow)
			slow = quick
		}
	}
	res += string(S[slow]) + strconv.Itoa(quick-slow)
	if len(res) > len(S) {
		return S
	}
	return res
}
