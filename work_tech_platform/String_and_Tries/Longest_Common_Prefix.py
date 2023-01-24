"""
https://workat.tech/problem-solving/practice/longest-common-prefix
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s[0]
        end = -1
        flag = True
        while flag:
            end += 1
            for i in range(1, len(s)):
                if len(s[i]) <= end or s[0][end] != s[i][end]:
                    flag = False
                    break
        return s[0][:end] if end >= 0 else ''


solve = Solution()

print(solve.longestCommonPrefix(s=["apple", "apply", "apollo", "abracadabra"]))

print(solve.longestCommonPrefix(s=["qwerty", "hello"]))


print(solve.longestCommonPrefix(s=["helloworld", "hell", "hello"]))