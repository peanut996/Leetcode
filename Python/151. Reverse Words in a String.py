#!/usr/bin/python3.7
"""151. Reverse Words in a String
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

def main():
    solution = Solution()
    str="the sky is blue"
    try:
        assert solution.reverseWords(str)=="blue is sky the"
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
