"""
424. 替换后的最长重复字符

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。

示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_history = 0
        char_count = [0] * 26
        while r < len(s):
            index = ord(s[r]) - ord('A')
            char_count[index] += 1
            max_history = max(max_history, char_count[index])
            if r-l+1 > max_history+k:
                # 窗口滑动条件 窗口大小大于当前max + k
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return len(s) - l
