"""
https://leetcode.com/problems/palindrome-partitioning/description/
"""
from typing import List


class Solution:

    def dfs(self, s, i, temp, result):
        if i >= len(s):
            result.append(temp[:])
            return
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                temp.append(s[i:j+1])
                self.dfs(s, j+1, temp, result)
                temp.pop()
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, 0, [], result)
        return result

solve = Solution()
print(solve.partition(s='aab'))