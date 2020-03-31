package main

import "math"

/*559. Maximum Depth of N-ary Tree
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
我们应返回其最大深度，3。

说明:

    树的深度不会超过 1000。
    树的节点总不会超过 5000。

*/

func maxDepthOfNary(root *Node) int {
	if root == nil {
		return 0
	}
	res := 0
	for _, child := range root.Children {
		depth := maxDepthOfNary(child)
		res = int(math.Max(float64(res), float64(depth)))
	}
	return res + 1
}
