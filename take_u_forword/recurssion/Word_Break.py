"""
https://leetcode.com/problems/word-break/description/
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cut = {0: True}
        for i in range(1, len(s) + 1):
            cut[i] = False
            for j in range(i):
                if cut[j] and s[j:i] in words:
                    cut[i] = True
                    break
        return cut[len(s)]

solve = Solution()
print(solve.wordBreak(s='applepenapple', wordDict=["apple","pen"]))
