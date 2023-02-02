"""
https://leetcode.com/problems/palindrome-partitioning/submissions/886694612/

https://www.youtube.com/watch?v=WBgsABoClE0&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=17
"""
from typing import List


class Solution:
    @staticmethod
    def is_palindrome(x):
        return x == x[::-1]

    def dfs(self, s, i, part, result):
        if i >= len(s):
            result.append(part[:])
            return
        for j in range(i, len(s)):
            if self.is_palindrome(s[i:j+1]):
                part.append(s[i:j+1])
                self.dfs(s, j+1, part, result)
                part.pop()
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, 0, [], result)
        return result

solve = Solution()
print(solve.partition(s='aab'))
